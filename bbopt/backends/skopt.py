#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4c57ffde

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
The scikit-optimize backend. Does black box optimization.
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
from bbopt.util import values_sorted_by_keys
from bbopt.util import split_examples
from bbopt.util import replace_values

# Utilities:

def create_dimension(guess=None, randint=None, uniform=None, choice=None,):
    if (sum)(map(_coconut_forward_compose(_coconut.functools.partial(_coconut.operator.is_, None), _coconut.operator.not_), (randint, uniform, choice))) != 1:
        raise TypeError("the skopt backend requires exactly one of" " randint, uniform, or choice")
    if choice is not None:
        if not isinstance(choice, list):
            raise ValueError("choice must be a list")
        return choice
    if randint is not None:
        if not isinstance(randint, list) or len(randint) != 2:
            raise ValueError("randint must be a list of length 2")
        return (tuple)(map(int, randint))
    if uniform is not None:
        if not isinstance(uniform, list) or len(uniform) != 2:
            raise ValueError("uniform must be a list of length 2")
        return (tuple)(map(float, uniform))

# Backend:

class SkoptBackend(_coconut.object):
    """The scikit-optimize backend uses scikit-optimize for black box optimization."""

    def __init__(self, examples, params, base_estimator=GaussianProcessRegressor, **kwargs):
        dimensions = [create_dimension(**param_kwargs) for param_kwargs in values_sorted_by_keys(params)]
        data_points, objectives, minimizing = split_examples(examples)
        if minimizing:
            optimizer = Optimizer(dimensions, base_estimator, **kwargs)
            optimizer.tell(data_points, objectives)
            current_point = optimizer.ask()
            self.current_values = replace_values(params, current_point)
        elif minimizing is None:
            self.current_values = {}
        else:
            raise ValueError("scikit-optimize only supports minimizing, not maximizing")

    def param(self, name, **kwargs):
        if name in self.current_values:
            return self.current_values[name]
        elif "guess" in kwargs:
            return kwargs["guess"]
        else:
            return RandomBackend().param(**kwargs)
