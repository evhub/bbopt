#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xf637112

# Compiled with Coconut version 1.5.0-post_dev57 [Fish License]

"""
The serving backend. Selects the best existing data point.
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



from bbopt.util import best_example
from bbopt.backends.util import Backend


class ServingBackend(Backend):
    """The serving backend uses the parameter values from the best example."""
    backend_name = "serving"

    def __init__(self, *args, **kwargs):
        self.attempt_update(*args, **kwargs)

    @override
    def attempt_update(self, examples, params, allow_missing_data=False):
        """Update the serving backend with new parameters."""
# since we're serving, ignore params and just extract the best example
        self.current_values = best_example(examples)["values"]

# set new allow_missing_data and call init_fallback_backend if necessary
        self.allow_missing_data = allow_missing_data
        if not self.fallback_backend and self.allow_missing_data:
            self.init_fallback_backend()

        return True

    @override
    def fallback_func(self, name, func, *args, **kwargs):
        if self.allow_missing_data:
            return super(ServingBackend, self).fallback_func(name, func, *args, **kwargs)
        else:
            raise ValueError("missing data for parameter {_coconut_format_0} while serving and no guess".format(_coconut_format_0=(name)))

    @classmethod
    def register_none_aliases(cls):
        """Add None aliases as in previous versions of BBopt."""
        cls.register_alias(None)
        cls.register_alg(None)


# Registered names:

_coconut_call_set_names(ServingBackend)
ServingBackend.register()
ServingBackend.register_alg("serving")  # allow_missing_data=False not included to help bb._backend_store
ServingBackend.register_alg("max_greedy", allow_missing_data=True)
