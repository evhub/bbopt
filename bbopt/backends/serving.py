#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x21c1e1e6

# Compiled with Coconut version 3.0.0-a_dev36

"""
The serving backend. Selects the best existing data point.
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



from bbopt.util import best_example  #5 (line in Coconut source)
from bbopt.backends.util import Backend  #6 (line in Coconut source)


# Backend:

class ServingBackend(Backend):  #11 (line in Coconut source)
    """The serving backend uses the parameter values from the best example."""  #12 (line in Coconut source)
    backend_name = "serving"  #13 (line in Coconut source)

    @override  #15 (line in Coconut source)
    def attempt_update(self, examples, params, allow_missing_data=False):  #16 (line in Coconut source)
        """Update the serving backend with new parameters."""  #17 (line in Coconut source)
# since we're serving, ignore params and just extract the best example
        self.current_values = best_example(examples)["values"]  #19 (line in Coconut source)

# set new allow_missing_data and call init_fallback_backend if necessary
        self.allow_missing_data = allow_missing_data  #22 (line in Coconut source)
        if not self.fallback_backend and self.allow_missing_data:  #23 (line in Coconut source)
            self.init_fallback_backend()  #24 (line in Coconut source)

        return True  #26 (line in Coconut source)


    @override  #28 (line in Coconut source)
    def fallback_func(self, name, func, *args, **kwargs):  #29 (line in Coconut source)
        if self.allow_missing_data:  #30 (line in Coconut source)
            __class__ = ServingBackend  #31 (line in Coconut source)

            return super().fallback_func(name, func, *args, **kwargs)  #31 (line in Coconut source)
        else:  #32 (line in Coconut source)
            raise ValueError("missing data for parameter {_coconut_format_0} while serving and no guess".format(_coconut_format_0=(name)))  #33 (line in Coconut source)


# Registered names:


_coconut_call_set_names(ServingBackend)  #38 (line in Coconut source)
ServingBackend.register()  #38 (line in Coconut source)

# allow_missing_data=False not included to help bb._backend_store
ServingBackend.register_alg(None)  #41 (line in Coconut source)
ServingBackend.register_alg("serving")  #42 (line in Coconut source)

ServingBackend.register_alg("max_greedy", allow_missing_data=True)  #44 (line in Coconut source)
