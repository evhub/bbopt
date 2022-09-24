#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfc46137

# Compiled with Coconut version 2.0.0-a_dev63 [How Not to Be Seen]

"""
The serving backend. Selects the best existing data point.
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



from bbopt.util import best_example  #5 (line num in coconut source)
from bbopt.backends.util import Backend  #6 (line num in coconut source)


# Backend:

class ServingBackend(Backend):  #11 (line num in coconut source)
    """The serving backend uses the parameter values from the best example."""  #12 (line num in coconut source)
    backend_name = "serving"  #13 (line num in coconut source)

    @override  #15 (line num in coconut source)
    def attempt_update(self, examples, params, allow_missing_data=False):  #16 (line num in coconut source)
        """Update the serving backend with new parameters."""  #17 (line num in coconut source)
# since we're serving, ignore params and just extract the best example
        self.current_values = best_example(examples)["values"]  #19 (line num in coconut source)

# set new allow_missing_data and call init_fallback_backend if necessary
        self.allow_missing_data = allow_missing_data  #22 (line num in coconut source)
        if not self.fallback_backend and self.allow_missing_data:  #23 (line num in coconut source)
            self.init_fallback_backend()  #24 (line num in coconut source)

        return True  #26 (line num in coconut source)


    @override  #28 (line num in coconut source)
    def fallback_func(self, name, func, *args, **kwargs):  #29 (line num in coconut source)
        if self.allow_missing_data:  #30 (line num in coconut source)
            __class__ = ServingBackend  #31 (line num in coconut source)

            return super().fallback_func(name, func, *args, **kwargs)  #31 (line num in coconut source)
        else:  #32 (line num in coconut source)
            raise ValueError("missing data for parameter {_coconut_format_0} while serving and no guess".format(_coconut_format_0=(name)))  #33 (line num in coconut source)


# Registered names:


_coconut_call_set_names(ServingBackend)  #38 (line num in coconut source)
ServingBackend.register()  #38 (line num in coconut source)

# allow_missing_data=False not included to help bb._backend_store
ServingBackend.register_alg(None)  #41 (line num in coconut source)
ServingBackend.register_alg("serving")  #42 (line num in coconut source)

ServingBackend.register_alg("max_greedy", allow_missing_data=True)  #44 (line num in coconut source)
