#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x460673f

# Compiled with Coconut version 1.3.0-post_dev2 [Dead Parrot]

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

from bbgun.util import values_sorted_by_keys
from bbgun.util import split_examples
from bbgun.util import replace_values

# Utilities:

def create_dimension(initial_value=None, bounds=None, prior=None, categories=None,):
    if (sum)(map(_coconut.functools.partial(_coconut.operator.is_, None), (bounds, categories))) != 1:
        raise TypeError("the skopt backend requires exactly one of" " int_in, float_in, or choose_from")
    if prior is not None and bounds is None:
        raise TypeError("prior requires bounds")
    if bounds is not None:
        if not isinstance(bounds, list):
            raise ValueError("bounds must be a list")
        if prior is not None:
            if not isinstance(prior, str):
                raise ValueError("prior must be a string")
            bounds += [prior]
        return tuple(bounds)
    if categories is not None:
        if not isinstance(categories, list):
            raise ValueError("categories must be a list")
        return categories

# Backend:

class SkoptBackend(_coconut.object):
    """The scikit-optimize backend uses scikit-optimize for black box optimization."""

    def __init__(self, examples, params, **kwargs):
        dimensions = [create_dimension(**param_kwargs) for param_kwargs in values_sorted_by_keys(params)]
        data_points, objectives, maximizing = split_examples(examples)
        if maximizing is None:
            self.current_values = {}
        elif not maximizing:
            optimizer = Optimizer(dimensions, **kwargs)
            optimizer.tell(data_points, objectives)
            current_point = optimizer.ask()
            self.current_values = replace_values(params, current_point)
        else:
            raise ValueError("scikit-optimize only supports minimizing, not maximizing")

    def param(self, name, **kwargs):
        if name in self.current_values:
            return self.current_values[name]
        elif "initial_value" in kwargs:
            return kwargs["initial_value"]
        else:
            raise ValueError("missing data for parameter %r and no initial_value given" % name)
