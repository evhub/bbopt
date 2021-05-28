#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb2afaae

# Compiled with Coconut version 1.5.0-post_dev57 [Fish License]

"""
The bayes-skopt backend. Does black-box optimization with the bask fork of scikit-optimize.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
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
                _coconut_vtype = type(_coconut_v)
                _coconut_vtype.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)
# Compiled Coconut: -----------------------------------------------------------



from bask import Optimizer

from bbopt.backends.skopt import SkoptBackend
from bbopt.backends.skopt import create_dimensions
from bbopt.backends.skopt import guess_n_initial_points


# Backend:

class BaskBackend(SkoptBackend):
    """The bask backend uses bayes-skopt for black box optimization."""
    backend_name = "bayes-skopt"

    @override
    def setup_backend(self, params, n_initial_points=None, **options):
        """Special method to initialize the backend from params."""
        self.params = params
        if n_initial_points is None:
            n_initial_points = guess_n_initial_points(params)
        self.optimizer = Optimizer(create_dimensions(params), n_initial_points=n_initial_points, **options)


# Registered names:

_coconut_call_set_names(BaskBackend)
BaskBackend.register()
BaskBackend.register_alias("bask")
BaskBackend.register_alg("bask_gaussian_process")
