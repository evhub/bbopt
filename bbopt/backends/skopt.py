#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd2961294

# Compiled with Coconut version 1.4.0-post_dev7 [Ernest Scribbler]

"""
The scikit-optimize backend. Does black box optimization using scikit-optimize.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



from skopt import Optimizer
from skopt.space import Categorical
from skopt.space import Integer
from skopt.space import Real

from bbopt.backends.random import RandomBackend
from bbopt.params import param_processor
from bbopt.util import sorted_items
from bbopt.util import split_examples
from bbopt.util import make_values
from bbopt.util import serve_values


# Utilities:

@param_processor.only_random_function_kwargs
def create_dimension(name, choice=None, randrange=None, uniform=None,):
    """Create a scikit-optimize dimension for the given param kwargs."""
    if choice is not None:
        return Categorical(*choice)
    if randrange is not None:
        start, stop, step = randrange
        if step != 1:
            raise ValueError("the scikit-optimize backend only supports a randrange step size of 1")
        stop -= 1  # scikit-optimize ranges are inclusive
        return Integer(start, stop)
    if uniform is not None:
        return Real(*uniform)
    raise TypeError("insufficiently specified parameter {}".format(name))


@param_processor.only_random_function_kwargs
def choose_default_placeholder(name, choice=None, randrange=None, uniform=None,):
    """Choose a default placeholder_when_missing value for the given param kwargs."""
    if choice is not None:
        return _coconut_igetitem(choice, 0)
    if randrange is not None:
        start, stop, step = randrange
        return start
    if uniform is not None:
        start, stop = uniform
        return start
    raise TypeError("insufficiently specified parameter {}".format(name))


# Backend:

class SkoptBackend(_coconut.object):
    """The scikit-optimize backend uses scikit-optimize for black box optimization."""
    random_backend = RandomBackend()

    def __init__(self, examples, params, base_estimator="gp", **kwargs):
        if not examples:
            self.current_values = {}
            return

        data_points, losses = split_examples(examples, params, fallback_func=choose_default_placeholder)
        dimensions = [create_dimension(name, **param_kwargs) for name, param_kwargs in sorted_items(params)]

        optimizer = Optimizer(dimensions, base_estimator, **kwargs)
        optimizer.tell(data_points, losses)
        current_point = optimizer.ask()

        self.current_values = make_values(params, current_point)

# decorator to raise an error if kwargs include an unsupported method
    _coconut_decorator_0 = _coconut.functools.partial(param_processor.implements_params, backend_name="scikit-optimize", implemented_params=("choice", "randrange", "uniform",))
    @_coconut_decorator_0
    def param(self, name, **kwargs):
        return serve_values(name, kwargs, serving_values=self.current_values, fallback_func=self.random_backend.param)
