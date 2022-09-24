#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x70ba5cdc

# Compiled with Coconut version 2.0.0-a_dev65 [How Not to Be Seen]

"""
The backend and algorithm registries.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
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



# Registry class:

class Registry(_coconut.object):  #7 (line num in coconut source)
    """Registry that keeps track of registered objects."""  #8 (line num in coconut source)

    def __init__(self, obj_name, defaults=None, generators=None, aliases=None):  #10 (line num in coconut source)
        self.obj_name = obj_name  #11 (line num in coconut source)
        self.registered = ({} if defaults is None else defaults)  #12 (line num in coconut source)
        self.generators = ({} if generators is None else generators)  #13 (line num in coconut source)
        self.aliases = ({} if aliases is None else aliases)  #14 (line num in coconut source)
        self.no_conflict_registries = []  #15 (line num in coconut source)


    def shouldnt_conflict_with(self, registry):  #17 (line num in coconut source)
        """Add the given registry to the no conflict registries."""  #18 (line num in coconut source)
        self.no_conflict_registries.append(registry)  #19 (line num in coconut source)


    def __getitem__(self, name):  #21 (line num in coconut source)
        name = self.aliases.get(name, name)  #22 (line num in coconut source)
        _coconut_match_to_0 = self.registered  #23 (line num in coconut source)
        _coconut_match_check_0 = False  #23 (line num in coconut source)
        _coconut_match_set_name_value = _coconut_sentinel  #23 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #23 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_to_0.get(name, _coconut_sentinel)  #23 (line num in coconut source)
            if _coconut_match_temp_0 is not _coconut_sentinel:  #23 (line num in coconut source)
                _coconut_match_set_name_value = _coconut_match_temp_0  #23 (line num in coconut source)
                _coconut_match_check_0 = True  #23 (line num in coconut source)
        if _coconut_match_check_0:  #23 (line num in coconut source)
            if _coconut_match_set_name_value is not _coconut_sentinel:  #23 (line num in coconut source)
                value = _coconut_match_set_name_value  #23 (line num in coconut source)
        if _coconut_match_check_0:  #23 (line num in coconut source)
            return value  #24 (line num in coconut source)
        else:  #25 (line num in coconut source)
            if name in self.generators:  #25 (line num in coconut source)
                return self.run_gen(name)  #26 (line num in coconut source)
            else:  #27 (line num in coconut source)
                for registry in self.no_conflict_registries:  #28 (line num in coconut source)
                    if name in registry:  #29 (line num in coconut source)
                        raise ValueError("invalid {_coconut_format_0}: {_coconut_format_1} ({_coconut_format_2} is a(n) {_coconut_format_3} not a(n) {_coconut_format_4})".format(_coconut_format_0=(self.obj_name), _coconut_format_1=(name), _coconut_format_2=(name), _coconut_format_3=(registry.obj_name), _coconut_format_4=(self.obj_name)))  #30 (line num in coconut source)
                valid_names = ", ".join((repr(name) for name in self))  #31 (line num in coconut source)
                raise ValueError("unknown {_coconut_format_0}: {_coconut_format_1} (valid {_coconut_format_2}s: {_coconut_format_3})".format(_coconut_format_0=(self.obj_name), _coconut_format_1=(name), _coconut_format_2=(self.obj_name), _coconut_format_3=(valid_names)))  #32 (line num in coconut source)


    def get(self, name, default=None):  #34 (line num in coconut source)
        """Attempt to __getitem__ else default."""  #35 (line num in coconut source)
        try:  #36 (line num in coconut source)
            return self[name]  #37 (line num in coconut source)
        except (ValueError, TypeError):  #38 (line num in coconut source)
            return default  #39 (line num in coconut source)


    def register(self, name, value, replace=False):  #41 (line num in coconut source)
        """Register value under the given name."""  #42 (line num in coconut source)
        if not replace:  #43 (line num in coconut source)
            _coconut_match_to_1 = self.registered  #44 (line num in coconut source)
            _coconut_match_check_1 = False  #44 (line num in coconut source)
            _coconut_match_set_name_stored_val = _coconut_sentinel  #44 (line num in coconut source)
            if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #44 (line num in coconut source)
                _coconut_match_temp_1 = _coconut_match_to_1.get(name, _coconut_sentinel)  #44 (line num in coconut source)
                if _coconut_match_temp_1 is not _coconut_sentinel:  #44 (line num in coconut source)
                    _coconut_match_set_name_stored_val = _coconut_match_temp_1  #44 (line num in coconut source)
                    _coconut_match_check_1 = True  #44 (line num in coconut source)
            if _coconut_match_check_1:  #44 (line num in coconut source)
                if _coconut_match_set_name_stored_val is not _coconut_sentinel:  #44 (line num in coconut source)
                    stored_val = _coconut_match_set_name_stored_val  #44 (line num in coconut source)
            if _coconut_match_check_1:  #44 (line num in coconut source)
                if stored_val == value:  #45 (line num in coconut source)
                    return  #46 (line num in coconut source)
                else:  #47 (line num in coconut source)
                    raise ValueError("cannot change registry for already existing name: {_coconut_format_0}".format(_coconut_format_0=(name)))  #48 (line num in coconut source)
        if name in self.aliases:  #49 (line num in coconut source)
            raise ValueError("cannot register name with existing alias: {_coconut_format_0}".format(_coconut_format_0=(name)))  #50 (line num in coconut source)
        for registry in self.no_conflict_registries:  #51 (line num in coconut source)
            if name in registry:  #52 (line num in coconut source)
                raise ValueError("cannot register name with conflicting {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(registry.obj_name), _coconut_format_1=(name)))  #53 (line num in coconut source)
        self.registered[name] = value  #54 (line num in coconut source)


    def register_alias(self, name, alias, replace=False):  #56 (line num in coconut source)
        """Register an alias for the given name."""  #57 (line num in coconut source)
        if not replace:  #58 (line num in coconut source)
            _coconut_match_to_2 = self.aliases  #59 (line num in coconut source)
            _coconut_match_check_2 = False  #59 (line num in coconut source)
            _coconut_match_set_name_stored_alias = _coconut_sentinel  #59 (line num in coconut source)
            if _coconut.isinstance(_coconut_match_to_2, _coconut.abc.Mapping):  #59 (line num in coconut source)
                _coconut_match_temp_2 = _coconut_match_to_2.get(name, _coconut_sentinel)  #59 (line num in coconut source)
                if _coconut_match_temp_2 is not _coconut_sentinel:  #59 (line num in coconut source)
                    _coconut_match_set_name_stored_alias = _coconut_match_temp_2  #59 (line num in coconut source)
                    _coconut_match_check_2 = True  #59 (line num in coconut source)
            if _coconut_match_check_2:  #59 (line num in coconut source)
                if _coconut_match_set_name_stored_alias is not _coconut_sentinel:  #59 (line num in coconut source)
                    stored_alias = _coconut_match_set_name_stored_alias  #59 (line num in coconut source)
            if _coconut_match_check_2:  #59 (line num in coconut source)
                if stored_alias == alias:  #60 (line num in coconut source)
                    return  #61 (line num in coconut source)
                else:  #62 (line num in coconut source)
                    raise ValueError("cannot change registry for already existing alias: {_coconut_format_0}".format(_coconut_format_0=(alias)))  #63 (line num in coconut source)
        if alias in self.registered:  #64 (line num in coconut source)
            raise ValueError("cannot register overlapping alias: {_coconut_format_0}".format(_coconut_format_0=(alias)))  #65 (line num in coconut source)
        for registry in self.no_conflict_registries:  #66 (line num in coconut source)
            if name in registry:  #67 (line num in coconut source)
                raise ValueError("cannot register alias with conflicting {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(registry.obj_name), _coconut_format_1=(alias)))  #68 (line num in coconut source)
        self.aliases[alias] = name  #69 (line num in coconut source)


    def run_gen(self, name):  #71 (line num in coconut source)
        """Run the generator for the given name."""  #72 (line num in coconut source)
        value = self.generators[name]()  #73 (line num in coconut source)
        if value is not None:  #74 (line num in coconut source)
            self.register(name, value)  #75 (line num in coconut source)
        del self.generators[name]  #76 (line num in coconut source)
        return self.registered[name]  #77 (line num in coconut source)


    def __iter__(self):  #79 (line num in coconut source)
        _coconut_yield_from_1 = _coconut.iter(self.registered)  #80 (line num in coconut source)
        while True:  #80 (line num in coconut source)
            try:  #80 (line num in coconut source)
                yield _coconut.next(_coconut_yield_from_1)  #80 (line num in coconut source)
            except _coconut.StopIteration as _coconut_yield_err_0:  #80 (line num in coconut source)
                _coconut_yield_from_0 = _coconut_yield_err_0.args[0] if _coconut.len(_coconut_yield_err_0.args) > 0 else None  #80 (line num in coconut source)
                break  #80 (line num in coconut source)

        _coconut_yield_from_0  #80 (line num in coconut source)
        _coconut_yield_from_3 = _coconut.iter(self.generators)  #81 (line num in coconut source)
        while True:  #81 (line num in coconut source)
            try:  #81 (line num in coconut source)
                yield _coconut.next(_coconut_yield_from_3)  #81 (line num in coconut source)
            except _coconut.StopIteration as _coconut_yield_err_1:  #81 (line num in coconut source)
                _coconut_yield_from_2 = _coconut_yield_err_1.args[0] if _coconut.len(_coconut_yield_err_1.args) > 0 else None  #81 (line num in coconut source)
                break  #81 (line num in coconut source)

        _coconut_yield_from_2  #81 (line num in coconut source)
        _coconut_yield_from_5 = _coconut.iter(self.aliases)  #82 (line num in coconut source)
        while True:  #82 (line num in coconut source)
            try:  #82 (line num in coconut source)
                yield _coconut.next(_coconut_yield_from_5)  #82 (line num in coconut source)
            except _coconut.StopIteration as _coconut_yield_err_2:  #82 (line num in coconut source)
                _coconut_yield_from_4 = _coconut_yield_err_2.args[0] if _coconut.len(_coconut_yield_err_2.args) > 0 else None  #82 (line num in coconut source)
                break  #82 (line num in coconut source)

        _coconut_yield_from_4  #82 (line num in coconut source)


    def __contains__(self, name):  #84 (line num in coconut source)
        return name in self.registered or name in self.generators or name in self.aliases  #85 (line num in coconut source)


    def run_all_gens(self):  #87 (line num in coconut source)
        """Run all generators."""  #88 (line num in coconut source)
        for name in self.generators:  #89 (line num in coconut source)
            self.run_gen(name)  #90 (line num in coconut source)


    def items(self):  #92 (line num in coconut source)
        """Get all items in the registry as (name, value) pairs."""  #93 (line num in coconut source)
        self.run_all_gens()  #94 (line num in coconut source)
        _coconut_yield_from_7 = _coconut.iter(self.registered.items())  #95 (line num in coconut source)
        while True:  #95 (line num in coconut source)
            try:  #95 (line num in coconut source)
                yield _coconut.next(_coconut_yield_from_7)  #95 (line num in coconut source)
            except _coconut.StopIteration as _coconut_yield_err_3:  #95 (line num in coconut source)
                _coconut_yield_from_6 = _coconut_yield_err_3.args[0] if _coconut.len(_coconut_yield_err_3.args) > 0 else None  #95 (line num in coconut source)
                break  #95 (line num in coconut source)

        _coconut_yield_from_6  #95 (line num in coconut source)


    def asdict(self):  #97 (line num in coconut source)
        """Convert registry to dictionary."""  #98 (line num in coconut source)
        self.run_all_gens()  #99 (line num in coconut source)
        return self.registered  #100 (line num in coconut source)


# Registries:


_coconut_call_set_names(Registry)  #105 (line num in coconut source)
backend_registry = Registry("backend")  #105 (line num in coconut source)

alg_registry = Registry("algorithm")  #107 (line num in coconut source)

meta_registry = Registry("meta algorithm")  #109 (line num in coconut source)

alg_registry.shouldnt_conflict_with(meta_registry)  #111 (line num in coconut source)
meta_registry.shouldnt_conflict_with(alg_registry)  #112 (line num in coconut source)
