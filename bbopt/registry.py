#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4c6c5f85

# Compiled with Coconut version 1.5.0-post_dev57 [Fish License]

"""
The backend and algorithm registries.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
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



# Registry class:

class Registry(_coconut.object):
    """Registry that keeps track of registered objects."""

    def __init__(self, obj_name, defaults=None, generators=None, aliases=None):
        self.obj_name = obj_name
        self.registered = ({} if defaults is None else defaults)
        self.generators = ({} if generators is None else generators)
        self.aliases = ({} if aliases is None else aliases)
        self.no_conflict_registries = []

    def shouldnt_conflict_with(self, registry):
        """Add the given registry to the no conflict registries."""
        self.no_conflict_registries.append(registry)

    def __getitem__(self, name):
        name = self.aliases.get(name, name)
        _coconut_match_to_0 = self.registered
        _coconut_match_check_0 = False
        if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to_0.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                value = _coconut_match_temp_0
                _coconut_match_check_0 = True
        if _coconut_match_check_0:
            return value
        else:
            if name in self.generators:
                return self.run_gen(name)
            else:
                for registry in self.no_conflict_registries:
                    if name in registry:
                        raise ValueError("invalid {_coconut_format_0}: {_coconut_format_1} ({_coconut_format_2} is a(n) {_coconut_format_3} not a(n) {_coconut_format_4})".format(_coconut_format_0=(self.obj_name), _coconut_format_1=(name), _coconut_format_2=(name), _coconut_format_3=(registry.obj_name), _coconut_format_4=(self.obj_name)))
                valid_names = ", ".join((repr(name) for name in self))
                raise ValueError("unknown {_coconut_format_0}: {_coconut_format_1} (valid {_coconut_format_2}s: {_coconut_format_3})".format(_coconut_format_0=(self.obj_name), _coconut_format_1=(name), _coconut_format_2=(self.obj_name), _coconut_format_3=(valid_names)))

    def get(self, name, default=None):
        """Attempt to __getitem__ else default."""
        try:
            return self[name]
        except (ValueError, TypeError):
            return default

    def register(self, name, value, replace=False):
        """Register value under the given name."""
        if not replace:
            _coconut_match_to_1 = self.registered
            _coconut_match_check_1 = False
            if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to_1.get(name, _coconut_sentinel)
                if _coconut_match_temp_0 is not _coconut_sentinel:
                    stored_val = _coconut_match_temp_0
                    _coconut_match_check_1 = True
            if _coconut_match_check_1:
                if stored_val == value:
                    return
                else:
                    raise ValueError("cannot change registry for already existing name: {_coconut_format_0}".format(_coconut_format_0=(name)))
        if name in self.aliases:
            raise ValueError("cannot register name with existing alias: {_coconut_format_0}".format(_coconut_format_0=(name)))
        for registry in self.no_conflict_registries:
            if name in registry:
                raise ValueError("cannot register name with conflicting {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(registry.obj_name), _coconut_format_1=(name)))
        self.registered[name] = value

    def register_alias(self, name, alias, replace=False):
        """Register an alias for the given name."""
        if not replace:
            _coconut_match_to_2 = self.aliases
            _coconut_match_check_2 = False
            if _coconut.isinstance(_coconut_match_to_2, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to_2.get(name, _coconut_sentinel)
                if _coconut_match_temp_0 is not _coconut_sentinel:
                    stored_alias = _coconut_match_temp_0
                    _coconut_match_check_2 = True
            if _coconut_match_check_2:
                if stored_alias == alias:
                    return
                else:
                    raise ValueError("cannot change registry for already existing alias: {_coconut_format_0}".format(_coconut_format_0=(alias)))
        if alias in self.registered:
            raise ValueError("cannot register overlapping alias: {_coconut_format_0}".format(_coconut_format_0=(alias)))
        for registry in self.no_conflict_registries:
            if name in registry:
                raise ValueError("cannot register alias with conflicting {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(registry.obj_name), _coconut_format_1=(alias)))
        self.aliases[alias] = name

    def run_gen(self, name):
        """Run the generator for the given name."""
        value = self.generators[name]()
        if value is not None:
            self.register(name, value)
        del self.generators[name]
        return self.registered[name]

    def __iter__(self):
        _coconut_yield_from_1 = _coconut.iter(self.registered)
        while True:
            try:
                yield _coconut.next(_coconut_yield_from_1)
            except _coconut.StopIteration as _coconut_yield_err_0:
                _coconut_yield_from_0 = _coconut_yield_err_0.args[0] if _coconut.len(_coconut_yield_err_0.args) > 0 else None
                break

        _coconut_yield_from_0
        _coconut_yield_from_3 = _coconut.iter(self.generators)
        while True:
            try:
                yield _coconut.next(_coconut_yield_from_3)
            except _coconut.StopIteration as _coconut_yield_err_1:
                _coconut_yield_from_2 = _coconut_yield_err_1.args[0] if _coconut.len(_coconut_yield_err_1.args) > 0 else None
                break

        _coconut_yield_from_2
        _coconut_yield_from_5 = _coconut.iter(self.aliases)
        while True:
            try:
                yield _coconut.next(_coconut_yield_from_5)
            except _coconut.StopIteration as _coconut_yield_err_2:
                _coconut_yield_from_4 = _coconut_yield_err_2.args[0] if _coconut.len(_coconut_yield_err_2.args) > 0 else None
                break

        _coconut_yield_from_4

    def __contains__(self, name):
        return name in self.registered or name in self.generators or name in self.aliases

    def run_all_gens(self):
        """Run all generators."""
        for name in self.generators:
            self.run_gen(name)

    def items(self):
        """Get all items in the registry as (name, value) pairs."""
        self.run_all_gens()
        _coconut_yield_from_7 = _coconut.iter(self.registered.items())
        while True:
            try:
                yield _coconut.next(_coconut_yield_from_7)
            except _coconut.StopIteration as _coconut_yield_err_3:
                _coconut_yield_from_6 = _coconut_yield_err_3.args[0] if _coconut.len(_coconut_yield_err_3.args) > 0 else None
                break

        _coconut_yield_from_6

    def asdict(self):
        """Convert registry to dictionary."""
        self.run_all_gens()
        return self.registered


# Registries:

_coconut_call_set_names(Registry)
backend_registry = Registry("backend")

alg_registry = Registry("algorithm")

meta_registry = Registry("meta algorithm")

alg_registry.shouldnt_conflict_with(meta_registry)
meta_registry.shouldnt_conflict_with(alg_registry)
