#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xac0fa04f

# Compiled with Coconut version 2.0.0 [How Not to Be Seen]

"""
The bayes-skopt backend. Does black-box optimization with the bask fork of scikit-optimize.
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



from bask import Optimizer  #5 (line in Coconut source)

from bbopt.backends.skopt import SkoptBackend  #7 (line in Coconut source)
from bbopt.backends.skopt import create_dimensions  #7 (line in Coconut source)
from bbopt.backends.skopt import guess_n_initial_points  #7 (line in Coconut source)


# Backend:

class BaskBackend(SkoptBackend):  #16 (line in Coconut source)
    """The bask backend uses bayes-skopt for black box optimization."""  #17 (line in Coconut source)
    backend_name = "bayes-skopt"  #18 (line in Coconut source)

    @override  #20 (line in Coconut source)
    def setup_backend(self, params, n_initial_points=None, **options):  #21 (line in Coconut source)
        """Special method to initialize the backend from params."""  #22 (line in Coconut source)
        self.params = params  #23 (line in Coconut source)
        if n_initial_points is None:  #24 (line in Coconut source)
            n_initial_points = guess_n_initial_points(params)  #25 (line in Coconut source)
        self.optimizer = Optimizer(create_dimensions(params), n_initial_points=n_initial_points, **options)  #26 (line in Coconut source)


# Registered names:


_coconut_call_set_names(BaskBackend)  #35 (line in Coconut source)
BaskBackend.register()  #35 (line in Coconut source)
BaskBackend.register_alias("bask")  #36 (line in Coconut source)
BaskBackend.register_alg("bask_gaussian_process")  #37 (line in Coconut source)
