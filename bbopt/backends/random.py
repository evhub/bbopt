#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xaef97623

# Compiled with Coconut version 1.4.0-post_dev7 [Ernest Scribbler]

"""
The random backend. Used for testing purposes.
Does not use existing data, simply spits out random valid values.
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



import random

from bbopt.params import param_processor


class RandomBackend(_coconut.object):
    """The random backend chooses parameter values randomly."""

    def __init__(self, examples=None, params=None):
        pass  # we're choosing randomly, so we ignore everything

    random_functions = {"randrange": random.randrange, "choice": random.choice, "sample": random.sample, "uniform": random.uniform, "triangular": random.triangular, "betavariate": random.betavariate, "expovariate": random.expovariate, "gammavariate": random.gammavariate, "normalvariate": random.gauss, "lognormvariate": random.lognormvariate, "vonmisesvariate": random.vonmisesvariate, "paretovariate": random.paretovariate, "weibullvariate": random.weibullvariate}

    def param(self, name=None, **kwargs):
# remove non-function parameters from kwargs
        kwargs = param_processor.filter_kwargs(kwargs)

# verify kwargs and extract the random command and its arguments
        if len(kwargs) != 1:
            raise TypeError("the random backend requires exactly one parameter," " <name of the random function to call>=<argument(s) to that function>")
        cmd, args = _coconut_igetitem(kwargs.items(), 0)
        if cmd not in self.random_functions:
            raise ValueError("unknown random function {}".format(cmd))

# call the proper random function
        return self.random_functions[cmd](*args)
