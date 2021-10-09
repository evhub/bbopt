#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4b97aa84

# Compiled with Coconut version 1.5.0-post_dev91 [Fish License]

"""
Backends contains all of bbopt's different backends.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == str("__coconut__"):
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



sys = _coconut_sys
import traceback

# import all the other backends to register them
from bbopt.backends.serving import ServingBackend
from bbopt.backends.random import RandomBackend
from bbopt.backends.mixture import MixtureBackend
from bbopt.backends.bandit import BanditBackend
try:
    from bbopt.backends.skopt import SkoptBackend
except ImportError:
    traceback.print_exc()
    print("Could not import scikit-optimize backend; backend unavailable (see above error).")
try:
    from bbopt.backends.hyperopt import HyperoptBackend
except ImportError:
    traceback.print_exc()
    print("Could not import hyperopt backend; backend unavailable (see above error).")
if sys.version_info >= (3,):
    try:
        from bbopt.backends.pysot import PySOTBackend
    except ImportError:
        traceback.print_exc()
        print("Could not import pySOT backend; backend unavailable (see above error).")
if sys.version_info >= (3, 7):
    try:
        from bbopt.backends.bask import BaskBackend
    except ImportError:
        traceback.print_exc()
        print("Could not import bayes-skopt backend; backend unavailable (see above error).")
