#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf5557f4d

# Compiled with Coconut version 2.0.0 [How Not to Be Seen]

"""
The random backend. Does not use existing data, simply spits out random valid values.
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



import random  #5 (line in Coconut source)

from bbopt.backends.util import Backend  #7 (line in Coconut source)


# Backend:

class RandomBackend(Backend):  #12 (line in Coconut source)
    """The random backend chooses parameter values randomly."""  #13 (line in Coconut source)
    backend_name = "random"  #14 (line in Coconut source)
    random_functions = {"randrange": random.randrange, "choice": random.choice, "uniform": random.uniform, "triangular": random.triangular, "betavariate": random.betavariate, "expovariate": random.expovariate, "gammavariate": random.gammavariate, "normalvariate": random.gauss, "vonmisesvariate": random.vonmisesvariate, "paretovariate": random.paretovariate, "weibullvariate": random.weibullvariate}  # gauss is more efficient than normalvariate  #15 (line in Coconut source)

    @override  #29 (line in Coconut source)
    def param(self, name, func, *args, **kwargs):  #30 (line in Coconut source)
        if func not in self.random_functions:  #31 (line in Coconut source)
            raise ValueError("unknown random function {_coconut_format_0}".format(_coconut_format_0=(name)))  #32 (line in Coconut source)
        return self.random_functions[func](*args)  #33 (line in Coconut source)


    @override  #35 (line in Coconut source)
    def attempt_update(self, examples, params):  #36 (line in Coconut source)
        """The random backend requires no modifications to be updated with new parameters."""  #37 (line in Coconut source)
        return True  #38 (line in Coconut source)


# Registered names:


_coconut_call_set_names(RandomBackend)  #43 (line in Coconut source)
RandomBackend.register()  #43 (line in Coconut source)
RandomBackend.register_alg("random")  #44 (line in Coconut source)
