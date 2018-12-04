#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2bcf7674

# Compiled with Coconut version 1.4.0-post_dev3 [Ernest Scribbler]

"""
The serving backend. Selects the best existing data point.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



from bbopt.util import best_example
from bbopt.util import serve_values


class ServingBackend(_coconut.object):
    """The serving backend uses the parameter values from the best example."""

    def __init__(self, examples, params):  # ignore params since we're serving
        self.serving_values = best_example(examples)["values"]

    def param(self, name, **kwargs):
        def _coconut_lambda_0(name, **kwargs):
            raise ValueError("missing data for parameter {} while serving and no guess".format(name))
        return serve_values(*(name, kwargs), serving_values=self.serving_values, fallback_func=(_coconut_lambda_0))
