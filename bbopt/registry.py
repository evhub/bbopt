#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb07efcf3

# Compiled with Coconut version 1.4.0-post_dev23 [Ernest Scribbler]

"""
The backend and algorithm registries.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------




class Registry(_coconut.object):
    """Registry that keeps track of registered objects."""

    def __init__(self, obj_name="obj", defaults=None, generators={}, aliases={}):
        self.obj_name = obj_name
        self.registered = {} if defaults is None else defaults
        self.generators = generators
        self.aliases = aliases

    def __getitem__(self, name):
        name = self.aliases.get(name, name)
        _coconut_match_to = self.registered
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                value = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            return self.registered[name]
        else:
            if name in self.generators:
                return self.run_gen(name)
            else:
                valid_names = ", ".join((repr(name) for name in self))
                raise ValueError("unknown {_coconut_format_0}: {_coconut_format_1} (valid {_coconut_format_2}s: {_coconut_format_3})".format(_coconut_format_0=(obj_name), _coconut_format_1=(name), _coconut_format_2=(obj_name), _coconut_format_3=(valid_names)))

    def register(self, name, value):
        """Register value under the given name."""
        self.registered[name] = value

    def run_gen(self, name):
        """Run the generator for the given name."""
        value = self.generators[name]()
        self.register(name, value)
        del self.generators[name]
        return value

    def __iter__(self):
        _coconut_yield_from = self.registered
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item

        _coconut_yield_from = self.generators
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


    def run_all_gens(self):
        """Run all generators."""
        for name in self.generators:
            self.run_gen(name)

    def items(self):
        """Get all items in the registry as (name, value) pairs."""
        self.run_all_gens()
        _coconut_yield_from = self.registered.items()
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


    def asdict(self):
        """Convert registry to dictionary."""
        self.run_all_gens()
        return self.registered


def _coconut_lambda_0(_=None):
    from bbopt.backends.serving import ServingBackend
    return ServingBackend
def _coconut_lambda_1(_=None):
    from bbopt.backends.random import RandomBackend
    return RandomBackend
def _coconut_lambda_2(_=None):
    from bbopt.backends.skopt import SkoptBackend
    return SkoptBackend
def _coconut_lambda_3(_=None):
    from bbopt.backends.hyperopt import HyperoptBackend
    return HyperoptBackend
def _coconut_lambda_4(_=None):
    from bbopt.backends.mixture import MixtureBackend
    return MixtureBackend
backend_registry = Registry(obj_name="backend", generators={"serving": (_coconut_lambda_0), "random": (_coconut_lambda_1), "scikit-optimize": (_coconut_lambda_2), "hyperopt": (_coconut_lambda_3), "mixture": (_coconut_lambda_4)}, aliases={None: "serving"})


def init_backend(name, examples, params, *args, **options):
    """Create a backend object of the given name with the given data."""
    return backend_registry[name](examples, params, *args, **options)


def _coconut_lambda_5(_=None):
    from hyperopt import anneal
    return ("hyperopt", dict(algo=anneal.suggest))
alg_registry = Registry(obj_name="algorithm", defaults={"serving": ("serving", {}), "random": ("random", {}), "gaussian_process": ("scikit-optimize", {}), "random_forest": ("scikit-optimize", dict(base_estimator="RF")), "extra_trees": ("scikit-optimize", dict(base_estimator="ET")), "gradient_boosted_regression_trees": ("scikit-optimize", dict(base_estimator="GBRT")), "tree_structured_parzen_estimator": ("hyperopt", {})}, generators={"annealing": (_coconut_lambda_5)}, aliases={None: "serving"})
