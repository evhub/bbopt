#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x63f8dd5b

# Compiled with Coconut version 1.5.0-post_dev7 [Fish License]

"""
Constants for use across all of BBopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------




# Installation constants:
name = "bbopt"
version = "1.1.15"
description = "The easiest hyperparameter optimization you'll ever do."
long_description = """
See BBopt's GitHub_ for more information.

.. _GitHub: https://github.com/evhub/bbopt
"""
github_url = "https://github.com/evhub/bbopt"
author = "Evan Hubinger"
author_email = "evanjhub@gmail.com"
classifiers = ("Development Status :: 5 - Production/Stable", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent",)
requirements = ("numpy>=1.15.1", "matplotlib>=2.2.5", "scikit-optimize>=0.7.4", "pysot>=0.3.3",)
extra_requirements = {":python_version<'3'": ("futures>=3.3", "scikit-learn>=0.20.4", "portalocker>=1.7.1,<2.0", "hyperopt>=0.1.2,<0.2", "networkx>=1.0,<2.0",), ":python_version>='3'": ("hyperopt>=0.2.4", "scikit-learn>=0.22.2", "portalocker>=1.7.1", "networkx>=2.2", "pymongo>=3.9", "pyspark>=2.4",), "examples": ("keras",)}
extra_requirements["dev"] = (extra_requirements["examples"] + ("coconut-develop", "pytest>=3.0",))


# Optimizer constants:
data_file_ext = ".bbopt"
lock_timeout = 6
default_alg = "tree_structured_parzen_estimator"
default_protocol = 2
use_randrange_for_categorical_data = False
use_generic_categories_for_categorical_data = False
use_placeholder_when_outside_support = False


# CLI constants:
default_trials = 100
default_jobs = 1
