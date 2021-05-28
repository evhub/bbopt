#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfffddada

# Compiled with Coconut version 1.5.0-post_dev57 [Fish License]

"""
Constants for use across all of BBopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
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
                type(_coconut_v).__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)
# Compiled Coconut: -----------------------------------------------------------




# Installation constants:
name = "bbopt"
version = "1.3.0"
description = "The easiest hyperparameter optimization you'll ever do."
long_description = """
See BBopt's GitHub_ for more information.

.. _GitHub: https://github.com/evhub/bbopt
"""
github_url = "https://github.com/evhub/bbopt"
author = "Evan Hubinger"
author_email = "evanjhub@gmail.com"
classifiers = ("Development Status :: 5 - Production/Stable", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent",)
requirements = ("numpy>=1.15.1", "matplotlib>=2.2.5", "scikit-optimize>=0.8.1",)
extra_requirements = {":python_version>='3.7'": ("bask>=0.10.5",), ":python_version>='3'": ("pysot>=0.3.3", "portalocker>=2.2.1", "hyperopt>=0.2.4", "scikit-learn>=0.23.2", "networkx>=2.2", "pymongo>=3.9", "pyspark>=2.4",), ":python_version<'3'": ("futures>=3.3", "scikit-learn>=0.20.4", "portalocker>=1.7.1,<2.0", "hyperopt>=0.1.2,<0.2", "networkx>=1.0,<2.0",), "examples": ("tensorflow>=2.0; python_version>='3'",)}
extra_requirements["dev"] = (extra_requirements["examples"] + ("coconut-develop", "pytest>=3.0",))


# Optimizer constants:
default_alg = "tpe_or_gp"
default_meta_alg = "epsilon_max_greedy"

default_protocol = 2
lock_timeout = 6
meta_opt_alg_var = "_run_meta_alg"
data_file_ext = ".bbopt"

use_generic_categories_for_categorical_data = False
use_placeholder_when_outside_support = False


# CLI constants:
default_trials = 100
default_jobs = 4


# Backend constants:
default_fallback_backend = "random"
erroring_backend_errs = (ValueError, TypeError)
eps_greedy_explore_prob = 0.2
