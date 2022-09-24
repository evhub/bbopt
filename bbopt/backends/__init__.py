#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf583057e

# Compiled with Coconut version 2.0.0-a_dev65 [How Not to Be Seen]

"""
Backends contains all of bbopt's different backends.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:  # type: ignore
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
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



sys = _coconut_sys  #5 (line num in coconut source)
import traceback  #6 (line num in coconut source)

from bbopt.util import printerr  #8 (line num in coconut source)

# import all the backends to register them
from bbopt.backends.serving import ServingBackend  #11 (line num in coconut source)
from bbopt.backends.random import RandomBackend  #12 (line num in coconut source)
from bbopt.backends.mixture import MixtureBackend  #13 (line num in coconut source)
from bbopt.backends.bandit import BanditBackend  #14 (line num in coconut source)
try:  #15 (line num in coconut source)
    from bbopt.backends.skopt import SkoptBackend  #16 (line num in coconut source)
except ImportError:  #17 (line num in coconut source)
    traceback.print_exc()  #18 (line num in coconut source)
    printerr("Could not import scikit-optimize backend; backend unavailable (see above error).")  #19 (line num in coconut source)
try:  #20 (line num in coconut source)
    from bbopt.backends.hyperopt import HyperoptBackend  #21 (line num in coconut source)
except ImportError:  #22 (line num in coconut source)
    traceback.print_exc()  #23 (line num in coconut source)
    printerr("Could not import hyperopt backend; backend unavailable (see above error).")  #24 (line num in coconut source)
if sys.version_info >= (3,):  #25 (line num in coconut source)
    try:  #26 (line num in coconut source)
        from bbopt.backends.pysot import PySOTBackend  #27 (line num in coconut source)
    except ImportError:  #28 (line num in coconut source)
        traceback.print_exc()  #29 (line num in coconut source)
        printerr("Could not import pySOT backend; backend unavailable (see above error).")  #30 (line num in coconut source)
if sys.version_info >= (3, 7):  #31 (line num in coconut source)
    try:  #32 (line num in coconut source)
        from bbopt.backends.bask import BaskBackend  #33 (line num in coconut source)
    except ImportError:  #34 (line num in coconut source)
        traceback.print_exc()  #35 (line num in coconut source)
        printerr("Could not import bayes-skopt backend; backend unavailable (see above error).")  #36 (line num in coconut source)
if sys.version_info >= (3,):  #37 (line num in coconut source)
    try:  #38 (line num in coconut source)
        from bbopt.backends.openai import OpenAIBackend  #39 (line num in coconut source)
    except ImportError:  #40 (line num in coconut source)
        traceback.print_exc()  #41 (line num in coconut source)
        printerr("Could not import openai backend; backend unavailable (see above error).")  #42 (line num in coconut source)

# meta alg mixtures don't care what backend we register them on,
#  so we just register them here
ServingBackend.register_meta("tpe_or_gp", ("tree_structured_parzen_estimator", "safe_gaussian_process"))  #46 (line num in coconut source)
ServingBackend.register_meta("any_fast", ("tree_structured_parzen_estimator", "safe_random_forest", "safe_extra_trees", "safe_gradient_boosted_regression_trees"))  #50 (line num in coconut source)
