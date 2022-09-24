#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x143ac14f

# Compiled with Coconut version 2.0.0-a_dev65 [How Not to Be Seen]

"""
The mixture backend. Lets you specify a distribution over different possible algorithms.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:  # type: ignore
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == str("__coconut__"):
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



from bbopt import constants  #5 (line num in coconut source)
from bbopt.util import convert_match_errors  #6 (line num in coconut source)
from bbopt.registry import alg_registry  #7 (line num in coconut source)
from bbopt.backends.util import Backend  #8 (line num in coconut source)
from bbopt.backends.util import get_backend  #8 (line num in coconut source)
from bbopt.backends.util import get_cum_probs_for  #8 (line num in coconut source)
from bbopt.backends.util import random_from_cum_probs  #8 (line num in coconut source)


# Backend:

class MixtureBackend(Backend):  #18 (line num in coconut source)
    """Mixture backend. Takes in a distribution over different possible algorithms
    of the form [(algorithm, weight)]. The properties selected_alg and selected_backend
    can be used to retrieve which alg/backend is currently being used."""  #21 (line num in coconut source)

    backend_name = "mixture"  #23 (line num in coconut source)
    request_backend_store = True  #24 (line num in coconut source)
    remove_erroring_algs = None  #25 (line num in coconut source)

    @override  #27 (line num in coconut source)
    @convert_match_errors  #28 (line num in coconut source)
    @_coconut_mark_as_match  #29 (line num in coconut source)
    def attempt_update(*_coconut_match_args, **_coconut_match_kwargs):  #29 (line num in coconut source)
        """Special method that allows fast updating of the backend."""  #30 (line num in coconut source)
        _coconut_match_check_0 = False  #31 (line num in coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #31 (line num in coconut source)
        _coconut_match_set_name_examples = _coconut_sentinel  #31 (line num in coconut source)
        _coconut_match_set_name_params = _coconut_sentinel  #31 (line num in coconut source)
        _coconut_match_set_name_distribution = _coconut_sentinel  #31 (line num in coconut source)
        _coconut_match_set_name_remove_erroring_algs = _coconut_sentinel  #31 (line num in coconut source)
        _coconut_match_set_name__backend_store = _coconut_sentinel  #31 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #31 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 5) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "params" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "distribution" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 4, "remove_erroring_algs" in _coconut_match_kwargs)) <= 1):  #31 (line num in coconut source)
            _coconut_match_temp_5 = _coconut_match_kwargs.pop("_backend_store") if "_backend_store" in _coconut_match_kwargs else _coconut_sentinel  #31 (line num in coconut source)
            if _coconut_match_temp_5 is not _coconut_sentinel:  #31 (line num in coconut source)
                _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #31 (line num in coconut source)
                _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("examples")  #31 (line num in coconut source)
                _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("params")  #31 (line num in coconut source)
                _coconut_match_temp_3 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("distribution")  #31 (line num in coconut source)
                _coconut_match_temp_4 = _coconut_match_args[4] if _coconut.len(_coconut_match_args) > 4 else _coconut_match_kwargs.pop("remove_erroring_algs") if "remove_erroring_algs" in _coconut_match_kwargs else False  #31 (line num in coconut source)
                _coconut_match_set_name__backend_store = _coconut_match_temp_5  #31 (line num in coconut source)
                _coconut_match_set_name_self = _coconut_match_temp_0  #31 (line num in coconut source)
                _coconut_match_set_name_examples = _coconut_match_temp_1  #31 (line num in coconut source)
                _coconut_match_set_name_params = _coconut_match_temp_2  #31 (line num in coconut source)
                _coconut_match_set_name_distribution = _coconut_match_temp_3  #31 (line num in coconut source)
                _coconut_match_set_name_remove_erroring_algs = _coconut_match_temp_4  #31 (line num in coconut source)
                if not _coconut_match_kwargs:  #31 (line num in coconut source)
                    _coconut_match_check_0 = True  #31 (line num in coconut source)
        if _coconut_match_check_0:  #31 (line num in coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #31 (line num in coconut source)
                self = _coconut_match_set_name_self  #31 (line num in coconut source)
            if _coconut_match_set_name_examples is not _coconut_sentinel:  #31 (line num in coconut source)
                examples = _coconut_match_set_name_examples  #31 (line num in coconut source)
            if _coconut_match_set_name_params is not _coconut_sentinel:  #31 (line num in coconut source)
                params = _coconut_match_set_name_params  #31 (line num in coconut source)
            if _coconut_match_set_name_distribution is not _coconut_sentinel:  #31 (line num in coconut source)
                distribution = _coconut_match_set_name_distribution  #31 (line num in coconut source)
            if _coconut_match_set_name_remove_erroring_algs is not _coconut_sentinel:  #31 (line num in coconut source)
                remove_erroring_algs = _coconut_match_set_name_remove_erroring_algs  #31 (line num in coconut source)
            if _coconut_match_set_name__backend_store is not _coconut_sentinel:  #31 (line num in coconut source)
                _backend_store = _coconut_match_set_name__backend_store  #31 (line num in coconut source)
        if not _coconut_match_check_0:  #31 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def attempt_update(self, examples, params, distribution, remove_erroring_algs=False, *, _backend_store):', _coconut_match_args)  #31 (line num in coconut source)

        self.use_distribution(distribution, force=remove_erroring_algs != self.remove_erroring_algs)  #31 (line num in coconut source)

        self.examples = examples  #33 (line num in coconut source)
        self.params = params  #34 (line num in coconut source)
        self.remove_erroring_algs = remove_erroring_algs  #35 (line num in coconut source)
        self.backend_store = _backend_store  #36 (line num in coconut source)

        self.select_new_backend()  #38 (line num in coconut source)
        return True  #39 (line num in coconut source)


    def use_distribution(self, distribution, force=False):  #41 (line num in coconut source)
        """Set the distribution to the given distribution."""  #42 (line num in coconut source)
        distribution = tuple(((alg, weight() if callable(weight) else weight) for alg, weight in distribution))  #43 (line num in coconut source)

        if force or distribution != self.distribution:  #48 (line num in coconut source)
            self.cum_probs = get_cum_probs_for(distribution)  #49 (line num in coconut source)
            self.distribution = distribution  #50 (line num in coconut source)


    def select_new_backend(self):  #52 (line num in coconut source)
        """Randomly select a new backend."""  #53 (line num in coconut source)
# randomly select algorithm
        self.selected_alg = random_from_cum_probs(self.cum_probs)  #55 (line num in coconut source)
        if self.selected_alg is None:  #56 (line num in coconut source)
            raise ValueError("could not select backend from distribution: {_coconut_format_0}".format(_coconut_format_0=(self.distribution)))  #57 (line num in coconut source)

# initialize backend
        self.selected_backend, options = alg_registry[self.selected_alg]  #60 (line num in coconut source)
        try:  #61 (line num in coconut source)
            self.current_backend = get_backend(self.backend_store, self.selected_backend, self.examples, self.params, **options)  #62 (line num in coconut source)
        except constants.erroring_backend_errs:  #69 (line num in coconut source)
            if not self.remove_erroring_algs:  #70 (line num in coconut source)
                raise  #71 (line num in coconut source)
            self.reselect_backend()  #72 (line num in coconut source)


    def reselect_backend(self):  #74 (line num in coconut source)
        """Choose a new backend when the current one errors."""  #75 (line num in coconut source)
        new_distribution = []  #76 (line num in coconut source)
        for alg, weight in self.distribution:  #77 (line num in coconut source)
            if alg != self.selected_alg:  #78 (line num in coconut source)
                new_distribution.append((alg, weight))  #79 (line num in coconut source)
        self.cum_probs = get_cum_probs_for(new_distribution)  #80 (line num in coconut source)
        self.select_new_backend()  #81 (line num in coconut source)


    @override  #83 (line num in coconut source)
    def param(self, name, func, *args, **kwargs):  #84 (line num in coconut source)
        """Defer parameter selection to the selected backend."""  #85 (line num in coconut source)
        try:  #86 (line num in coconut source)
            return self.current_backend.param(name, func, *args, **kwargs)  #87 (line num in coconut source)
        except constants.erroring_backend_errs:  #88 (line num in coconut source)
            if not self.remove_erroring_algs:  #89 (line num in coconut source)
                raise  #90 (line num in coconut source)
            self.reselect_backend()  #91 (line num in coconut source)
        return self.param(name, func, *args, **kwargs)  #92 (line num in coconut source)


    @classmethod  #94 (line num in coconut source)
    def register_safe_alg_for(cls, base_alg, new_alg_name=None, fallback_alg=None):  #95 (line num in coconut source)
        """Register a version of base_alg that defaults to the fallback if base_alg fails."""  #96 (line num in coconut source)
        if new_alg_name is None:  #97 (line num in coconut source)
            new_alg_name = "safe_" + base_alg  #98 (line num in coconut source)
        if fallback_alg is None:  #99 (line num in coconut source)
            fallback_alg = constants.safe_fallback_alg  #100 (line num in coconut source)
        cls.register_alg(new_alg_name, distribution=((base_alg, float("inf")), (fallback_alg, 1)), remove_erroring_algs=True)  #101 (line num in coconut source)


    @classmethod  #110 (line num in coconut source)
    def register_epsilon_exploration_alg_for(cls, base_alg, new_alg_name=None, eps=None):  #111 (line num in coconut source)
        """Register a version of base_alg with epsilon greedy exploration."""  #112 (line num in coconut source)
        if new_alg_name is None:  #113 (line num in coconut source)
            new_alg_name = "epsilon_" + base_alg  #114 (line num in coconut source)
        cls.register_alg(new_alg_name, distribution=((base_alg, lambda _=None: 1 - ((constants.eps_greedy_explore_prob if eps is None else eps))), ("random", lambda _=None: (constants.eps_greedy_explore_prob if eps is None else eps))))  #115 (line num in coconut source)




# Registered names:


_coconut_call_set_names(MixtureBackend)  #130 (line num in coconut source)
MixtureBackend.register()  #130 (line num in coconut source)

MixtureBackend.register_epsilon_exploration_alg_for("max_greedy")  #132 (line num in coconut source)

MixtureBackend.register_safe_alg_for("gaussian_process")  #134 (line num in coconut source)
MixtureBackend.register_safe_alg_for("random_forest")  #135 (line num in coconut source)
MixtureBackend.register_safe_alg_for("extra_trees")  #136 (line num in coconut source)
MixtureBackend.register_safe_alg_for("gradient_boosted_regression_trees")  #137 (line num in coconut source)
