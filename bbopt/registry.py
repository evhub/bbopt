#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa7a23948

# Compiled with Coconut version 1.4.0-post_dev25 [Ernest Scribbler]

"""
The backend and algorithm registries.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel, _coconut_assert
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------




class Registry(_coconut.object):
    """Registry that keeps track of registered objects."""

    def __init__(self, obj_name, defaults=None, generators=None, aliases=None):
        self.obj_name = obj_name
        self.registered = ({} if defaults is None else defaults)
        self.generators = ({} if generators is None else generators)
        self.aliases = ({} if aliases is None else aliases)

    def __getitem__(self, name):
        name = self.aliases.get(name, name)
        _coconut_match_to = self.registered
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                value = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            return self.registered[name]
        else:
            if name in self.generators:
                return self.run_gen(name)
            else:
                valid_names = ", ".join((repr(name) for name in self))
                raise ValueError("unknown {_coconut_format_0}: {_coconut_format_1} (valid {_coconut_format_2}s: {_coconut_format_3})".format(_coconut_format_0=(self.obj_name), _coconut_format_1=(name), _coconut_format_2=(self.obj_name), _coconut_format_3=(valid_names)))

    def register(self, name, value):
        """Register value under the given name."""
        self.registered[name] = value

    def register_alias(self, name, alias):
        """Register an alias for the given name."""
        self.aliases[alias] = name

    def run_gen(self, name):
        """Run the generator for the given name."""
        value = self.generators[name]()
        if value is not None:
            self.register(name, value)
        del self.generators[name]
        return self.registered[name]

    def __iter__(self):
        _coconut_yield_from = self.registered
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item

        _coconut_yield_from = self.generators
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item

        _coconut_yield_from = self.aliases
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


    def run_all_gens(self):
        """Run all generators."""
        for name in self.generators:
            self.run_gen(name)

    def items(self):
        """Get all items in the registry as (name, value) pairs."""
        self.run_all_gens()
        _coconut_yield_from = self.registered.items()
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


    def asdict(self):
        """Convert registry to dictionary."""
        self.run_all_gens()
        return self.registered


backend_registry = Registry("backend")


def init_backend(name, examples, params, *args, **options):
    """Create a backend object of the given name with the given data."""
    return backend_registry[name](examples, params, *args, **options)


alg_registry = Registry("algorithm")
