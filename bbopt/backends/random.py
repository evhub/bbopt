#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x798e4361

# Compiled with Coconut version 1.4.0-post_dev25 [Ernest Scribbler]

"""
The random backend. Does not use existing data, simply spits out random valid values.
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



import random

from bbopt.backends.util import Backend


class RandomBackend(Backend):
    """The random backend chooses parameter values randomly."""
    backend_name = "random"
    random_functions = {"randrange": random.randrange, "choice": random.choice, "uniform": random.uniform, "triangular": random.triangular, "betavariate": random.betavariate, "expovariate": random.expovariate, "gammavariate": random.gammavariate, "normalvariate": random.gauss, "vonmisesvariate": random.vonmisesvariate, "paretovariate": random.paretovariate, "weibullvariate": random.weibullvariate}

    def param(self, name, func, *args, **kwargs):
        if func not in self.random_functions:
            raise ValueError("unknown random function {_coconut_format_0}".format(_coconut_format_0=(name)))
        return self.random_functions[func](*args)


# Registered names:

RandomBackend.register()
RandomBackend.register_alg("random")
