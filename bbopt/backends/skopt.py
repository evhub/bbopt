#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfe4a4a3c

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
The scikit-optimize backend. Does black box optimization using scikit-optimize.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



# Imports:

from skopt import Optimizer
from skopt.learning import GaussianProcessRegressor

from bbopt.backends.random import RandomBackend
from bbopt.params import param_processor
from bbopt.util import sorted_items
from bbopt.util import split_examples
from bbopt.util import replace_values
from bbopt.util import negate_objective

# Utilities:

def create_dimension(name, choice=None, randrange=None, uniform=None,):
    """Create a scikit-optimize dimension for the given param kwargs."""
    if choice is not None:
        return choice  # lists are interpreted as choices
    if randrange is not None:
        start, stop, step = randrange
        if step != 1:
            raise ValueError("the scikit-optimize backend only supports a randrange step size of 1")
        stop -= 1  # scikit-optimize ranges are inclusive
        return (start, stop)  # int tuples are interpreted as int ranges
    if uniform is not None:
        return (tuple)(map(float, uniform))  # float tuples are interpreted as float ranges
    raise TypeError("insufficiently specified parameter %r" % name)

# Backend:

class SkoptBackend(_coconut.object):
    """The scikit-optimize backend uses scikit-optimize for black box optimization."""

    def __init__(self, examples, params, default_placeholder=None, base_estimator=GaussianProcessRegressor, **kwargs):
        if not examples:
            self.current_values = {}
            return
        data_points, losses = split_examples(examples, params, default_placeholder)
        dimensions = [create_dimension(name, **param_processor.filter_kwargs(param_kwargs)) for name, param_kwargs in sorted_items(params)]
        optimizer = Optimizer(dimensions, base_estimator, **kwargs)
        optimizer.tell(data_points, losses)
        current_point = optimizer.ask()
        self.current_values = replace_values(params, current_point)

    def param(self, name, **kwargs):
        _coconut_match_check = False
        _coconut_match_to = self.current_values
        _coconut_sentinel = _coconut.object()
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                value = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            return value
        else:
            if "guess" in kwargs:
                return kwargs["guess"]
            else:
                return RandomBackend().param(**kwargs)
