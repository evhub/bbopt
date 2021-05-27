#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x44c267a4

# Compiled with Coconut version 1.5.0-post_dev52 [Fish License]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
_coconut_module_name = _coconut_os_path.splitext(_coconut_os_path.basename(_coconut_file_path))[0]
if not _coconut_module_name or not _coconut_module_name[0].isalpha() or not all (c.isalpha() or c.isdigit() for c in _coconut_module_name):
    raise ImportError("invalid Coconut package name " + repr(_coconut_module_name) + " (pass --standalone to compile as individual files rather than a package)")
_coconut_cached_module = _coconut_sys.modules.get(str(_coconut_module_name + ".__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str(_coconut_module_name + ".__coconut__")]
_coconut_sys.path.insert(0, _coconut_os_path.dirname(_coconut_file_path))
exec("from " + _coconut_module_name + ".__coconut__ import *")
exec("from " + _coconut_module_name + ".__coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable")
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------
