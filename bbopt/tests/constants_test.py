#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa69b8e27

# Compiled with Coconut version 2.0.0-a_dev65 [How Not to Be Seen]

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

import unittest  #1 (line num in coconut source)

from bbopt import constants  #3 (line num in coconut source)


# Utilities:

def is_hashable(obj):  #8 (line num in coconut source)
    """Determine if obj is hashable."""  #9 (line num in coconut source)
    try:  #10 (line num in coconut source)
        hash(obj)  #11 (line num in coconut source)
    except Exception:  #12 (line num in coconut source)
        return False  #13 (line num in coconut source)
    else:  #14 (line num in coconut source)
        return True  #15 (line num in coconut source)



def assert_dict_or_callable_or_hashable(name, obj):  #18 (line num in coconut source)
    """Assert obj is hashable, or for dicts apply recursively to values."""  #19 (line num in coconut source)
    if isinstance(obj, dict):  #20 (line num in coconut source)
        for val in obj.values():  #21 (line num in coconut source)
            assert_dict_or_callable_or_hashable(name, val)  #22 (line num in coconut source)
    elif not callable(obj):  #23 (line num in coconut source)
        assert is_hashable(obj), "Constant " + name + " contains unhashable values"  #24 (line num in coconut source)


# Tests:


class TestConstants(unittest.TestCase):  #29 (line num in coconut source)

    def test_immutable(self):  #31 (line num in coconut source)
        for name, value in vars(constants).items():  #32 (line num in coconut source)
            if not name.startswith("__"):  #33 (line num in coconut source)
                assert not isinstance(value, list), "Constant " + name + " should be tuple, not list"  #34 (line num in coconut source)
                assert not isinstance(value, set), "Constant " + name + " should be frozenset, not set"  #35 (line num in coconut source)
                if "sentinel" not in name.lower():  #36 (line num in coconut source)
                    assert_dict_or_callable_or_hashable(name, value)  #37 (line num in coconut source)


_coconut_call_set_names(TestConstants)  #38 (line num in coconut source)
