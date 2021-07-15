#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc492fd24

# Compiled with Coconut version 1.5.0-post_dev75 [Fish License]

"""
The mixture backend. Lets you specify a distribution over different possible algorithms.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
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
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



from bbopt import constants
from bbopt.util import convert_match_errors
from bbopt.registry import alg_registry
from bbopt.backends.util import Backend
from bbopt.backends.util import get_backend
from bbopt.backends.util import get_cum_probs_for
from bbopt.backends.util import random_from_cum_probs


# Backend:

class MixtureBackend(Backend):
    """Mixture backend. Takes in a distribution over different possible algorithms
    of the form [(algorithm, weight)]. The properties selected_alg and selected_backend
    can be used to retrieve which alg/backend is currently being used."""

    backend_name = "mixture"
    request_backend_store = True
    remove_erroring_algs = None

    @override
    @convert_match_errors
    @_coconut_mark_as_match
    def attempt_update(*_coconut_match_args, **_coconut_match_kwargs):
        """Special method that allows fast updating of the backend."""
        _coconut_match_check_0 = False
        _coconut_FunctionMatchError = _coconut_get_function_match_error()
        if (_coconut.len(_coconut_match_args) <= 5) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "params" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "distribution" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 4, "remove_erroring_algs" in _coconut_match_kwargs)) <= 1):
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("examples")
            _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("params")
            _coconut_match_temp_3 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("distribution")
            _coconut_match_temp_4 = _coconut_match_args[4] if _coconut.len(_coconut_match_args) > 4 else _coconut_match_kwargs.pop("remove_erroring_algs") if "remove_erroring_algs" in _coconut_match_kwargs else False
            _coconut_match_temp_5 = _coconut_match_kwargs.pop("_backend_store") if "_backend_store" in _coconut_match_kwargs else _coconut_sentinel
            if (_coconut_match_temp_5 is not _coconut_sentinel) and (not _coconut_match_kwargs):
                self = _coconut_match_temp_0
                examples = _coconut_match_temp_1
                params = _coconut_match_temp_2
                distribution = _coconut_match_temp_3
                remove_erroring_algs = _coconut_match_temp_4
                _backend_store = _coconut_match_temp_5
                _coconut_match_check_0 = True
        if not _coconut_match_check_0:
            raise _coconut_FunctionMatchError('match def attempt_update(self, examples, params, distribution, remove_erroring_algs=False, *, _backend_store):', _coconut_match_args)

        self.use_distribution(distribution, force=remove_erroring_algs != self.remove_erroring_algs)

        self.examples = examples
        self.params = params
        self.remove_erroring_algs = remove_erroring_algs
        self.backend_store = _backend_store

        self.select_new_backend()
        return True

    def use_distribution(self, distribution, force=False):
        """Set the distribution to the given distribution."""
        if distribution == "epsilon_max_greedy":
            distribution = (("random", constants.eps_greedy_explore_prob), ("max_greedy", 1 - constants.eps_greedy_explore_prob),)
        else:
            distribution = tuple(distribution)

        if force or distribution != self.distribution:
            self.cum_probs = get_cum_probs_for(distribution)
            self.distribution = distribution

    def select_new_backend(self):
        """Randomly select a new backend."""
# randomly select algorithm
        self.selected_alg = random_from_cum_probs(self.cum_probs)
        if self.selected_alg is None:
            raise ValueError("could not select backend from distribution: {_coconut_format_0}".format(_coconut_format_0=(self.distribution)))

# initialize backend
        self.selected_backend, options = alg_registry[self.selected_alg]
        try:
            self.current_backend = get_backend(self.backend_store, self.selected_backend, self.examples, self.params, **options)
        except constants.erroring_backend_errs:
            if not self.remove_erroring_algs:
                raise
            self.reselect_backend()

    def reselect_backend(self):
        """Choose a new backend when the current one errors."""
        new_distribution = []
        for alg, weight in self.distribution:
            if alg != self.selected_alg:
                new_distribution.append((alg, weight))
        self.cum_probs = get_cum_probs_for(new_distribution)
        self.select_new_backend()

    @override
    def param(self, name, func, *args, **kwargs):
        """Defer parameter selection to the selected backend."""
        try:
            return self.current_backend.param(name, func, *args, **kwargs)
        except constants.erroring_backend_errs:
            if not self.remove_erroring_algs:
                raise
            self.reselect_backend()
        return self.param(name, func, *args, **kwargs)

    @classmethod
    def register_safe_alg_for(cls, base_alg, new_alg_name=None, fallback_alg=None):
        """Register a version of base_alg that defaults to the fallback if base_alg fails."""
        if new_alg_name is None:
            new_alg_name = "safe_" + base_alg
        if fallback_alg is None:
            fallback_alg = constants.safe_fallback_alg
        cls.register_alg(new_alg_name, distribution=((base_alg, float("inf")), (fallback_alg, 1),), remove_erroring_algs=True)


# Registered names:

_coconut_call_set_names(MixtureBackend)
MixtureBackend.register()
MixtureBackend.register_alg("epsilon_max_greedy", distribution="epsilon_max_greedy")

MixtureBackend.register_safe_alg_for("gaussian_process")
MixtureBackend.register_safe_alg_for("random_forest")
MixtureBackend.register_safe_alg_for("extra_trees")
MixtureBackend.register_safe_alg_for("gradient_boosted_regression_trees")

# we register meta alg mixtures here
MixtureBackend.register_meta("tpe_or_gp", ("tree_structured_parzen_estimator", "safe_gaussian_process",))
MixtureBackend.register_meta("any_fast", ("tree_structured_parzen_estimator", "safe_random_forest", "safe_extra_trees", "safe_gradient_boosted_regression_trees",))
