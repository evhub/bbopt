#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa4e2b940

# Compiled with Coconut version 3.0.0-a_dev36

"""
The mixture backend. Lets you specify a distribution over different possible algorithms.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
_coconut_header_info = ('3.0.0-a_dev36', '', True)
import os as _coconut_os
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in
if _coconut_pop_path:
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



from bbopt import constants  #5 (line in Coconut source)
from bbopt.util import convert_match_errors  #6 (line in Coconut source)
from bbopt.registry import alg_registry  #7 (line in Coconut source)
from bbopt.backends.util import Backend  #8 (line in Coconut source)
from bbopt.backends.util import get_backend  #8 (line in Coconut source)
from bbopt.backends.util import get_cum_probs_for  #8 (line in Coconut source)
from bbopt.backends.util import random_from_cum_probs  #8 (line in Coconut source)


# Backend:

class MixtureBackend(Backend):  #18 (line in Coconut source)
    """Mixture backend. Takes in a distribution over different possible algorithms
    of the form [(algorithm, weight)]. The properties selected_alg and selected_backend
    can be used to retrieve which alg/backend is currently being used."""  #21 (line in Coconut source)

    backend_name = "mixture"  #23 (line in Coconut source)
    request_backend_store = True  #24 (line in Coconut source)
    remove_erroring_algs = None  #25 (line in Coconut source)

    @override  #27 (line in Coconut source)
    @convert_match_errors  #28 (line in Coconut source)
    @_coconut_mark_as_match  #29 (line in Coconut source)
    def attempt_update(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #29 (line in Coconut source)
        """Special method that allows fast updating of the backend."""  #30 (line in Coconut source)
        _coconut_match_check_0 = False  #31 (line in Coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #31 (line in Coconut source)
        _coconut_match_set_name_examples = _coconut_sentinel  #31 (line in Coconut source)
        _coconut_match_set_name_params = _coconut_sentinel  #31 (line in Coconut source)
        _coconut_match_set_name_distribution = _coconut_sentinel  #31 (line in Coconut source)
        _coconut_match_set_name_remove_erroring_algs = _coconut_sentinel  #31 (line in Coconut source)
        _coconut_match_set_name__backend_store = _coconut_sentinel  #31 (line in Coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #31 (line in Coconut source)
        if _coconut_match_first_arg is not _coconut_sentinel:  #31 (line in Coconut source)
            _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #31 (line in Coconut source)
        if (_coconut.len(_coconut_match_args) <= 5) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "params" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "distribution" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 4, "remove_erroring_algs" in _coconut_match_kwargs)) <= 1):  #31 (line in Coconut source)
            _coconut_match_temp_5 = _coconut_match_kwargs.pop("_backend_store") if "_backend_store" in _coconut_match_kwargs else _coconut_sentinel  #31 (line in Coconut source)
            if _coconut_match_temp_5 is not _coconut_sentinel:  #31 (line in Coconut source)
                _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #31 (line in Coconut source)
                _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("examples")  #31 (line in Coconut source)
                _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("params")  #31 (line in Coconut source)
                _coconut_match_temp_3 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("distribution")  #31 (line in Coconut source)
                _coconut_match_temp_4 = _coconut_match_args[4] if _coconut.len(_coconut_match_args) > 4 else _coconut_match_kwargs.pop("remove_erroring_algs") if "remove_erroring_algs" in _coconut_match_kwargs else False  #31 (line in Coconut source)
                _coconut_match_set_name__backend_store = _coconut_match_temp_5  #31 (line in Coconut source)
                _coconut_match_set_name_self = _coconut_match_temp_0  #31 (line in Coconut source)
                _coconut_match_set_name_examples = _coconut_match_temp_1  #31 (line in Coconut source)
                _coconut_match_set_name_params = _coconut_match_temp_2  #31 (line in Coconut source)
                _coconut_match_set_name_distribution = _coconut_match_temp_3  #31 (line in Coconut source)
                _coconut_match_set_name_remove_erroring_algs = _coconut_match_temp_4  #31 (line in Coconut source)
                if not _coconut_match_kwargs:  #31 (line in Coconut source)
                    _coconut_match_check_0 = True  #31 (line in Coconut source)
        if _coconut_match_check_0:  #31 (line in Coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #31 (line in Coconut source)
                self = _coconut_match_set_name_self  #31 (line in Coconut source)
            if _coconut_match_set_name_examples is not _coconut_sentinel:  #31 (line in Coconut source)
                examples = _coconut_match_set_name_examples  #31 (line in Coconut source)
            if _coconut_match_set_name_params is not _coconut_sentinel:  #31 (line in Coconut source)
                params = _coconut_match_set_name_params  #31 (line in Coconut source)
            if _coconut_match_set_name_distribution is not _coconut_sentinel:  #31 (line in Coconut source)
                distribution = _coconut_match_set_name_distribution  #31 (line in Coconut source)
            if _coconut_match_set_name_remove_erroring_algs is not _coconut_sentinel:  #31 (line in Coconut source)
                remove_erroring_algs = _coconut_match_set_name_remove_erroring_algs  #31 (line in Coconut source)
            if _coconut_match_set_name__backend_store is not _coconut_sentinel:  #31 (line in Coconut source)
                _backend_store = _coconut_match_set_name__backend_store  #31 (line in Coconut source)
        if not _coconut_match_check_0:  #31 (line in Coconut source)
            raise _coconut_FunctionMatchError('match def attempt_update(self, examples, params, distribution, remove_erroring_algs=False, *, _backend_store):', _coconut_match_args)  #31 (line in Coconut source)

        self.use_distribution(distribution, force=remove_erroring_algs != self.remove_erroring_algs)  #31 (line in Coconut source)

        self.examples = examples  #33 (line in Coconut source)
        self.params = params  #34 (line in Coconut source)
        self.remove_erroring_algs = remove_erroring_algs  #35 (line in Coconut source)
        self.backend_store = _backend_store  #36 (line in Coconut source)

        self.select_new_backend()  #38 (line in Coconut source)
        return True  #39 (line in Coconut source)


    def use_distribution(self, distribution, force=False):  #41 (line in Coconut source)
        """Set the distribution to the given distribution."""  #42 (line in Coconut source)
        distribution = tuple(((alg, weight() if callable(weight) else weight) for alg, weight in distribution))  #43 (line in Coconut source)

        if force or distribution != self.distribution:  #48 (line in Coconut source)
            self.cum_probs = get_cum_probs_for(distribution)  #49 (line in Coconut source)
            self.distribution = distribution  #50 (line in Coconut source)


    def select_new_backend(self):  #52 (line in Coconut source)
        """Randomly select a new backend."""  #53 (line in Coconut source)
# randomly select algorithm
        self.selected_alg = random_from_cum_probs(self.cum_probs)  #55 (line in Coconut source)
        if self.selected_alg is None:  #56 (line in Coconut source)
            raise ValueError("could not select backend from distribution: {_coconut_format_0}".format(_coconut_format_0=(self.distribution)))  #57 (line in Coconut source)

# initialize backend
        self.selected_backend, options = alg_registry[self.selected_alg]  #60 (line in Coconut source)
        try:  #61 (line in Coconut source)
            self.current_backend = get_backend(self.backend_store, self.selected_backend, self.examples, self.params, **options)  #62 (line in Coconut source)
        except constants.erroring_backend_errs:  #69 (line in Coconut source)
            if not self.remove_erroring_algs:  #70 (line in Coconut source)
                raise  #71 (line in Coconut source)
            self.reselect_backend()  #72 (line in Coconut source)


    def reselect_backend(self):  #74 (line in Coconut source)
        """Choose a new backend when the current one errors."""  #75 (line in Coconut source)
        new_distribution = []  #76 (line in Coconut source)
        for alg, weight in self.distribution:  #77 (line in Coconut source)
            if alg != self.selected_alg:  #78 (line in Coconut source)
                new_distribution.append((alg, weight))  #79 (line in Coconut source)
        self.cum_probs = get_cum_probs_for(new_distribution)  #80 (line in Coconut source)
        self.select_new_backend()  #81 (line in Coconut source)


    @override  #83 (line in Coconut source)
    def param(self, name, func, *args, **kwargs):  #84 (line in Coconut source)
        """Defer parameter selection to the selected backend."""  #85 (line in Coconut source)
        try:  #86 (line in Coconut source)
            return self.current_backend.param(name, func, *args, **kwargs)  #87 (line in Coconut source)
        except constants.erroring_backend_errs:  #88 (line in Coconut source)
            if not self.remove_erroring_algs:  #89 (line in Coconut source)
                raise  #90 (line in Coconut source)
            self.reselect_backend()  #91 (line in Coconut source)
        return self.param(name, func, *args, **kwargs)  #92 (line in Coconut source)


    @classmethod  #94 (line in Coconut source)
    def register_safe_alg_for(cls, base_alg, new_alg_name=None, fallback_alg=None):  #95 (line in Coconut source)
        """Register a version of base_alg that defaults to the fallback if base_alg fails."""  #96 (line in Coconut source)
        if new_alg_name is None:  #97 (line in Coconut source)
            new_alg_name = "safe_" + base_alg  #98 (line in Coconut source)
        if fallback_alg is None:  #99 (line in Coconut source)
            fallback_alg = constants.safe_fallback_alg  #100 (line in Coconut source)
        cls.register_alg(new_alg_name, distribution=((base_alg, float("inf")), (fallback_alg, 1)), remove_erroring_algs=True)  #101 (line in Coconut source)


    @classmethod  #110 (line in Coconut source)
    def register_epsilon_exploration_alg_for(cls, base_alg, new_alg_name=None, eps=None):  #111 (line in Coconut source)
        """Register a version of base_alg with epsilon greedy exploration."""  #112 (line in Coconut source)
        if new_alg_name is None:  #113 (line in Coconut source)
            new_alg_name = "epsilon_" + base_alg  #114 (line in Coconut source)
        cls.register_alg(new_alg_name, distribution=((base_alg, lambda _=None: 1 - ((constants.eps_greedy_explore_prob if eps is None else eps))), ("random", lambda _=None: (constants.eps_greedy_explore_prob if eps is None else eps))))  #115 (line in Coconut source)




# Registered names:


_coconut_call_set_names(MixtureBackend)  #130 (line in Coconut source)
MixtureBackend.register()  #130 (line in Coconut source)

MixtureBackend.register_epsilon_exploration_alg_for("max_greedy")  #132 (line in Coconut source)

MixtureBackend.register_safe_alg_for("gaussian_process")  #134 (line in Coconut source)
MixtureBackend.register_safe_alg_for("random_forest")  #135 (line in Coconut source)
MixtureBackend.register_safe_alg_for("extra_trees")  #136 (line in Coconut source)
MixtureBackend.register_safe_alg_for("gradient_boosted_regression_trees")  #137 (line in Coconut source)
