#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xff1b716f

# Compiled with Coconut version 3.0.0-a_dev36

"""
The backend and algorithm registries.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
_coconut_header_info = ('3.0.0-a_dev36', '', True)
import os as _coconut_os
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
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



# Registry class:

class Registry(_coconut.object):  #7 (line in Coconut source)
    """Registry that keeps track of registered objects."""  #8 (line in Coconut source)

    def __init__(self, obj_name, defaults=None, generators=None, aliases=None):  #10 (line in Coconut source)
        self.obj_name = obj_name  #11 (line in Coconut source)
        self.registered = (_coconut.dict() if defaults is None else defaults)  #12 (line in Coconut source)
        self.generators = (_coconut.dict() if generators is None else generators)  #13 (line in Coconut source)
        self.aliases = (_coconut.dict() if aliases is None else aliases)  #14 (line in Coconut source)
        self.no_conflict_registries = []  #15 (line in Coconut source)


    def shouldnt_conflict_with(self, registry):  #17 (line in Coconut source)
        """Add the given registry to the no conflict registries."""  #18 (line in Coconut source)
        self.no_conflict_registries.append(registry)  #19 (line in Coconut source)


    def __getitem__(self, name):  #21 (line in Coconut source)
        name = self.aliases.get(name, name)  #22 (line in Coconut source)
        _coconut_match_to_0 = self.registered  #23 (line in Coconut source)
        _coconut_match_check_0 = False  #23 (line in Coconut source)
        _coconut_match_set_name_value = _coconut_sentinel  #23 (line in Coconut source)
        if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #23 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_match_to_0.get(name, _coconut_sentinel)  #23 (line in Coconut source)
            if _coconut_match_temp_0 is not _coconut_sentinel:  #23 (line in Coconut source)
                _coconut_match_set_name_value = _coconut_match_temp_0  #23 (line in Coconut source)
                _coconut_match_check_0 = True  #23 (line in Coconut source)
        if _coconut_match_check_0:  #23 (line in Coconut source)
            if _coconut_match_set_name_value is not _coconut_sentinel:  #23 (line in Coconut source)
                value = _coconut_match_set_name_value  #23 (line in Coconut source)
        if _coconut_match_check_0:  #23 (line in Coconut source)
            return value  #24 (line in Coconut source)
        else:  #25 (line in Coconut source)
            if name in self.generators:  #25 (line in Coconut source)
                return self.run_gen(name)  #26 (line in Coconut source)
            else:  #27 (line in Coconut source)
                for registry in self.no_conflict_registries:  #28 (line in Coconut source)
                    if name in registry:  #29 (line in Coconut source)
                        raise ValueError("invalid {_coconut_format_0}: {_coconut_format_1} ({_coconut_format_2} is a(n) {_coconut_format_3} not a(n) {_coconut_format_4})".format(_coconut_format_0=(self.obj_name), _coconut_format_1=(name), _coconut_format_2=(name), _coconut_format_3=(registry.obj_name), _coconut_format_4=(self.obj_name)))  #30 (line in Coconut source)
                valid_names = ", ".join((repr(name) for name in self))  #31 (line in Coconut source)
                raise ValueError("unknown {_coconut_format_0}: {_coconut_format_1} (valid {_coconut_format_2}s: {_coconut_format_3})".format(_coconut_format_0=(self.obj_name), _coconut_format_1=(name), _coconut_format_2=(self.obj_name), _coconut_format_3=(valid_names)))  #32 (line in Coconut source)


    def get(self, name, default=None):  #34 (line in Coconut source)
        """Attempt to __getitem__ else default."""  #35 (line in Coconut source)
        try:  #36 (line in Coconut source)
            return self[name]  #37 (line in Coconut source)
        except (ValueError, TypeError):  #38 (line in Coconut source)
            return default  #39 (line in Coconut source)


    def register(self, name, value, replace=False):  #41 (line in Coconut source)
        """Register value under the given name."""  #42 (line in Coconut source)
        if not replace:  #43 (line in Coconut source)
            _coconut_match_to_1 = self.registered  #44 (line in Coconut source)
            _coconut_match_check_1 = False  #44 (line in Coconut source)
            _coconut_match_set_name_stored_val = _coconut_sentinel  #44 (line in Coconut source)
            if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #44 (line in Coconut source)
                _coconut_match_temp_1 = _coconut_match_to_1.get(name, _coconut_sentinel)  #44 (line in Coconut source)
                if _coconut_match_temp_1 is not _coconut_sentinel:  #44 (line in Coconut source)
                    _coconut_match_set_name_stored_val = _coconut_match_temp_1  #44 (line in Coconut source)
                    _coconut_match_check_1 = True  #44 (line in Coconut source)
            if _coconut_match_check_1:  #44 (line in Coconut source)
                if _coconut_match_set_name_stored_val is not _coconut_sentinel:  #44 (line in Coconut source)
                    stored_val = _coconut_match_set_name_stored_val  #44 (line in Coconut source)
            if _coconut_match_check_1:  #44 (line in Coconut source)
                if stored_val == value:  #45 (line in Coconut source)
                    return  #46 (line in Coconut source)
                else:  #47 (line in Coconut source)
                    raise ValueError("cannot change registry for already existing name: {_coconut_format_0}".format(_coconut_format_0=(name)))  #48 (line in Coconut source)
        if name in self.aliases:  #49 (line in Coconut source)
            raise ValueError("cannot register name with existing alias: {_coconut_format_0}".format(_coconut_format_0=(name)))  #50 (line in Coconut source)
        for registry in self.no_conflict_registries:  #51 (line in Coconut source)
            if name in registry:  #52 (line in Coconut source)
                raise ValueError("cannot register name with conflicting {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(registry.obj_name), _coconut_format_1=(name)))  #53 (line in Coconut source)
        self.registered[name] = value  #54 (line in Coconut source)


    def register_alias(self, name, alias, replace=False):  #56 (line in Coconut source)
        """Register an alias for the given name."""  #57 (line in Coconut source)
        if not replace:  #58 (line in Coconut source)
            _coconut_match_to_2 = self.aliases  #59 (line in Coconut source)
            _coconut_match_check_2 = False  #59 (line in Coconut source)
            _coconut_match_set_name_stored_alias = _coconut_sentinel  #59 (line in Coconut source)
            if _coconut.isinstance(_coconut_match_to_2, _coconut.abc.Mapping):  #59 (line in Coconut source)
                _coconut_match_temp_2 = _coconut_match_to_2.get(name, _coconut_sentinel)  #59 (line in Coconut source)
                if _coconut_match_temp_2 is not _coconut_sentinel:  #59 (line in Coconut source)
                    _coconut_match_set_name_stored_alias = _coconut_match_temp_2  #59 (line in Coconut source)
                    _coconut_match_check_2 = True  #59 (line in Coconut source)
            if _coconut_match_check_2:  #59 (line in Coconut source)
                if _coconut_match_set_name_stored_alias is not _coconut_sentinel:  #59 (line in Coconut source)
                    stored_alias = _coconut_match_set_name_stored_alias  #59 (line in Coconut source)
            if _coconut_match_check_2:  #59 (line in Coconut source)
                if stored_alias == alias:  #60 (line in Coconut source)
                    return  #61 (line in Coconut source)
                else:  #62 (line in Coconut source)
                    raise ValueError("cannot change registry for already existing alias: {_coconut_format_0}".format(_coconut_format_0=(alias)))  #63 (line in Coconut source)
        if alias in self.registered:  #64 (line in Coconut source)
            raise ValueError("cannot register overlapping alias: {_coconut_format_0}".format(_coconut_format_0=(alias)))  #65 (line in Coconut source)
        for registry in self.no_conflict_registries:  #66 (line in Coconut source)
            if name in registry:  #67 (line in Coconut source)
                raise ValueError("cannot register alias with conflicting {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(registry.obj_name), _coconut_format_1=(alias)))  #68 (line in Coconut source)
        self.aliases[alias] = name  #69 (line in Coconut source)


    def run_gen(self, name):  #71 (line in Coconut source)
        """Run the generator for the given name."""  #72 (line in Coconut source)
        value = self.generators[name]()  #73 (line in Coconut source)
        if value is not None:  #74 (line in Coconut source)
            self.register(name, value)  #75 (line in Coconut source)
        del self.generators[name]  #76 (line in Coconut source)
        return self.registered[name]  #77 (line in Coconut source)


    def __iter__(self):  #79 (line in Coconut source)
        _coconut_yield_from_1 = _coconut.iter(self.registered)  #80 (line in Coconut source)
        while True:  #80 (line in Coconut source)
            try:  #80 (line in Coconut source)
                yield _coconut.next(_coconut_yield_from_1)  #80 (line in Coconut source)
            except _coconut.StopIteration as _coconut_yield_err_0:  #80 (line in Coconut source)
                _coconut_yield_from_0 = _coconut_yield_err_0.args[0] if _coconut.len(_coconut_yield_err_0.args) > 0 else None  #80 (line in Coconut source)
                break  #80 (line in Coconut source)
        _coconut_yield_from_0  #80 (line in Coconut source)
        _coconut_yield_from_3 = _coconut.iter(self.generators)  #81 (line in Coconut source)
        while True:  #81 (line in Coconut source)
            try:  #81 (line in Coconut source)
                yield _coconut.next(_coconut_yield_from_3)  #81 (line in Coconut source)
            except _coconut.StopIteration as _coconut_yield_err_1:  #81 (line in Coconut source)
                _coconut_yield_from_2 = _coconut_yield_err_1.args[0] if _coconut.len(_coconut_yield_err_1.args) > 0 else None  #81 (line in Coconut source)
                break  #81 (line in Coconut source)
        _coconut_yield_from_2  #81 (line in Coconut source)
        _coconut_yield_from_5 = _coconut.iter(self.aliases)  #82 (line in Coconut source)
        while True:  #82 (line in Coconut source)
            try:  #82 (line in Coconut source)
                yield _coconut.next(_coconut_yield_from_5)  #82 (line in Coconut source)
            except _coconut.StopIteration as _coconut_yield_err_2:  #82 (line in Coconut source)
                _coconut_yield_from_4 = _coconut_yield_err_2.args[0] if _coconut.len(_coconut_yield_err_2.args) > 0 else None  #82 (line in Coconut source)
                break  #82 (line in Coconut source)
        _coconut_yield_from_4  #82 (line in Coconut source)


    def __contains__(self, name):  #84 (line in Coconut source)
        return name in self.registered or name in self.generators or name in self.aliases  #85 (line in Coconut source)


    def run_all_gens(self):  #87 (line in Coconut source)
        """Run all generators."""  #88 (line in Coconut source)
        for name in self.generators:  #89 (line in Coconut source)
            self.run_gen(name)  #90 (line in Coconut source)


    def items(self):  #92 (line in Coconut source)
        """Get all items in the registry as (name, value) pairs."""  #93 (line in Coconut source)
        self.run_all_gens()  #94 (line in Coconut source)
        _coconut_yield_from_7 = _coconut.iter(self.registered.items())  #95 (line in Coconut source)
        while True:  #95 (line in Coconut source)
            try:  #95 (line in Coconut source)
                yield _coconut.next(_coconut_yield_from_7)  #95 (line in Coconut source)
            except _coconut.StopIteration as _coconut_yield_err_3:  #95 (line in Coconut source)
                _coconut_yield_from_6 = _coconut_yield_err_3.args[0] if _coconut.len(_coconut_yield_err_3.args) > 0 else None  #95 (line in Coconut source)
                break  #95 (line in Coconut source)
        _coconut_yield_from_6  #95 (line in Coconut source)


    def asdict(self):  #97 (line in Coconut source)
        """Convert registry to dictionary."""  #98 (line in Coconut source)
        self.run_all_gens()  #99 (line in Coconut source)
        return self.registered  #100 (line in Coconut source)


# Registries:


_coconut_call_set_names(Registry)  #105 (line in Coconut source)
backend_registry = Registry("backend")  #105 (line in Coconut source)

alg_registry = Registry("algorithm")  #107 (line in Coconut source)

meta_registry = Registry("meta algorithm")  #109 (line in Coconut source)

alg_registry.shouldnt_conflict_with(meta_registry)  #111 (line in Coconut source)
meta_registry.shouldnt_conflict_with(alg_registry)  #112 (line in Coconut source)
