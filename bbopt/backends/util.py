#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x1ee25f74

# Compiled with Coconut version 2.0.0-a_dev53 [How Not to Be Seen]

"""
Utilities for use in BBopt backends.
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
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import random  #5 (line num in coconut source)

if _coconut_sys.version_info < (3, 3):  #7 (line num in coconut source)
    from collections import Iterable  #7 (line num in coconut source)
else:  #7 (line num in coconut source)
    from collections.abc import Iterable  #7 (line num in coconut source)

from bbopt import constants  #9 (line num in coconut source)
from bbopt.params import param_processor  #10 (line num in coconut source)
from bbopt.util import sorted_items  #11 (line num in coconut source)
from bbopt.util import convert_match_errors  #11 (line num in coconut source)
from bbopt.util import DictProxy  #11 (line num in coconut source)
from bbopt.util import ListProxy  #11 (line num in coconut source)
from bbopt.util import mean  #11 (line num in coconut source)
from bbopt.registry import backend_registry  #18 (line num in coconut source)
from bbopt.registry import alg_registry  #18 (line num in coconut source)
from bbopt.registry import meta_registry  #18 (line num in coconut source)


# Utilities:

@convert_match_errors  #27 (line num in coconut source)
@_coconut_mark_as_match  #28 (line num in coconut source)
def _init_backend(*_coconut_match_args, **_coconut_match_kwargs):  #28 (line num in coconut source)
    """Create a backend object with the given data (backend can be backend name or class)."""  #29 (line num in coconut source)
    _coconut_match_check_0 = False  #30 (line num in coconut source)
    _coconut_match_set_name_backend_cls = _coconut_sentinel  #30 (line num in coconut source)
    _coconut_match_set_name_examples = _coconut_sentinel  #30 (line num in coconut source)
    _coconut_match_set_name_params = _coconut_sentinel  #30 (line num in coconut source)
    _coconut_match_set_name_args = _coconut_sentinel  #30 (line num in coconut source)
    _coconut_match_set_name__attempt_to_update_backend = _coconut_sentinel  #30 (line num in coconut source)
    _coconut_match_set_name__on_new_backend = _coconut_sentinel  #30 (line num in coconut source)
    _coconut_match_set_name_options = _coconut_sentinel  #30 (line num in coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #30 (line num in coconut source)
    if (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "backend_cls" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "params" in _coconut_match_kwargs)) == 1):  #30 (line num in coconut source)
        _coconut_match_set_name_args = _coconut_match_args[3:]  #30 (line num in coconut source)
        _coconut_match_temp_3 = _coconut_match_kwargs.pop("_attempt_to_update_backend") if "_attempt_to_update_backend" in _coconut_match_kwargs else None  #30 (line num in coconut source)
        _coconut_match_temp_4 = _coconut_match_kwargs.pop("_on_new_backend") if "_on_new_backend" in _coconut_match_kwargs else None  #30 (line num in coconut source)
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("backend_cls")  #30 (line num in coconut source)
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("examples")  #30 (line num in coconut source)
        _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("params")  #30 (line num in coconut source)
        _coconut_match_set_name__attempt_to_update_backend = _coconut_match_temp_3  #30 (line num in coconut source)
        _coconut_match_set_name__on_new_backend = _coconut_match_temp_4  #30 (line num in coconut source)
        _coconut_match_set_name_backend_cls = _coconut_match_temp_0  #30 (line num in coconut source)
        _coconut_match_set_name_examples = _coconut_match_temp_1  #30 (line num in coconut source)
        _coconut_match_set_name_params = _coconut_match_temp_2  #30 (line num in coconut source)
        _coconut_match_set_name_options = _coconut_match_kwargs  #30 (line num in coconut source)
        _coconut_match_check_0 = True  #30 (line num in coconut source)
    if _coconut_match_check_0:  #30 (line num in coconut source)
        if _coconut_match_set_name_backend_cls is not _coconut_sentinel:  #30 (line num in coconut source)
            backend_cls = _coconut_match_set_name_backend_cls  #30 (line num in coconut source)
        if _coconut_match_set_name_examples is not _coconut_sentinel:  #30 (line num in coconut source)
            examples = _coconut_match_set_name_examples  #30 (line num in coconut source)
        if _coconut_match_set_name_params is not _coconut_sentinel:  #30 (line num in coconut source)
            params = _coconut_match_set_name_params  #30 (line num in coconut source)
        if _coconut_match_set_name_args is not _coconut_sentinel:  #30 (line num in coconut source)
            args = _coconut_match_set_name_args  #30 (line num in coconut source)
        if _coconut_match_set_name__attempt_to_update_backend is not _coconut_sentinel:  #30 (line num in coconut source)
            _attempt_to_update_backend = _coconut_match_set_name__attempt_to_update_backend  #30 (line num in coconut source)
        if _coconut_match_set_name__on_new_backend is not _coconut_sentinel:  #30 (line num in coconut source)
            _on_new_backend = _coconut_match_set_name__on_new_backend  #30 (line num in coconut source)
        if _coconut_match_set_name_options is not _coconut_sentinel:  #30 (line num in coconut source)
            options = _coconut_match_set_name_options  #30 (line num in coconut source)
    if not _coconut_match_check_0:  #30 (line num in coconut source)
        raise _coconut_FunctionMatchError('match def _init_backend(backend_cls, examples, params, *args, _attempt_to_update_backend=None, _on_new_backend=None, **options):', _coconut_match_args)  #30 (line num in coconut source)

    backend_examples = examples[:]  #30 (line num in coconut source)
    backend_params = params.copy()  #31 (line num in coconut source)

    new_backend = None  #33 (line num in coconut source)
    if isinstance(_attempt_to_update_backend, backend_cls):  #34 (line num in coconut source)
        updated_backend = _attempt_to_update_backend.attempt_update(backend_examples, backend_params, *args, **options)  #35 (line num in coconut source)
        if updated_backend is True:  #36 (line num in coconut source)
            new_backend = _attempt_to_update_backend  #37 (line num in coconut source)
        elif isinstance(updated_backend, backend_cls):  #38 (line num in coconut source)
            new_backend = updated_backend  #39 (line num in coconut source)
        else:  #40 (line num in coconut source)
            assert updated_backend is False, "invalid {_coconut_format_0}.attempt_update return value: {_coconut_format_1}".format(_coconut_format_0=(backend_cls), _coconut_format_1=(updated_backend))  #41 (line num in coconut source)

    if new_backend is None:  #43 (line num in coconut source)
        assert not _attempt_to_update_backend or isinstance(_attempt_to_update_backend, Backend), "invalid backend to attempt update on: {_coconut_format_0}".format(_coconut_format_0=(_attempt_to_update_backend))  #44 (line num in coconut source)
        new_backend = backend_cls(backend_examples, backend_params, *args, **options)  #45 (line num in coconut source)
        if _on_new_backend is not None:  #46 (line num in coconut source)
            _on_new_backend(new_backend)  #47 (line num in coconut source)

    return new_backend  #49 (line num in coconut source)



def _make_safe_backend_store(backend_store, remove_backends):  #52 (line num in coconut source)
    """Get a new backend_store without the given remove_backends."""  #53 (line num in coconut source)
    safe_backend_store = DictProxy(old_dict=backend_store, new_dict=backend_store.copy())  #54 (line num in coconut source)
    for backend_cls in backend_store:  #55 (line num in coconut source)
        if any((isinstance(rem_backend, backend_cls) for rem_backend in remove_backends)):  #56 (line num in coconut source)
            safe_specific_backends = []  #57 (line num in coconut source)
            for stored_args, stored_options, stored_backend in backend_store[backend_cls]:  #58 (line num in coconut source)
                if stored_backend not in remove_backends:  #59 (line num in coconut source)
                    safe_specific_backends.append((stored_args, stored_options, stored_backend))  #60 (line num in coconut source)
            safe_backend_store[backend_cls] = ListProxy(old_list=backend_store[backend_cls], new_list=safe_specific_backends)  #61 (line num in coconut source)
    return safe_backend_store  #62 (line num in coconut source)



@_coconut_mark_as_match  #65 (line num in coconut source)
def get_backend(*_coconut_match_args, **_coconut_match_kwargs):  #65 (line num in coconut source)
    """Create a backend object, attempting to update a backend from backend_store."""  #66 (line num in coconut source)
    _coconut_match_check_1 = False  #67 (line num in coconut source)
    _coconut_match_set_name_backend_store = _coconut_sentinel  #67 (line num in coconut source)
    _coconut_match_set_name_backend = _coconut_sentinel  #67 (line num in coconut source)
    _coconut_match_set_name_examples = _coconut_sentinel  #67 (line num in coconut source)
    _coconut_match_set_name_params = _coconut_sentinel  #67 (line num in coconut source)
    _coconut_match_set_name_args = _coconut_sentinel  #67 (line num in coconut source)
    _coconut_match_set_name__current_backend = _coconut_sentinel  #67 (line num in coconut source)
    _coconut_match_set_name__on_new_backend = _coconut_sentinel  #67 (line num in coconut source)
    _coconut_match_set_name_options = _coconut_sentinel  #67 (line num in coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #67 (line num in coconut source)
    if (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "backend_store" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "backend" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "params" in _coconut_match_kwargs)) == 1):  #67 (line num in coconut source)
        _coconut_match_set_name_args = _coconut_match_args[4:]  #67 (line num in coconut source)
        _coconut_match_temp_9 = _coconut_match_kwargs.pop("_current_backend") if "_current_backend" in _coconut_match_kwargs else None  #67 (line num in coconut source)
        _coconut_match_temp_10 = _coconut_match_kwargs.pop("_on_new_backend") if "_on_new_backend" in _coconut_match_kwargs else None  #67 (line num in coconut source)
        _coconut_match_temp_5 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("backend_store")  #67 (line num in coconut source)
        _coconut_match_temp_6 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("backend")  #67 (line num in coconut source)
        _coconut_match_temp_7 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("examples")  #67 (line num in coconut source)
        _coconut_match_temp_8 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("params")  #67 (line num in coconut source)
        _coconut_match_set_name__current_backend = _coconut_match_temp_9  #67 (line num in coconut source)
        _coconut_match_set_name__on_new_backend = _coconut_match_temp_10  #67 (line num in coconut source)
        _coconut_match_set_name_backend_store = _coconut_match_temp_5  #67 (line num in coconut source)
        _coconut_match_set_name_backend = _coconut_match_temp_6  #67 (line num in coconut source)
        _coconut_match_set_name_examples = _coconut_match_temp_7  #67 (line num in coconut source)
        _coconut_match_set_name_params = _coconut_match_temp_8  #67 (line num in coconut source)
        _coconut_match_set_name_options = _coconut_match_kwargs  #67 (line num in coconut source)
        _coconut_match_check_1 = True  #67 (line num in coconut source)
    if _coconut_match_check_1:  #67 (line num in coconut source)
        if _coconut_match_set_name_backend_store is not _coconut_sentinel:  #67 (line num in coconut source)
            backend_store = _coconut_match_set_name_backend_store  #67 (line num in coconut source)
        if _coconut_match_set_name_backend is not _coconut_sentinel:  #67 (line num in coconut source)
            backend = _coconut_match_set_name_backend  #67 (line num in coconut source)
        if _coconut_match_set_name_examples is not _coconut_sentinel:  #67 (line num in coconut source)
            examples = _coconut_match_set_name_examples  #67 (line num in coconut source)
        if _coconut_match_set_name_params is not _coconut_sentinel:  #67 (line num in coconut source)
            params = _coconut_match_set_name_params  #67 (line num in coconut source)
        if _coconut_match_set_name_args is not _coconut_sentinel:  #67 (line num in coconut source)
            args = _coconut_match_set_name_args  #67 (line num in coconut source)
        if _coconut_match_set_name__current_backend is not _coconut_sentinel:  #67 (line num in coconut source)
            _current_backend = _coconut_match_set_name__current_backend  #67 (line num in coconut source)
        if _coconut_match_set_name__on_new_backend is not _coconut_sentinel:  #67 (line num in coconut source)
            _on_new_backend = _coconut_match_set_name__on_new_backend  #67 (line num in coconut source)
        if _coconut_match_set_name_options is not _coconut_sentinel:  #67 (line num in coconut source)
            options = _coconut_match_set_name_options  #67 (line num in coconut source)
    if not _coconut_match_check_1:  #67 (line num in coconut source)
        raise _coconut_FunctionMatchError('match def get_backend(backend_store, backend, examples, params, *args, _current_backend=None, _on_new_backend=None, **options):', _coconut_match_args)  #67 (line num in coconut source)

    if isinstance(backend, type) and issubclass(backend, Backend):  #67 (line num in coconut source)
        backend_cls = backend  #68 (line num in coconut source)
    else:  #69 (line num in coconut source)
        backend_cls = backend_registry[backend]  #70 (line num in coconut source)
        assert issubclass(backend_cls, Backend), "invalid backend class for {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(backend), _coconut_format_1=(backend_cls))  #71 (line num in coconut source)

    store_ind = None  #73 (line num in coconut source)
    attempt_to_update_backend = _current_backend  #74 (line num in coconut source)
    for i, (stored_args, stored_options, stored_backend) in enumerate(backend_store[backend_cls]):  #75 (line num in coconut source)
        attempt_to_update_backend = stored_backend  #76 (line num in coconut source)
        if stored_args == args and stored_options == options:  #77 (line num in coconut source)
            store_ind = i  #78 (line num in coconut source)
            break  #79 (line num in coconut source)

    if backend_cls.request_backend_store:  #81 (line num in coconut source)
        init_options = options.copy()  #82 (line num in coconut source)
        init_options["_backend_store"] = _make_safe_backend_store(backend_store, (attempt_to_update_backend,))  #83 (line num in coconut source)
    else:  #84 (line num in coconut source)
        init_options = options  #85 (line num in coconut source)

    new_backend = _init_backend(backend_cls, examples, params, *args, _attempt_to_update_backend=attempt_to_update_backend, _on_new_backend=_on_new_backend, **init_options)  #87 (line num in coconut source)

    if store_ind is None:  #97 (line num in coconut source)
        backend_store[backend_cls].append((args, options, new_backend))  #98 (line num in coconut source)
    else:  #99 (line num in coconut source)
        backend_store[backend_cls][store_ind] = (args, options, new_backend)  #100 (line num in coconut source)

    return new_backend  #102 (line num in coconut source)



def negate_objective(objective):  #105 (line num in coconut source)
    """Take the negative of the given objective (converts a gain into a loss and vice versa)."""  #106 (line num in coconut source)
    if isinstance(objective, Iterable):  #107 (line num in coconut source)
        return (list)((map)(negate_objective, objective))  #108 (line num in coconut source)
    else:  #109 (line num in coconut source)
        return -objective  #110 (line num in coconut source)



def get_names_and_features(values, params, fallback_func=param_processor.choose_default_placeholder, converters={}, convert_fallback=True,):  #113 (line num in coconut source)
    """Return an iterator of (name, feature) for the parameters in sorted order with the given fallback function.
    If passed, converters must map funcs to functions from (value, *args) -> new_value which will be run
    on the resulting value for that func (but only on fallbacks if convert_fallback)."""  #122 (line num in coconut source)
    for name, (func, args, kwargs) in sorted_items(params):  #123 (line num in coconut source)
# determine feature
        fallback = False  #125 (line num in coconut source)
        _coconut_match_to_1 = values  #126 (line num in coconut source)
        _coconut_match_check_3 = False  #126 (line num in coconut source)
        _coconut_match_set_name_feature = _coconut_sentinel  #126 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #126 (line num in coconut source)
            _coconut_match_temp_12 = _coconut_match_to_1.get(name, _coconut_sentinel)  #126 (line num in coconut source)
            if _coconut_match_temp_12 is not _coconut_sentinel:  #126 (line num in coconut source)
                _coconut_match_set_name_feature = _coconut_match_temp_12  #126 (line num in coconut source)
                _coconut_match_check_3 = True  #126 (line num in coconut source)
        if _coconut_match_check_3:  #126 (line num in coconut source)
            if _coconut_match_set_name_feature is not _coconut_sentinel:  #126 (line num in coconut source)
                feature = _coconut_match_set_name_feature  #126 (line num in coconut source)
        if _coconut_match_check_3:  #126 (line num in coconut source)
            pass  #127 (line num in coconut source)
        else:  #128 (line num in coconut source)
            _coconut_match_to_0 = kwargs  #128 (line num in coconut source)
            _coconut_match_check_2 = False  #128 (line num in coconut source)
            _coconut_match_set_name_placeholder_value = _coconut_sentinel  #128 (line num in coconut source)
            if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #128 (line num in coconut source)
                _coconut_match_temp_11 = _coconut_match_to_0.get("placeholder_when_missing", _coconut_sentinel)  #128 (line num in coconut source)
                if _coconut_match_temp_11 is not _coconut_sentinel:  #128 (line num in coconut source)
                    _coconut_match_set_name_placeholder_value = _coconut_match_temp_11  #128 (line num in coconut source)
                    _coconut_match_check_2 = True  #128 (line num in coconut source)
            if _coconut_match_check_2:  #128 (line num in coconut source)
                if _coconut_match_set_name_placeholder_value is not _coconut_sentinel:  #128 (line num in coconut source)
                    placeholder_value = _coconut_match_set_name_placeholder_value  #128 (line num in coconut source)
            if _coconut_match_check_2:  #128 (line num in coconut source)
                feature = placeholder_value  #129 (line num in coconut source)
            else:  #130 (line num in coconut source)
                fallback = True  #131 (line num in coconut source)
                feature = fallback_func(name, func, *args, **kwargs)  #132 (line num in coconut source)

# run converters
        if not fallback or convert_fallback:  #135 (line num in coconut source)
            _coconut_match_to_2 = converters  #136 (line num in coconut source)
            _coconut_match_check_4 = False  #136 (line num in coconut source)
            _coconut_match_set_name_converter_func = _coconut_sentinel  #136 (line num in coconut source)
            if _coconut.isinstance(_coconut_match_to_2, _coconut.abc.Mapping):  #136 (line num in coconut source)
                _coconut_match_temp_13 = _coconut_match_to_2.get(func, _coconut_sentinel)  #136 (line num in coconut source)
                if _coconut_match_temp_13 is not _coconut_sentinel:  #136 (line num in coconut source)
                    _coconut_match_set_name_converter_func = _coconut_match_temp_13  #136 (line num in coconut source)
                    _coconut_match_check_4 = True  #136 (line num in coconut source)
            if _coconut_match_check_4:  #136 (line num in coconut source)
                if _coconut_match_set_name_converter_func is not _coconut_sentinel:  #136 (line num in coconut source)
                    converter_func = _coconut_match_set_name_converter_func  #136 (line num in coconut source)
            if _coconut_match_check_4:  #136 (line num in coconut source)
                feature = converter_func(feature, *args)  #137 (line num in coconut source)

        yield name, feature  #139 (line num in coconut source)



def make_features(*args, **kwargs):  #142 (line num in coconut source)
    """Same as get_names_and_features but just yields the features."""  #143 (line num in coconut source)
    _coconut_yield_from_1 = _coconut.iter((starmap)(lambda name, feature: feature, get_names_and_features(*args, **kwargs)))  #144 (line num in coconut source)
    while True:  #144 (line num in coconut source)
        try:  #144 (line num in coconut source)
            yield _coconut.next(_coconut_yield_from_1)  #144 (line num in coconut source)
        except _coconut.StopIteration as _coconut_yield_err_0:  #144 (line num in coconut source)
            _coconut_yield_from_0 = _coconut_yield_err_0.args[0] if _coconut.len(_coconut_yield_err_0.args) > 0 else None  #144 (line num in coconut source)
            break  #144 (line num in coconut source)

    _coconut_yield_from_0  #144 (line num in coconut source)



def split_examples(examples, params, fallback_func=param_processor.choose_default_placeholder, converters={}, convert_fallback=True,):  #147 (line num in coconut source)
    """Split examples into a list of data points and a list of losses with the given fallback function."""  #154 (line num in coconut source)
    data_points, losses = [], []  #155 (line num in coconut source)
    for example in examples:  #156 (line num in coconut source)

# extract values, loss
        _coconut_case_match_to_0 = example  #159 (line num in coconut source)
        _coconut_case_match_check_0 = False  #159 (line num in coconut source)
        _coconut_match_set_name_values = _coconut_sentinel  #159 (line num in coconut source)
        _coconut_match_set_name_gain = _coconut_sentinel  #159 (line num in coconut source)
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):  #159 (line num in coconut source)
            _coconut_match_temp_14 = _coconut_case_match_to_0.get("values", _coconut_sentinel)  #159 (line num in coconut source)
            _coconut_match_temp_15 = _coconut_case_match_to_0.get("gain", _coconut_sentinel)  #159 (line num in coconut source)
            if (_coconut_match_temp_14 is not _coconut_sentinel) and (_coconut_match_temp_15 is not _coconut_sentinel):  #159 (line num in coconut source)
                _coconut_match_set_name_values = _coconut_match_temp_14  #159 (line num in coconut source)
                _coconut_match_set_name_gain = _coconut_match_temp_15  #159 (line num in coconut source)
                _coconut_case_match_check_0 = True  #159 (line num in coconut source)
        if _coconut_case_match_check_0:  #159 (line num in coconut source)
            if _coconut_match_set_name_values is not _coconut_sentinel:  #159 (line num in coconut source)
                values = _coconut_match_set_name_values  #159 (line num in coconut source)
            if _coconut_match_set_name_gain is not _coconut_sentinel:  #159 (line num in coconut source)
                gain = _coconut_match_set_name_gain  #159 (line num in coconut source)
        if _coconut_case_match_check_0:  #159 (line num in coconut source)
            loss = negate_objective(gain)  #161 (line num in coconut source)
        if not _coconut_case_match_check_0:  #162 (line num in coconut source)
            _coconut_match_set_name_values = _coconut_sentinel  #162 (line num in coconut source)
            _coconut_match_set_name_loss = _coconut_sentinel  #162 (line num in coconut source)
            if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):  #162 (line num in coconut source)
                _coconut_match_temp_16 = _coconut_case_match_to_0.get("values", _coconut_sentinel)  #162 (line num in coconut source)
                _coconut_match_temp_17 = _coconut_case_match_to_0.get("loss", _coconut_sentinel)  #162 (line num in coconut source)
                if (_coconut_match_temp_16 is not _coconut_sentinel) and (_coconut_match_temp_17 is not _coconut_sentinel):  #162 (line num in coconut source)
                    _coconut_match_set_name_values = _coconut_match_temp_16  #162 (line num in coconut source)
                    _coconut_match_set_name_loss = _coconut_match_temp_17  #162 (line num in coconut source)
                    _coconut_case_match_check_0 = True  #162 (line num in coconut source)
            if _coconut_case_match_check_0:  #162 (line num in coconut source)
                if _coconut_match_set_name_values is not _coconut_sentinel:  #162 (line num in coconut source)
                    values = _coconut_match_set_name_values  #162 (line num in coconut source)
                if _coconut_match_set_name_loss is not _coconut_sentinel:  #162 (line num in coconut source)
                    loss = _coconut_match_set_name_loss  #162 (line num in coconut source)
            if _coconut_case_match_check_0:  #162 (line num in coconut source)
                pass  #163 (line num in coconut source)
        if not _coconut_case_match_check_0:  #164 (line num in coconut source)
            raise ValueError("invalid example {_coconut_format_0}".format(_coconut_format_0=(example)))  #165 (line num in coconut source)

# extract features
        features = (list)(make_features(values, params, fallback_func, converters, convert_fallback))  #168 (line num in coconut source)

# add to data_points, losses
        (data_points.append)(features)  #171 (line num in coconut source)
        (losses.append)(loss)  #172 (line num in coconut source)

    return data_points, losses  #174 (line num in coconut source)



def get_named_data_points_and_losses(examples, params, *args, **kwargs):  #177 (line num in coconut source)
    """Same as split_examples but returns named_data_points instead of data_points."""  #178 (line num in coconut source)
    data_points, losses = split_examples(examples, params, *args, **kwargs)  #179 (line num in coconut source)
    named_data_points = []  #180 (line num in coconut source)
    sorted_names = list(sorted(params))  #181 (line num in coconut source)
    for point in data_points:  #182 (line num in coconut source)
        pt_val = {}  #183 (line num in coconut source)
        for name, item in zip(sorted_names, point):  #184 (line num in coconut source)
            pt_val[name] = item  #185 (line num in coconut source)
        named_data_points.append(pt_val)  #186 (line num in coconut source)
    return named_data_points, losses  #187 (line num in coconut source)



def marginalize(named_data_points, losses, param_name, ave_func=mean):  #190 (line num in coconut source)
    """Get an average loss for each prior value of param_name."""  #191 (line num in coconut source)
    losses_for_vals = []  # we can't use a dict since vals might not be hashable  #192 (line num in coconut source)
    for point, loss in zip(named_data_points, losses):  #193 (line num in coconut source)
        val = point[param_name]  #194 (line num in coconut source)
        for check_val, check_losses in losses_for_vals:  #195 (line num in coconut source)
            if check_val == val:  #196 (line num in coconut source)
                check_losses.append(loss)  #197 (line num in coconut source)
                break  #198 (line num in coconut source)
        else:  # no break  #199 (line num in coconut source)
            losses_for_vals.append((val, [loss,]))  #200 (line num in coconut source)

    marginals = []  #202 (line num in coconut source)
    for val, all_losses in losses_for_vals:  #203 (line num in coconut source)
        marginals.append((val, ave_func(all_losses)))  #204 (line num in coconut source)
    return marginals  #205 (line num in coconut source)



def get_cum_probs_for(distribution):  #208 (line num in coconut source)
    """Generate cumulative probabilities from the given distribution."""  #209 (line num in coconut source)
    cum_probs = []  #210 (line num in coconut source)
    total_weight = sum((weight for elem, weight in distribution))  #211 (line num in coconut source)
    prev_cutoff = 0  #212 (line num in coconut source)
    for elem, weight in distribution:  #213 (line num in coconut source)
        if weight == float("inf"):  #214 (line num in coconut source)
            cutoff = 1  #215 (line num in coconut source)
        elif weight in (float("-inf"), float("nan")) or total_weight == float("nan"):  #216 (line num in coconut source)
            cutoff = prev_cutoff  #217 (line num in coconut source)
        else:  #218 (line num in coconut source)
            cutoff = prev_cutoff + weight / total_weight  #219 (line num in coconut source)
        cum_probs.append((elem, cutoff))  #220 (line num in coconut source)
        prev_cutoff = cutoff  #221 (line num in coconut source)
    return cum_probs  #222 (line num in coconut source)



def random_from_cum_probs(cum_probs):  #225 (line num in coconut source)
    """Randomly choose an element using cum_probs."""  #226 (line num in coconut source)
    rand_val = random.random()  #227 (line num in coconut source)
    for elem, cutoff in cum_probs:  #228 (line num in coconut source)
        if rand_val <= cutoff:  #229 (line num in coconut source)
            return elem  #230 (line num in coconut source)
    return None  #231 (line num in coconut source)



def make_values(params, point):  #234 (line num in coconut source)
    """Return a dictionary with the values replaced by the values in point,
    where point is a list of the values corresponding to the sorted params."""  #236 (line num in coconut source)
    values = {}  #237 (line num in coconut source)
    for i, k in (enumerate)((sorted)(params)):  #238 (line num in coconut source)
        values[k] = point[i]  #239 (line num in coconut source)
    return values  #240 (line num in coconut source)



def serve_values(name, func, args, kwargs, serving_values, fallback_func, backend_name=None, implemented_funcs=None, supported_kwargs=None,):  #243 (line num in coconut source)
    """Determines the parameter value to serve for the given parameter
    name and kwargs. First checks for unsupported funcs or kwargs, then
    uses the following algorithm:
    1. if name in serving_values, use serving_values[name], else
    2. if guess in kwargs, use the guess, else
    3. call fallback_func(name, func, *args, **kwargs)."""  #259 (line num in coconut source)
# validate arguments
    if implemented_funcs is not None:  #261 (line num in coconut source)
        assert backend_name is not None, "serve_values expects a backend_name argument when doing func validation"  #262 (line num in coconut source)
        if func not in implemented_funcs:  #263 (line num in coconut source)
            raise ValueError("the {_coconut_format_0} backend does not implement the {_coconut_format_1} function".format(_coconut_format_0=(backend_name), _coconut_format_1=(func)))  #264 (line num in coconut source)
    if supported_kwargs is not None:  #265 (line num in coconut source)
        assert backend_name is not None, "serve_values expects a backend_name argument when doing kwargs validation"  #266 (line num in coconut source)
        unsupported_kwargs = set(kwargs) - set(supported_kwargs)  #267 (line num in coconut source)
        if unsupported_kwargs:  #268 (line num in coconut source)
            raise ValueError("the {_coconut_format_0} backend does not support {_coconut_format_1} option(s)".format(_coconut_format_0=(backend_name), _coconut_format_1=(unsupported_kwargs)))  #269 (line num in coconut source)

# determine value
    _coconut_match_to_4 = serving_values  #272 (line num in coconut source)
    _coconut_match_check_6 = False  #272 (line num in coconut source)
    _coconut_match_set_name_value = _coconut_sentinel  #272 (line num in coconut source)
    if _coconut.isinstance(_coconut_match_to_4, _coconut.abc.Mapping):  #272 (line num in coconut source)
        _coconut_match_temp_19 = _coconut_match_to_4.get(name, _coconut_sentinel)  #272 (line num in coconut source)
        if _coconut_match_temp_19 is not _coconut_sentinel:  #272 (line num in coconut source)
            _coconut_match_set_name_value = _coconut_match_temp_19  #272 (line num in coconut source)
            _coconut_match_check_6 = True  #272 (line num in coconut source)
    if _coconut_match_check_6:  #272 (line num in coconut source)
        if _coconut_match_set_name_value is not _coconut_sentinel:  #272 (line num in coconut source)
            value = _coconut_match_set_name_value  #272 (line num in coconut source)
    if _coconut_match_check_6:  #272 (line num in coconut source)
        return value  #273 (line num in coconut source)
    else:  #274 (line num in coconut source)
        _coconut_match_to_3 = kwargs  #274 (line num in coconut source)
        _coconut_match_check_5 = False  #274 (line num in coconut source)
        _coconut_match_set_name_guess = _coconut_sentinel  #274 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_3, _coconut.abc.Mapping):  #274 (line num in coconut source)
            _coconut_match_temp_18 = _coconut_match_to_3.get("guess", _coconut_sentinel)  #274 (line num in coconut source)
            if _coconut_match_temp_18 is not _coconut_sentinel:  #274 (line num in coconut source)
                _coconut_match_set_name_guess = _coconut_match_temp_18  #274 (line num in coconut source)
                _coconut_match_check_5 = True  #274 (line num in coconut source)
        if _coconut_match_check_5:  #274 (line num in coconut source)
            if _coconut_match_set_name_guess is not _coconut_sentinel:  #274 (line num in coconut source)
                guess = _coconut_match_set_name_guess  #274 (line num in coconut source)
        if _coconut_match_check_5:  #274 (line num in coconut source)
            return guess  #275 (line num in coconut source)
        else:  #276 (line num in coconut source)
            return fallback_func(name, func, *args, **kwargs)  #277 (line num in coconut source)


# Backend base classes:


class Backend(_coconut.object):  #282 (line num in coconut source)
    """Base class for all BBopt backends."""  #283 (line num in coconut source)
# derived classes should always set this
    backend_name = None  #285 (line num in coconut source)

# derived classes can modify these if they want to further
#  restrict the set of supported funcs and/or kwargs
    implemented_funcs = None  #289 (line num in coconut source)
    supported_kwargs = ("guess", "placeholder_when_missing")  #290 (line num in coconut source)

# derived classes must set this on each run if they want to
#  use the default param implementation
    current_values = None  #297 (line num in coconut source)

# derived classes must set this if they want to use the
#  default fallback_func implementation
    fallback_backend = None  #301 (line num in coconut source)

# derived classes can implement tell_examples(new_examples)
#  to allow fast updating on new data
    tell_examples = None  #305 (line num in coconut source)

# derived classes can set this to True to have a _backend_store keyword
#  argument passed to __init__ with an object usable in get_backend
    request_backend_store = False  #309 (line num in coconut source)

    def __new__(cls, examples=None, params=None, *args, **kwargs):  #311 (line num in coconut source)
        __class__ = Backend  #312 (line num in coconut source)

        self = super().__new__(cls)  #312 (line num in coconut source)
        if self.tell_examples is not None:  #313 (line num in coconut source)
            self._examples = examples  #314 (line num in coconut source)
            self._params = params  #315 (line num in coconut source)
            self._args = args  #316 (line num in coconut source)
            self._kwargs = kwargs  #317 (line num in coconut source)
        return self  #318 (line num in coconut source)


    def __init__(self, examples=None, params=None, *args, **kwargs):  #320 (line num in coconut source)
        """Just call attempt_update by default."""  #321 (line num in coconut source)
        self._examples = []  #322 (line num in coconut source)
        result = self.attempt_update(examples, params, *args, **kwargs)  #323 (line num in coconut source)
        assert result, "Backend.__init__: {_coconut_format_0}.attempt_update(*{_coconut_format_1}, **{_coconut_format_2}) failed with result {_coconut_format_3!r}".format(_coconut_format_0=(self.__class__.__name__), _coconut_format_1=(args), _coconut_format_2=(kwargs), _coconut_format_3=(result))  #324 (line num in coconut source)


    def attempt_update(self, examples=None, params=None, *args, **kwargs):  #326 (line num in coconut source)
        """Attempt to update this backend with new arguments. False indicates that the
        update failed while True indicates a successful update."""  #328 (line num in coconut source)
        if (self.tell_examples is None or not self._params or params != self._params or args != self._args or kwargs != self._kwargs):  #329 (line num in coconut source)
            return False  #334 (line num in coconut source)
        old_examples, new_examples = examples[:len(self._examples)], examples[len(self._examples):]  #335 (line num in coconut source)
        if old_examples != self._examples:  #336 (line num in coconut source)
            return False  #337 (line num in coconut source)
        if new_examples:  #338 (line num in coconut source)
            try:  #339 (line num in coconut source)
                self.tell_examples(new_examples)  #340 (line num in coconut source)
            except NotImplementedError:  #341 (line num in coconut source)
                return False  #342 (line num in coconut source)
        self._examples = examples  #343 (line num in coconut source)
        return True  #344 (line num in coconut source)


    def init_fallback_backend(self):  #346 (line num in coconut source)
        """Set fallback_backend to a new random backend instance."""  #347 (line num in coconut source)
        self.fallback_backend = backend_registry[constants.default_fallback_backend]()  #348 (line num in coconut source)


    def fallback_func(self, name, func, *args, **kwargs):  #350 (line num in coconut source)
        """Default fallback_func calls self.fallback_backend.param."""  #351 (line num in coconut source)
        assert self.fallback_backend is not None, "Backend subclasses using Backend.fallback_func must set fallback_backend"  #352 (line num in coconut source)
        return self.fallback_backend.param(name, func, *args, **kwargs)  #353 (line num in coconut source)


    def param(self, name, func, *args, **kwargs):  #355 (line num in coconut source)
        """Default param calls serve_values with self.current_values and self.fallback_func."""  #356 (line num in coconut source)
        assert self.current_values is not None and (isinstance)(self.current_values, dict), "Backend subclasses using Backend.param must set current_values"  #357 (line num in coconut source)
        return serve_values(name, func, args, kwargs, serving_values=self.current_values, fallback_func=self.fallback_func, backend_name=self.backend_name, implemented_funcs=self.implemented_funcs, supported_kwargs=self.supported_kwargs)  #358 (line num in coconut source)


    registered_algs = None  #370 (line num in coconut source)

    @classmethod  #372 (line num in coconut source)
    def register(cls):  #373 (line num in coconut source)
        """Register this backend to the backend registry."""  #374 (line num in coconut source)
        assert cls.backend_name is not None, "Backend subclasses using Backend.register must set backend_name on the class"  #375 (line num in coconut source)
        backend_registry.register(cls.backend_name, cls)  #376 (line num in coconut source)

# clear out registered_algs when register is called, since that
#  probably indicates a subclass is trying to register new algs
        cls.registered_algs = []  #380 (line num in coconut source)


    @classmethod  #382 (line num in coconut source)
    def register_alias(cls, alias):  #383 (line num in coconut source)
        """Register an alias for this backend."""  #384 (line num in coconut source)
        assert cls.backend_name is not None, "Backend subclasses using Backend.register_alias must set backend_name on the class"  #385 (line num in coconut source)
        backend_registry.register_alias(cls.backend_name, alias)  #386 (line num in coconut source)


    @classmethod  #388 (line num in coconut source)
    def register_alg(cls, alg_name, **options):  #389 (line num in coconut source)
        """Register an algorithm under the given name that calls this backend with the given options."""  #390 (line num in coconut source)
        assert cls.backend_name is not None, "Backend subclasses using Backend.register_alg must set backend_name on the class"  #391 (line num in coconut source)
        alg_registry.register(alg_name, (cls.backend_name, options))  #392 (line num in coconut source)

        assert cls.registered_algs is not None, "Backend.register_alg must come after Backend.register"  #394 (line num in coconut source)
        cls.registered_algs.append(alg_name)  #395 (line num in coconut source)


    @classmethod  #397 (line num in coconut source)
    def register_meta_for_all_algs(cls, alg_name, meta_alg=constants.default_alg_sentinel):  #398 (line num in coconut source)
        """Register a meta algorithm for all the algs registered on this class."""  #399 (line num in coconut source)
        assert cls.registered_algs is not None, "register_meta_for_all_algs requires prior register_alg calls"  #400 (line num in coconut source)
        cls.register_meta(alg_name, cls.registered_algs, meta_alg)  #401 (line num in coconut source)


    @staticmethod  #403 (line num in coconut source)
    def register_meta(alg_name, algs, meta_alg=constants.default_alg_sentinel):  #404 (line num in coconut source)
        """Register an algorithm that defers to run_meta."""  #405 (line num in coconut source)
        meta_registry.register(alg_name, (algs, meta_alg))  #406 (line num in coconut source)


    @staticmethod  #408 (line num in coconut source)
    def register_param_func(func_name, handler, placeholder_generator, support_check_func):  #409 (line num in coconut source)
        """Register a new parameter definition function. See bbopt.params for examples."""  #410 (line num in coconut source)
        param_processor.register(func_name, handler, placeholder_generator, support_check_func)  #411 (line num in coconut source)



_coconut_call_set_names(Backend)  #414 (line num in coconut source)
class StandardBackend(Backend):  #414 (line num in coconut source)
    """Base class for standard BBopt backends."""  #415 (line num in coconut source)

    def __init__(self, examples, params, *args, **kwargs):  #417 (line num in coconut source)
        """Implement __init__ using setup_backend and tell_examples."""  #418 (line num in coconut source)
        self.init_fallback_backend()  #419 (line num in coconut source)

        if not params:  #421 (line num in coconut source)
            self.current_values = {}  #422 (line num in coconut source)
            return  #423 (line num in coconut source)

        self.setup_backend(params, *args, **kwargs)  #425 (line num in coconut source)

        if examples:  #427 (line num in coconut source)
            self.tell_examples(examples)  #428 (line num in coconut source)
        else:  #429 (line num in coconut source)
            self.current_values = {}  #430 (line num in coconut source)


    @override  #432 (line num in coconut source)
    def tell_examples(self, new_examples):  #433 (line num in coconut source)
        """Implements tell_examples by calling tell_data."""  #434 (line num in coconut source)
        new_data, new_losses = get_named_data_points_and_losses(new_examples, self._params)  #435 (line num in coconut source)
        self.tell_data(new_data, new_losses)  #436 (line num in coconut source)
        self.current_values = self.get_next_values()  #437 (line num in coconut source)


    def setup_backend(self, params, *args, **kwargs):  #439 (line num in coconut source)
        """Override setup_backend with any setup work that needs to be done."""  #440 (line num in coconut source)
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.__init__ must define a setup_backend(params, *args, **kwargs) method")  #441 (line num in coconut source)


    def tell_data(self, new_data, new_losses):  #443 (line num in coconut source)
        """Override tell_data with any work that needs to be done to add the given data and losses."""  #444 (line num in coconut source)
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.tell_examples must define a tell_data(new_data, new_losses) method")  #445 (line num in coconut source)


    def get_next_values(self):  #447 (line num in coconut source)
        """Override get_next_values to produce the next set of values that should be evaluated."""  #448 (line num in coconut source)
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.tell_examples must define a get_next_values() method")  #449 (line num in coconut source)


_coconut_call_set_names(StandardBackend)  #451 (line num in coconut source)
