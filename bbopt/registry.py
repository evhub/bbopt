#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x57430af2

# Compiled with Coconut version 1.5.0-post_dev7 [Fish License]

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
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
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

    def register(self, name, value, replace=False):
        """Register value under the given name."""
        if not replace and name in self.registered:
            raise ValueError("cannot register already existing name {_coconut_format_0!r}".format(_coconut_format_0=(name)))
        if name in self.aliases:
            raise ValueError("cannot register name with existing alias {_coconut_format_0!r}".format(_coconut_format_0=(name)))
        self.registered[name] = value

    def register_alias(self, name, alias, replace=False):
        """Register an alias for the given name."""
        if not replace and alias in self.aliases:
            raise ValueError("cannot register already existing alias {_coconut_format_0!r}".format(_coconut_format_0=(alias)))
        if alias in self.registered:
            raise ValueError("cannot register overlapping alias {_coconut_format_0!r}".format(_coconut_format_0=(alias)))
        self.aliases[alias] = name

    def run_gen(self, name):
        """Run the generator for the given name."""
        value = self.generators[name]()
        if value is not None:
            self.register(name, value)
        del self.generators[name]
        return self.registered[name]

    def __iter__(self):
        _coconut_yield_from = _coconut.iter(self.registered)
        while True:
            try:
                yield _coconut.next(_coconut_yield_from)
            except _coconut.StopIteration as _coconut_yield_err:
                _coconut_yield_from_0 = _coconut_yield_err.args[0] if _coconut.len(_coconut_yield_err.args) > 0 else None
                break

        _coconut_yield_from_0
        _coconut_yield_from = _coconut.iter(self.generators)
        while True:
            try:
                yield _coconut.next(_coconut_yield_from)
            except _coconut.StopIteration as _coconut_yield_err:
                _coconut_yield_from_1 = _coconut_yield_err.args[0] if _coconut.len(_coconut_yield_err.args) > 0 else None
                break

        _coconut_yield_from_1
        _coconut_yield_from = _coconut.iter(self.aliases)
        while True:
            try:
                yield _coconut.next(_coconut_yield_from)
            except _coconut.StopIteration as _coconut_yield_err:
                _coconut_yield_from_2 = _coconut_yield_err.args[0] if _coconut.len(_coconut_yield_err.args) > 0 else None
                break

        _coconut_yield_from_2

    def run_all_gens(self):
        """Run all generators."""
        for name in self.generators:
            self.run_gen(name)

    def items(self):
        """Get all items in the registry as (name, value) pairs."""
        self.run_all_gens()
        _coconut_yield_from = _coconut.iter(self.registered.items())
        while True:
            try:
                yield _coconut.next(_coconut_yield_from)
            except _coconut.StopIteration as _coconut_yield_err:
                _coconut_yield_from_3 = _coconut_yield_err.args[0] if _coconut.len(_coconut_yield_err.args) > 0 else None
                break

        _coconut_yield_from_3

    def asdict(self):
        """Convert registry to dictionary."""
        self.run_all_gens()
        return self.registered


backend_registry = Registry("backend")


@_coconut_mark_as_match
def init_backend(*_coconut_match_to_args, **_coconut_match_to_kwargs):
    """Create a backend object of the given name with the given data."""
    _coconut_match_check = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.sum((_coconut.len(_coconut_match_to_args) > 0, "name" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 1, "examples" in _coconut_match_to_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_to_args) > 2, "params" in _coconut_match_to_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_to_args[0] if _coconut.len(_coconut_match_to_args) > 0 else _coconut_match_to_kwargs.pop("name")
        _coconut_match_temp_1 = _coconut_match_to_args[1] if _coconut.len(_coconut_match_to_args) > 1 else _coconut_match_to_kwargs.pop("examples")
        _coconut_match_temp_2 = _coconut_match_to_args[2] if _coconut.len(_coconut_match_to_args) > 2 else _coconut_match_to_kwargs.pop("params")
        args = _coconut_match_to_args[3:]
        _coconut_match_temp_3 = _coconut_match_to_kwargs.pop("attempt_to_update_backend") if "attempt_to_update_backend" in _coconut_match_to_kwargs else None
        name = _coconut_match_temp_0
        examples = _coconut_match_temp_1
        params = _coconut_match_temp_2
        attempt_to_update_backend = _coconut_match_temp_3
        options = _coconut_match_to_kwargs
        _coconut_match_check = True
    if not _coconut_match_check:
        raise _coconut_FunctionMatchError('match def init_backend(name, examples, params, *args, attempt_to_update_backend=None, **options):', _coconut_match_to_args)

    backend_cls = backend_registry[name]
    if attempt_to_update_backend is not None and isinstance(attempt_to_update_backend, backend_cls):
        updated_backend = attempt_to_update_backend.attempt_update(examples, params, *args, **options)
        if updated_backend is True:
            return attempt_to_update_backend
        elif isinstance(updated_backend, backend_cls):
            return updated_backend
        else:
            assert updated_backend is False, "invalid backend.attempt_update return value {_coconut_format_0} from {_coconut_format_1}".format(_coconut_format_0=(updated_backend), _coconut_format_1=(backend_cls))
    return backend_cls(examples, params, *args, **options)


alg_registry = Registry("algorithm")
