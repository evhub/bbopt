#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc6f7be89

# Compiled with Coconut version 1.4.0-post_dev25 [Ernest Scribbler]

"""
The scikit-optimize backend. Does black box optimization using scikit-optimize.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel, _coconut_assert
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



from skopt import Optimizer
from skopt.space import Categorical
from skopt.space import Integer
from skopt.space import Real

from bbopt.util import sorted_items
from bbopt.backends.util import Backend
from bbopt.backends.util import split_examples
from bbopt.backends.util import make_values


# Utilities:

def create_space(name, func, *args):
    """Create a scikit-optimize space for the given parameter."""
    name = py_str(name)
    _coconut_match_to = func
    _coconut_case_check_0 = False
    if _coconut_match_to == "choice":
        _coconut_case_check_0 = True
    if _coconut_case_check_0:
        return Categorical(*args, name=name)
    if not _coconut_case_check_0:
        if _coconut_match_to == "randrange":
            _coconut_case_check_0 = True
        if _coconut_case_check_0:
            start, stop, step = args
            if step != 1:
                raise ValueError("the scikit-optimize backend only supports a randrange step size of 1")
            stop -= 1  # scikit-optimize ranges are inclusive
            return Integer(start, stop, name=name)
    if not _coconut_case_check_0:
        if _coconut_match_to == "uniform":
            _coconut_case_check_0 = True
        if _coconut_case_check_0:
            return Real(*args, name=name)
    raise TypeError("insufficiently specified parameter {_coconut_format_0}".format(_coconut_format_0=(name)))


def create_dimensions(params):
    """Construct the full optimization space for the given parameters."""
    return [create_space(name, func, *args) for name, (func, args, kwargs) in sorted_items(params)]


# Backend:

class SkoptBackend(Backend):
    """The scikit-optimize backend uses scikit-optimize for black box optimization."""
    backend_name = "scikit-optimize"
    implemented_funcs = ("choice", "randrange", "uniform",)

    def __init__(self, examples, params, base_estimator="GP", **options):
        self.init_fallback_backend()

        if not examples:
            self.current_values = {}
            return

        data_points, losses = split_examples(examples, params)
        dimensions = create_dimensions(params)

        if isinstance(base_estimator, str):
            base_estimator = py_str(base_estimator)

        self.optimizer = Optimizer(dimensions, base_estimator, **options)
        self.result = self.optimizer.tell(data_points, losses)
        current_point = self.optimizer.ask()

        self.current_values = make_values(params, current_point)

    @property
    def space(self):
        """The space over which optimization was performed."""
        return self.optimizer.space

    @property
    def model(self):
        """Get the most recently fit model."""
        return self.optimizer.models[-1]


# Registered names:

SkoptBackend.register()
SkoptBackend.register_alias("skopt")
SkoptBackend.register_alg("gaussian_process", base_estimator="GP")
SkoptBackend.register_alg("random_forest", base_estimator="RF")
SkoptBackend.register_alg("extra_trees", base_estimator="ET")
SkoptBackend.register_alg("gradient_boosted_regression_trees", base_estimator="GBRT")
