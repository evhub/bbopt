#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x85908

# Compiled with Coconut version 1.5.0-post_dev52 [Fish License]

"""
The mixture backend. Lets you specify a distribution over different possible algorithms.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
_coconut_module_name = _coconut_os_path.splitext(_coconut_os_path.basename(_coconut_file_path))[0]
if not _coconut_module_name or not _coconut_module_name[0].isalpha() or not all (c.isalpha() or c.isdigit() for c in _coconut_module_name):
    raise ImportError("invalid Coconut package name " + repr(_coconut_module_name) + " (pass --standalone to compile as individual files rather than a package)")
_coconut_cached_module = _coconut_sys.modules.get(str(_coconut_module_name + ".__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str(_coconut_module_name + ".__coconut__")]
_coconut_sys.path.insert(0, _coconut_os_path.dirname(_coconut_file_path))
exec("from " + _coconut_module_name + ".__coconut__ import *")
exec("from " + _coconut_module_name + ".__coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable")
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import random

from bbopt import constants
from bbopt.registry import alg_registry
from bbopt.backends.util import Backend
from bbopt.backends.util import init_backend


class MixtureBackend(Backend):
    """Mixture backend. Takes in a distribution over different possible algorithms
    of the form [(algorithm, weight)]. The properties selected_alg and selected_backend
    can be used to retrieve which alg/backend is currently being used."""
    backend_name = "mixture"

    def __init__(self, examples, params, *args, **kwargs):
        self.backend_store = {}
        self.attempt_update(examples, params, *args, **kwargs)

    remove_erroring_algs = None

    @override
    def attempt_update(self, examples, params, distribution, remove_erroring_algs=False):
        """Special method that allows fast updating of the backend."""
        self.use_distribution(distribution, force=remove_erroring_algs != self.remove_erroring_algs)

        self.examples = examples
        self.params = params
        self.remove_erroring_algs = remove_erroring_algs

        self.select_new_backend()
        return True

    def use_distribution(self, distribution, force=False):
        """Set the distribution to the given distribution."""
        if distribution == "epsilon_max_greedy":
            distribution = (("random", constants.eps_greedy_explore_prob), ("max_greedy", 1 - constants.eps_greedy_explore_prob),)
        else:
            distribution = tuple(distribution)

        if force or distribution != self.distribution:
            self.set_cum_probs_for(distribution)
            self.distribution = distribution

    def set_cum_probs_for(self, distribution):
        """Set the cum_probs used to pick the backend according to the given distribution."""
        self.cum_probs = []
        total_weight = sum((weight for alg, weight in distribution))
        prev_cutoff = 0
        for alg, weight in distribution:
            if weight == float("inf"):
                cutoff = 1
            elif weight in (float("-inf"), float("nan")) or total_weight == float("nan"):
                cutoff = prev_cutoff
            else:
                cutoff = prev_cutoff + weight / total_weight
            self.cum_probs.append((alg, cutoff))
            prev_cutoff = cutoff

    def select_new_backend(self):
        """Randomly select a new backend."""
# randomly select algorithm
        rand_val = random.random()
        self.selected_alg = None
        for alg, cutoff in self.cum_probs:
            if rand_val <= cutoff:
                self.selected_alg = alg
                break
        if self.selected_alg is None:
            raise ValueError("could not select backend from distribution: {_coconut_format_0}".format(_coconut_format_0=(self.distribution)))

# initialize backend
        self.selected_backend, options = alg_registry[self.selected_alg]
        try:
            self.current_backend = init_backend(self.selected_backend, self.examples, self.params, attempt_to_update_backend=self.backend_store.get(self.selected_alg), **options)
        except constants.erroring_backend_errs:
            if not self.remove_erroring_algs:
                raise
            self.reselect_backend()
        else:
            self.backend_store[self.selected_alg] = self.current_backend

    def reselect_backend(self):
        """Choose a new backend when the current one errors."""
        new_distribution = []
        for alg, weight in self.distribution:
            if alg != self.selected_alg:
                new_distribution.append((alg, weight))
        self.set_cum_probs_for(new_distribution)
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


# Registered names:

_coconut_call_set_names(MixtureBackend)
MixtureBackend.register()
MixtureBackend.register_alg("epsilon_max_greedy", distribution="epsilon_max_greedy")
MixtureBackend.register_alg("_safe_gaussian_process", distribution=(("gaussian_process", float("inf")), ("annealing", 1),), remove_erroring_algs=True)
