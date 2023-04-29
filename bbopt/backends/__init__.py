#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xcd3ed2eb

# Compiled with Coconut version 3.0.0-a_dev36

"""
Backends contains all of bbopt's different backends.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
_coconut_header_info = ('3.0.0-a_dev36', '', True)
import os as _coconut_os
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in
if _coconut_pop_path:
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



sys = _coconut_sys  #5 (line in Coconut source)
import traceback  #6 (line in Coconut source)

from bbopt.util import printerr  #8 (line in Coconut source)

# import all the backends to register them
from bbopt.backends.serving import ServingBackend  # NOQA  #11 (line in Coconut source)
from bbopt.backends.random import RandomBackend  # NOQA  # NOQA  #12 (line in Coconut source)
from bbopt.backends.mixture import MixtureBackend  # NOQA  #13 (line in Coconut source)
from bbopt.backends.bandit import BanditBackend  # NOQA  #14 (line in Coconut source)
try:  #15 (line in Coconut source)
    from bbopt.backends.skopt import SkoptBackend  # NOQA  #16 (line in Coconut source)
except ImportError:  #17 (line in Coconut source)
    traceback.print_exc()  #18 (line in Coconut source)
    printerr("Could not import scikit-optimize backend; backend unavailable (see above error).")  #19 (line in Coconut source)
try:  #20 (line in Coconut source)
    from bbopt.backends.hyperopt import HyperoptBackend  # NOQA  #21 (line in Coconut source)
except ImportError:  #22 (line in Coconut source)
    traceback.print_exc()  #23 (line in Coconut source)
    printerr("Could not import hyperopt backend; backend unavailable (see above error).")  #24 (line in Coconut source)
if sys.version_info >= (3,):  #25 (line in Coconut source)
    try:  #26 (line in Coconut source)
        from bbopt.backends.pysot import PySOTBackend  # NOQA  #27 (line in Coconut source)
    except ImportError:  #28 (line in Coconut source)
        traceback.print_exc()  #29 (line in Coconut source)
        printerr("Could not import pySOT backend; backend unavailable (see above error).")  #30 (line in Coconut source)
if sys.version_info >= (3, 7):  #31 (line in Coconut source)
    try:  #32 (line in Coconut source)
        from bbopt.backends.bask import BaskBackend  # NOQA  #33 (line in Coconut source)
    except ImportError:  #34 (line in Coconut source)
        traceback.print_exc()  #35 (line in Coconut source)
        printerr("Could not import bayes-skopt backend; backend unavailable (see above error).")  #36 (line in Coconut source)
if sys.version_info >= (3,):  #37 (line in Coconut source)
    try:  #38 (line in Coconut source)
        from bbopt.backends.openai import OpenAIBackend  # NOQA  #39 (line in Coconut source)
    except ImportError:  #40 (line in Coconut source)
        traceback.print_exc()  #41 (line in Coconut source)
        printerr("Could not import openai backend; backend unavailable (see above error).")  #42 (line in Coconut source)

# meta alg mixtures don't care what backend we register them on,
#  so we just register them here
ServingBackend.register_meta("tpe_or_gp", ("tree_structured_parzen_estimator", "safe_gaussian_process"))  #46 (line in Coconut source)
ServingBackend.register_meta("any_fast", ("tree_structured_parzen_estimator", "safe_random_forest", "safe_extra_trees", "safe_gradient_boosted_regression_trees"))  #50 (line in Coconut source)
