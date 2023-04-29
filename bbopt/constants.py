#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4461831f

# Compiled with Coconut version 3.0.0-a_dev36

"""
Constants for use across all of BBopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
_coconut_header_info = ('3.0.0-a_dev36', '', True)
import os as _coconut_os
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
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




# Installation constants:
name = "bbopt"  #7 (line in Coconut source)
version = "1.4.2"  #8 (line in Coconut source)
description = "The easiest hyperparameter optimization you'll ever do."  #9 (line in Coconut source)
long_description = """
See BBopt's GitHub_ for more information.

.. _GitHub: https://github.com/evhub/bbopt
"""  #14 (line in Coconut source)
github_url = "https://github.com/evhub/bbopt"  #15 (line in Coconut source)
author = "Evan Hubinger"  #16 (line in Coconut source)
author_email = "evanjhub@gmail.com"  #17 (line in Coconut source)
classifiers = ("Development Status :: 5 - Production/Stable", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent")  #18 (line in Coconut source)
requirements = ("numpy>=1.15.1", "matplotlib>=2.2.5")  #24 (line in Coconut source)
extra_requirements = _coconut.dict(((":python_version>='3.7'", ("bask>=0.10.6",)), (":python_version>='3'", ("pysot>=0.3.3", "portalocker>=2.2.1", "hyperopt>=0.2.5", "scikit-optimize>=0.8.1", "openai>=0.6.4", "scikit-learn>=0.23.2", "networkx>=2.2", "pymongo>=3.9", "pyspark>=2.4")), (":python_version<'3'", ("futures>=3.3", "scikit-learn>=0.20.4", "scikit-optimize>=0.8.1,<0.9", "portalocker>=1.7.1,<2.0", "hyperopt>=0.1.2,<0.2", "networkx>=1.0,<2.0")), ("examples", ("tensorflow>=2.0; python_version>='3'",))))  #28 (line in Coconut source)
extra_requirements["dev"] = (extra_requirements["examples"] + ("coconut-develop", "pytest>=3.0"))  #62 (line in Coconut source)


# Optimizer constants:
default_alg = "any_fast"  #72 (line in Coconut source)
default_meta_alg = "boltzmann_gumbel_exploration"  #73 (line in Coconut source)

default_protocol = 2  #75 (line in Coconut source)
lock_timeout = 6  #76 (line in Coconut source)
meta_opt_alg_var = "_run_meta_alg"  #77 (line in Coconut source)
data_file_ext = ".bbopt"  #78 (line in Coconut source)

use_generic_categories_for_categorical_data = False  #80 (line in Coconut source)
use_placeholder_when_outside_support = False  #81 (line in Coconut source)

default_alg_sentinel = object()  #83 (line in Coconut source)


# CLI constants:
default_trials = 100  #87 (line in Coconut source)
default_jobs = 4  #88 (line in Coconut source)

run_id_env_var = "BBOPT_RUN_ID"  #90 (line in Coconut source)


# Backend constants:
default_fallback_backend = "random"  #94 (line in Coconut source)
erroring_backend_errs = (ValueError, TypeError)  #95 (line in Coconut source)

eps_greedy_explore_prob = 0.2  #97 (line in Coconut source)
safe_fallback_alg = "tree_structured_parzen_estimator"  #98 (line in Coconut source)


# OpenAI constants:
openai_default_engine = "text-curie-001"  #102 (line in Coconut source)
openai_davinci_engine = "text-davinci-002"  #103 (line in Coconut source)

openai_default_temp = 1  #105 (line in Coconut source)
openai_max_temp = 2  #106 (line in Coconut source)

openai_default_max_retries = 10  #108 (line in Coconut source)

openai_max_context_err_prefix = "This model's maximum context length is "  #110 (line in Coconut source)
