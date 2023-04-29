#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x6e43bef1

# Compiled with Coconut version 3.0.0-a_dev36

"""
Utilities for use in BBopt backends.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
_coconut_header_info = ('3.0.0-a_dev36', '', True)
import os as _coconut_os
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
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



import random  #5 (line in Coconut source)

from collections import OrderedDict  #7 (line in Coconut source)
try:  #8 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #8 (line in Coconut source)
except _coconut.NameError:  #8 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #8 (line in Coconut source)
sys = _coconut_sys  #8 (line in Coconut source)
if sys.version_info >= (3, 3):  #8 (line in Coconut source)
    from collections.abc import Iterable  #8 (line in Coconut source)
else:  #8 (line in Coconut source)
    from collections import Iterable  #8 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #8 (line in Coconut source)
    sys = _coconut_sys_0  #8 (line in Coconut source)

from bbopt import constants  #10 (line in Coconut source)
from bbopt.params import param_processor  #11 (line in Coconut source)
from bbopt.util import sorted_items  #12 (line in Coconut source)
from bbopt.util import convert_match_errors  #12 (line in Coconut source)
from bbopt.util import DictProxy  #12 (line in Coconut source)
from bbopt.util import ListProxy  #12 (line in Coconut source)
from bbopt.util import mean  #12 (line in Coconut source)
from bbopt.registry import backend_registry  #19 (line in Coconut source)
from bbopt.registry import alg_registry  #19 (line in Coconut source)
from bbopt.registry import meta_registry  #19 (line in Coconut source)


# Utilities:

def sorted_params(params):  #28 (line in Coconut source)
    """Get an OrderedDict of params in sorted order."""  #29 (line in Coconut source)
    return (OrderedDict)((sorted_items)(params))  #30 (line in Coconut source)



@convert_match_errors  #33 (line in Coconut source)
@_coconut_mark_as_match  #34 (line in Coconut source)
def _init_backend(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #34 (line in Coconut source)
    """Create a backend object with the given data (backend can be backend name or class)."""  #35 (line in Coconut source)
    _coconut_match_check_0 = False  #36 (line in Coconut source)
    _coconut_match_set_name_backend_cls = _coconut_sentinel  #36 (line in Coconut source)
    _coconut_match_set_name_examples = _coconut_sentinel  #36 (line in Coconut source)
    _coconut_match_set_name_params = _coconut_sentinel  #36 (line in Coconut source)
    _coconut_match_set_name_args = _coconut_sentinel  #36 (line in Coconut source)
    _coconut_match_set_name__attempt_to_update_backend = _coconut_sentinel  #36 (line in Coconut source)
    _coconut_match_set_name__on_new_backend = _coconut_sentinel  #36 (line in Coconut source)
    _coconut_match_set_name_options = _coconut_sentinel  #36 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #36 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #36 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #36 (line in Coconut source)
    if (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "backend_cls" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "params" in _coconut_match_kwargs)) == 1):  #36 (line in Coconut source)
        _coconut_match_set_name_args = _coconut_match_args[3:]  #36 (line in Coconut source)
        _coconut_match_temp_3 = _coconut_match_kwargs.pop("_attempt_to_update_backend") if "_attempt_to_update_backend" in _coconut_match_kwargs else None  #36 (line in Coconut source)
        _coconut_match_temp_4 = _coconut_match_kwargs.pop("_on_new_backend") if "_on_new_backend" in _coconut_match_kwargs else None  #36 (line in Coconut source)
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("backend_cls")  #36 (line in Coconut source)
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("examples")  #36 (line in Coconut source)
        _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("params")  #36 (line in Coconut source)
        _coconut_match_set_name__attempt_to_update_backend = _coconut_match_temp_3  #36 (line in Coconut source)
        _coconut_match_set_name__on_new_backend = _coconut_match_temp_4  #36 (line in Coconut source)
        _coconut_match_set_name_backend_cls = _coconut_match_temp_0  #36 (line in Coconut source)
        _coconut_match_set_name_examples = _coconut_match_temp_1  #36 (line in Coconut source)
        _coconut_match_set_name_params = _coconut_match_temp_2  #36 (line in Coconut source)
        _coconut_match_set_name_options = _coconut_match_kwargs  #36 (line in Coconut source)
        _coconut_match_check_0 = True  #36 (line in Coconut source)
    if _coconut_match_check_0:  #36 (line in Coconut source)
        if _coconut_match_set_name_backend_cls is not _coconut_sentinel:  #36 (line in Coconut source)
            backend_cls = _coconut_match_set_name_backend_cls  #36 (line in Coconut source)
        if _coconut_match_set_name_examples is not _coconut_sentinel:  #36 (line in Coconut source)
            examples = _coconut_match_set_name_examples  #36 (line in Coconut source)
        if _coconut_match_set_name_params is not _coconut_sentinel:  #36 (line in Coconut source)
            params = _coconut_match_set_name_params  #36 (line in Coconut source)
        if _coconut_match_set_name_args is not _coconut_sentinel:  #36 (line in Coconut source)
            args = _coconut_match_set_name_args  #36 (line in Coconut source)
        if _coconut_match_set_name__attempt_to_update_backend is not _coconut_sentinel:  #36 (line in Coconut source)
            _attempt_to_update_backend = _coconut_match_set_name__attempt_to_update_backend  #36 (line in Coconut source)
        if _coconut_match_set_name__on_new_backend is not _coconut_sentinel:  #36 (line in Coconut source)
            _on_new_backend = _coconut_match_set_name__on_new_backend  #36 (line in Coconut source)
        if _coconut_match_set_name_options is not _coconut_sentinel:  #36 (line in Coconut source)
            options = _coconut_match_set_name_options  #36 (line in Coconut source)
    if not _coconut_match_check_0:  #36 (line in Coconut source)
        raise _coconut_FunctionMatchError('match def _init_backend(backend_cls, examples, params, *args, _attempt_to_update_backend=None, _on_new_backend=None, **options):', _coconut_match_args)  #36 (line in Coconut source)

    backend_examples = examples[:]  #36 (line in Coconut source)
    backend_params = params.copy()  #37 (line in Coconut source)

    new_backend = None  #39 (line in Coconut source)
    if isinstance(_attempt_to_update_backend, backend_cls):  #40 (line in Coconut source)
        updated_backend = _attempt_to_update_backend.attempt_update(backend_examples, backend_params, *args, **options)  #41 (line in Coconut source)
        if updated_backend is True:  #42 (line in Coconut source)
            new_backend = _attempt_to_update_backend  #43 (line in Coconut source)
        elif isinstance(updated_backend, backend_cls):  #44 (line in Coconut source)
            new_backend = updated_backend  #45 (line in Coconut source)
        else:  #46 (line in Coconut source)
            assert updated_backend is False, "invalid {_coconut_format_0}.attempt_update return value: {_coconut_format_1}".format(_coconut_format_0=(backend_cls), _coconut_format_1=(updated_backend))  #47 (line in Coconut source)

    if new_backend is None:  #49 (line in Coconut source)
        assert not _attempt_to_update_backend or isinstance(_attempt_to_update_backend, Backend), "invalid backend to attempt update on: {_coconut_format_0}".format(_coconut_format_0=(_attempt_to_update_backend))  #50 (line in Coconut source)
        new_backend = backend_cls(backend_examples, backend_params, *args, **options)  #51 (line in Coconut source)
        if _on_new_backend is not None:  #52 (line in Coconut source)
            _on_new_backend(new_backend)  #53 (line in Coconut source)

    return new_backend  #55 (line in Coconut source)



def _make_safe_backend_store(backend_store, remove_backends):  #58 (line in Coconut source)
    """Get a new backend_store without the given remove_backends."""  #59 (line in Coconut source)
    safe_backend_store = DictProxy(old_dict=backend_store, new_dict=backend_store.copy())  #60 (line in Coconut source)
    for backend_cls in backend_store:  #61 (line in Coconut source)
        if any((isinstance(rem_backend, backend_cls) for rem_backend in remove_backends)):  #62 (line in Coconut source)
            safe_specific_backends = []  #63 (line in Coconut source)
            for stored_args, stored_options, stored_backend in backend_store[backend_cls]:  #64 (line in Coconut source)
                if stored_backend not in remove_backends:  #65 (line in Coconut source)
                    safe_specific_backends.append((stored_args, stored_options, stored_backend))  #66 (line in Coconut source)
            safe_backend_store[backend_cls] = ListProxy(old_list=backend_store[backend_cls], new_list=safe_specific_backends)  #67 (line in Coconut source)
    return safe_backend_store  #68 (line in Coconut source)



@_coconut_mark_as_match  #71 (line in Coconut source)
def get_backend(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #71 (line in Coconut source)
    """Create a backend object, attempting to update a backend from backend_store."""  #72 (line in Coconut source)
    _coconut_match_check_1 = False  #73 (line in Coconut source)
    _coconut_match_set_name_backend_store = _coconut_sentinel  #73 (line in Coconut source)
    _coconut_match_set_name_backend = _coconut_sentinel  #73 (line in Coconut source)
    _coconut_match_set_name_examples = _coconut_sentinel  #73 (line in Coconut source)
    _coconut_match_set_name_params = _coconut_sentinel  #73 (line in Coconut source)
    _coconut_match_set_name_args = _coconut_sentinel  #73 (line in Coconut source)
    _coconut_match_set_name__current_backend = _coconut_sentinel  #73 (line in Coconut source)
    _coconut_match_set_name__on_new_backend = _coconut_sentinel  #73 (line in Coconut source)
    _coconut_match_set_name_options = _coconut_sentinel  #73 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #73 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #73 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #73 (line in Coconut source)
    if (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "backend_store" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "backend" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "params" in _coconut_match_kwargs)) == 1):  #73 (line in Coconut source)
        _coconut_match_set_name_args = _coconut_match_args[4:]  #73 (line in Coconut source)
        _coconut_match_temp_9 = _coconut_match_kwargs.pop("_current_backend") if "_current_backend" in _coconut_match_kwargs else None  #73 (line in Coconut source)
        _coconut_match_temp_10 = _coconut_match_kwargs.pop("_on_new_backend") if "_on_new_backend" in _coconut_match_kwargs else None  #73 (line in Coconut source)
        _coconut_match_temp_5 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("backend_store")  #73 (line in Coconut source)
        _coconut_match_temp_6 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("backend")  #73 (line in Coconut source)
        _coconut_match_temp_7 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("examples")  #73 (line in Coconut source)
        _coconut_match_temp_8 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("params")  #73 (line in Coconut source)
        _coconut_match_set_name__current_backend = _coconut_match_temp_9  #73 (line in Coconut source)
        _coconut_match_set_name__on_new_backend = _coconut_match_temp_10  #73 (line in Coconut source)
        _coconut_match_set_name_backend_store = _coconut_match_temp_5  #73 (line in Coconut source)
        _coconut_match_set_name_backend = _coconut_match_temp_6  #73 (line in Coconut source)
        _coconut_match_set_name_examples = _coconut_match_temp_7  #73 (line in Coconut source)
        _coconut_match_set_name_params = _coconut_match_temp_8  #73 (line in Coconut source)
        _coconut_match_set_name_options = _coconut_match_kwargs  #73 (line in Coconut source)
        _coconut_match_check_1 = True  #73 (line in Coconut source)
    if _coconut_match_check_1:  #73 (line in Coconut source)
        if _coconut_match_set_name_backend_store is not _coconut_sentinel:  #73 (line in Coconut source)
            backend_store = _coconut_match_set_name_backend_store  #73 (line in Coconut source)
        if _coconut_match_set_name_backend is not _coconut_sentinel:  #73 (line in Coconut source)
            backend = _coconut_match_set_name_backend  #73 (line in Coconut source)
        if _coconut_match_set_name_examples is not _coconut_sentinel:  #73 (line in Coconut source)
            examples = _coconut_match_set_name_examples  #73 (line in Coconut source)
        if _coconut_match_set_name_params is not _coconut_sentinel:  #73 (line in Coconut source)
            params = _coconut_match_set_name_params  #73 (line in Coconut source)
        if _coconut_match_set_name_args is not _coconut_sentinel:  #73 (line in Coconut source)
            args = _coconut_match_set_name_args  #73 (line in Coconut source)
        if _coconut_match_set_name__current_backend is not _coconut_sentinel:  #73 (line in Coconut source)
            _current_backend = _coconut_match_set_name__current_backend  #73 (line in Coconut source)
        if _coconut_match_set_name__on_new_backend is not _coconut_sentinel:  #73 (line in Coconut source)
            _on_new_backend = _coconut_match_set_name__on_new_backend  #73 (line in Coconut source)
        if _coconut_match_set_name_options is not _coconut_sentinel:  #73 (line in Coconut source)
            options = _coconut_match_set_name_options  #73 (line in Coconut source)
    if not _coconut_match_check_1:  #73 (line in Coconut source)
        raise _coconut_FunctionMatchError('match def get_backend(backend_store, backend, examples, params, *args, _current_backend=None, _on_new_backend=None, **options):', _coconut_match_args)  #73 (line in Coconut source)

    if isinstance(backend, type) and issubclass(backend, Backend):  #73 (line in Coconut source)
        backend_cls = backend  #74 (line in Coconut source)
    else:  #75 (line in Coconut source)
        backend_cls = backend_registry[backend]  #76 (line in Coconut source)
        assert issubclass(backend_cls, Backend), "invalid backend class for {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(backend), _coconut_format_1=(backend_cls))  #77 (line in Coconut source)

    store_ind = None  #79 (line in Coconut source)
    attempt_to_update_backend = _current_backend  #80 (line in Coconut source)
    for i, (stored_args, stored_options, stored_backend) in enumerate(backend_store[backend_cls]):  #81 (line in Coconut source)
        attempt_to_update_backend = stored_backend  #82 (line in Coconut source)
        if stored_args == args and stored_options == options:  #83 (line in Coconut source)
            store_ind = i  #84 (line in Coconut source)
            break  #85 (line in Coconut source)

    if backend_cls.request_backend_store:  #87 (line in Coconut source)
        init_options = options.copy()  #88 (line in Coconut source)
        init_options["_backend_store"] = _make_safe_backend_store(backend_store, (attempt_to_update_backend,))  #89 (line in Coconut source)
    else:  #90 (line in Coconut source)
        init_options = options  #91 (line in Coconut source)

    new_backend = _init_backend(backend_cls, examples, params, *args, _attempt_to_update_backend=attempt_to_update_backend, _on_new_backend=_on_new_backend, **init_options)  #93 (line in Coconut source)

    if store_ind is None:  #103 (line in Coconut source)
        backend_store[backend_cls].append((args, options, new_backend))  #104 (line in Coconut source)
    else:  #105 (line in Coconut source)
        backend_store[backend_cls][store_ind] = (args, options, new_backend)  #106 (line in Coconut source)

    return new_backend  #108 (line in Coconut source)



def negate_objective(objective):  #111 (line in Coconut source)
    """Take the negative of the given objective (converts a gain into a loss and vice versa)."""  #112 (line in Coconut source)
    if isinstance(objective, Iterable):  #113 (line in Coconut source)
        return (list)((map)(negate_objective, objective))  #114 (line in Coconut source)
    else:  #115 (line in Coconut source)
        return -objective  #116 (line in Coconut source)



def get_names_and_features(values, params, fallback_func=param_processor.choose_default_placeholder, converters=_coconut.dict(), convert_fallback=True,):  #119 (line in Coconut source)
    """Return an iterator of (name, feature) for the parameters in sorted order with the given fallback function.
    If passed, converters must map funcs to functions from (value, *args) -> new_value which will be run
    on the resulting value for that func (but only on fallbacks if convert_fallback)."""  #128 (line in Coconut source)
    for name, (func, args, kwargs) in sorted_items(params):  #129 (line in Coconut source)
# determine feature
        fallback = False  #131 (line in Coconut source)
        _coconut_match_to_1 = values  #132 (line in Coconut source)
        _coconut_match_check_3 = False  #132 (line in Coconut source)
        _coconut_match_set_name_feature = _coconut_sentinel  #132 (line in Coconut source)
        if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #132 (line in Coconut source)
            _coconut_match_temp_12 = _coconut_match_to_1.get(name, _coconut_sentinel)  #132 (line in Coconut source)
            if _coconut_match_temp_12 is not _coconut_sentinel:  #132 (line in Coconut source)
                _coconut_match_set_name_feature = _coconut_match_temp_12  #132 (line in Coconut source)
                _coconut_match_check_3 = True  #132 (line in Coconut source)
        if _coconut_match_check_3:  #132 (line in Coconut source)
            if _coconut_match_set_name_feature is not _coconut_sentinel:  #132 (line in Coconut source)
                feature = _coconut_match_set_name_feature  #132 (line in Coconut source)
        if _coconut_match_check_3:  #132 (line in Coconut source)
            pass  #133 (line in Coconut source)
        else:  #134 (line in Coconut source)
            _coconut_match_to_0 = kwargs  #134 (line in Coconut source)
            _coconut_match_check_2 = False  #134 (line in Coconut source)
            _coconut_match_set_name_placeholder_value = _coconut_sentinel  #134 (line in Coconut source)
            if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #134 (line in Coconut source)
                _coconut_match_temp_11 = _coconut_match_to_0.get("placeholder_when_missing", _coconut_sentinel)  #134 (line in Coconut source)
                if _coconut_match_temp_11 is not _coconut_sentinel:  #134 (line in Coconut source)
                    _coconut_match_set_name_placeholder_value = _coconut_match_temp_11  #134 (line in Coconut source)
                    _coconut_match_check_2 = True  #134 (line in Coconut source)
            if _coconut_match_check_2:  #134 (line in Coconut source)
                if _coconut_match_set_name_placeholder_value is not _coconut_sentinel:  #134 (line in Coconut source)
                    placeholder_value = _coconut_match_set_name_placeholder_value  #134 (line in Coconut source)
            if _coconut_match_check_2:  #134 (line in Coconut source)
                feature = placeholder_value  #135 (line in Coconut source)
            else:  #136 (line in Coconut source)
                fallback = True  #137 (line in Coconut source)
                feature = fallback_func(name, func, *args, **kwargs)  #138 (line in Coconut source)

# run converters
        if not fallback or convert_fallback:  #141 (line in Coconut source)
            _coconut_match_to_2 = converters  #142 (line in Coconut source)
            _coconut_match_check_4 = False  #142 (line in Coconut source)
            _coconut_match_set_name_converter_func = _coconut_sentinel  #142 (line in Coconut source)
            if _coconut.isinstance(_coconut_match_to_2, _coconut.abc.Mapping):  #142 (line in Coconut source)
                _coconut_match_temp_13 = _coconut_match_to_2.get(func, _coconut_sentinel)  #142 (line in Coconut source)
                if _coconut_match_temp_13 is not _coconut_sentinel:  #142 (line in Coconut source)
                    _coconut_match_set_name_converter_func = _coconut_match_temp_13  #142 (line in Coconut source)
                    _coconut_match_check_4 = True  #142 (line in Coconut source)
            if _coconut_match_check_4:  #142 (line in Coconut source)
                if _coconut_match_set_name_converter_func is not _coconut_sentinel:  #142 (line in Coconut source)
                    converter_func = _coconut_match_set_name_converter_func  #142 (line in Coconut source)
            if _coconut_match_check_4:  #142 (line in Coconut source)
                feature = converter_func(feature, *args)  #143 (line in Coconut source)

        yield name, feature  #145 (line in Coconut source)



def make_features(*args, **kwargs):  #148 (line in Coconut source)
    """Same as get_names_and_features but just yields the features."""  #149 (line in Coconut source)
    _coconut_yield_from_1 = _coconut.iter((starmap)(lambda name, feature: feature, get_names_and_features(*args, **kwargs)))  #150 (line in Coconut source)
    while True:  #150 (line in Coconut source)
        try:  #150 (line in Coconut source)
            yield _coconut.next(_coconut_yield_from_1)  #150 (line in Coconut source)
        except _coconut.StopIteration as _coconut_yield_err_0:  #150 (line in Coconut source)
            _coconut_yield_from_0 = _coconut_yield_err_0.args[0] if _coconut.len(_coconut_yield_err_0.args) > 0 else None  #150 (line in Coconut source)
            break  #150 (line in Coconut source)
    _coconut_yield_from_0  #150 (line in Coconut source)



def split_examples(examples, params, fallback_func=param_processor.choose_default_placeholder, converters=_coconut.dict(), convert_fallback=True,):  #153 (line in Coconut source)
    """Split examples into a list of data points and a list of losses with the given fallback function."""  #160 (line in Coconut source)
    data_points, losses = [], []  #161 (line in Coconut source)
    for example in examples:  #162 (line in Coconut source)

# extract values, loss
        _coconut_case_match_to_0 = example  #165 (line in Coconut source)
        _coconut_case_match_check_0 = False  #165 (line in Coconut source)
        _coconut_match_set_name_values = _coconut_sentinel  #165 (line in Coconut source)
        _coconut_match_set_name_gain = _coconut_sentinel  #165 (line in Coconut source)
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):  #165 (line in Coconut source)
            _coconut_match_temp_14 = _coconut_case_match_to_0.get("values", _coconut_sentinel)  #165 (line in Coconut source)
            _coconut_match_temp_15 = _coconut_case_match_to_0.get("gain", _coconut_sentinel)  #165 (line in Coconut source)
            if (_coconut_match_temp_14 is not _coconut_sentinel) and (_coconut_match_temp_15 is not _coconut_sentinel):  #165 (line in Coconut source)
                _coconut_match_set_name_values = _coconut_match_temp_14  #165 (line in Coconut source)
                _coconut_match_set_name_gain = _coconut_match_temp_15  #165 (line in Coconut source)
                _coconut_case_match_check_0 = True  #165 (line in Coconut source)
        if _coconut_case_match_check_0:  #165 (line in Coconut source)
            if _coconut_match_set_name_values is not _coconut_sentinel:  #165 (line in Coconut source)
                values = _coconut_match_set_name_values  #165 (line in Coconut source)
            if _coconut_match_set_name_gain is not _coconut_sentinel:  #165 (line in Coconut source)
                gain = _coconut_match_set_name_gain  #165 (line in Coconut source)
        if _coconut_case_match_check_0:  #165 (line in Coconut source)
            loss = negate_objective(gain)  #167 (line in Coconut source)
        if not _coconut_case_match_check_0:  #168 (line in Coconut source)
            _coconut_match_set_name_values = _coconut_sentinel  #168 (line in Coconut source)
            _coconut_match_set_name_loss = _coconut_sentinel  #168 (line in Coconut source)
            if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):  #168 (line in Coconut source)
                _coconut_match_temp_16 = _coconut_case_match_to_0.get("values", _coconut_sentinel)  #168 (line in Coconut source)
                _coconut_match_temp_17 = _coconut_case_match_to_0.get("loss", _coconut_sentinel)  #168 (line in Coconut source)
                if (_coconut_match_temp_16 is not _coconut_sentinel) and (_coconut_match_temp_17 is not _coconut_sentinel):  #168 (line in Coconut source)
                    _coconut_match_set_name_values = _coconut_match_temp_16  #168 (line in Coconut source)
                    _coconut_match_set_name_loss = _coconut_match_temp_17  #168 (line in Coconut source)
                    _coconut_case_match_check_0 = True  #168 (line in Coconut source)
            if _coconut_case_match_check_0:  #168 (line in Coconut source)
                if _coconut_match_set_name_values is not _coconut_sentinel:  #168 (line in Coconut source)
                    values = _coconut_match_set_name_values  #168 (line in Coconut source)
                if _coconut_match_set_name_loss is not _coconut_sentinel:  #168 (line in Coconut source)
                    loss = _coconut_match_set_name_loss  #168 (line in Coconut source)
            if _coconut_case_match_check_0:  #168 (line in Coconut source)
                pass  #169 (line in Coconut source)
        if not _coconut_case_match_check_0:  #170 (line in Coconut source)
            raise ValueError("invalid example {_coconut_format_0}".format(_coconut_format_0=(example)))  #171 (line in Coconut source)

# extract features
        features = (list)(make_features(values, params, fallback_func, converters, convert_fallback))  #174 (line in Coconut source)

# add to data_points, losses
        (data_points.append)(features)  #177 (line in Coconut source)
        (losses.append)(loss)  #178 (line in Coconut source)

    return data_points, losses  #180 (line in Coconut source)



def get_named_data_points_and_losses(examples, params, *args, **kwargs):  #183 (line in Coconut source)
    """Same as split_examples but returns named_data_points instead of data_points."""  #184 (line in Coconut source)
    data_points, losses = split_examples(examples, params, *args, **kwargs)  #185 (line in Coconut source)
    named_data_points = []  #186 (line in Coconut source)
    sorted_names = list(sorted(params))  #187 (line in Coconut source)
    for point in data_points:  #188 (line in Coconut source)
        pt_val = _coconut.dict()  #189 (line in Coconut source)
        for name, item in zip(sorted_names, point):  #190 (line in Coconut source)
            pt_val[name] = item  #191 (line in Coconut source)
        named_data_points.append(pt_val)  #192 (line in Coconut source)
    return named_data_points, losses  #193 (line in Coconut source)



def marginalize(named_data_points, losses, param_name, ave_func=mean):  #196 (line in Coconut source)
    """Get an average loss for each prior value of param_name."""  #197 (line in Coconut source)
    losses_for_vals = []  # we can't use a dict since vals might not be hashable  #198 (line in Coconut source)
    for point, loss in zip(named_data_points, losses):  #199 (line in Coconut source)
        val = point[param_name]  #200 (line in Coconut source)
        for check_val, check_losses in losses_for_vals:  #201 (line in Coconut source)
            if check_val == val:  #202 (line in Coconut source)
                check_losses.append(loss)  #203 (line in Coconut source)
                break  #204 (line in Coconut source)
        else:  # no break  #205 (line in Coconut source)
            losses_for_vals.append((val, [loss,]))  #206 (line in Coconut source)

    marginals = []  #208 (line in Coconut source)
    for val, all_losses in losses_for_vals:  #209 (line in Coconut source)
        marginals.append((val, ave_func(all_losses)))  #210 (line in Coconut source)
    return marginals  #211 (line in Coconut source)



def get_cum_probs_for(distribution):  #214 (line in Coconut source)
    """Generate cumulative probabilities from the given distribution."""  #215 (line in Coconut source)
    cum_probs = []  #216 (line in Coconut source)
    total_weight = sum((weight for elem, weight in distribution))  #217 (line in Coconut source)
    prev_cutoff = 0  #218 (line in Coconut source)
    for elem, weight in distribution:  #219 (line in Coconut source)
        if weight == float("inf"):  #220 (line in Coconut source)
            cutoff = 1  #221 (line in Coconut source)
        elif weight in (float("-inf"), float("nan")) or total_weight == float("nan"):  #222 (line in Coconut source)
            cutoff = prev_cutoff  #223 (line in Coconut source)
        else:  #224 (line in Coconut source)
            cutoff = prev_cutoff + weight / total_weight  #225 (line in Coconut source)
        cum_probs.append((elem, cutoff))  #226 (line in Coconut source)
        prev_cutoff = cutoff  #227 (line in Coconut source)
    return cum_probs  #228 (line in Coconut source)



def random_from_cum_probs(cum_probs):  #231 (line in Coconut source)
    """Randomly choose an element using cum_probs."""  #232 (line in Coconut source)
    rand_val = random.random()  #233 (line in Coconut source)
    for elem, cutoff in cum_probs:  #234 (line in Coconut source)
        if rand_val <= cutoff:  #235 (line in Coconut source)
            return elem  #236 (line in Coconut source)
    return None  #237 (line in Coconut source)



def make_values(params, point):  #240 (line in Coconut source)
    """Return a dictionary with the values replaced by the values in point,
    where point is a list of the values corresponding to the sorted params."""  #242 (line in Coconut source)
    values = _coconut.dict()  #243 (line in Coconut source)
    for i, k in (enumerate)((sorted)(params)):  #244 (line in Coconut source)
        values[k] = point[i]  #245 (line in Coconut source)
    return values  #246 (line in Coconut source)



def serve_values(name, func, args, kwargs, serving_values, fallback_func, backend_name=None, implemented_funcs=None, supported_kwargs=None,):  #249 (line in Coconut source)
    """Determines the parameter value to serve for the given parameter
    name and kwargs. First checks for unsupported funcs or kwargs, then
    uses the following algorithm:
    1. if name in serving_values, use serving_values[name], else
    2. if guess in kwargs, use the guess, else
    3. call fallback_func(name, func, *args, **kwargs)."""  #265 (line in Coconut source)
# validate arguments
    if implemented_funcs is not None:  #267 (line in Coconut source)
        assert backend_name is not None, "serve_values expects a backend_name argument when doing func validation"  #268 (line in Coconut source)
        if func not in implemented_funcs:  #269 (line in Coconut source)
            raise ValueError("the {_coconut_format_0} backend does not implement the {_coconut_format_1} function".format(_coconut_format_0=(backend_name), _coconut_format_1=(func)))  #270 (line in Coconut source)
    if supported_kwargs is not None:  #271 (line in Coconut source)
        assert backend_name is not None, "serve_values expects a backend_name argument when doing kwargs validation"  #272 (line in Coconut source)
        unsupported_kwargs = set(kwargs) - set(supported_kwargs)  #273 (line in Coconut source)
        if unsupported_kwargs:  #274 (line in Coconut source)
            raise ValueError("the {_coconut_format_0} backend does not support {_coconut_format_1} option(s)".format(_coconut_format_0=(backend_name), _coconut_format_1=(unsupported_kwargs)))  #275 (line in Coconut source)

# determine value
    _coconut_match_to_4 = serving_values  #278 (line in Coconut source)
    _coconut_match_check_6 = False  #278 (line in Coconut source)
    _coconut_match_set_name_value = _coconut_sentinel  #278 (line in Coconut source)
    if _coconut.isinstance(_coconut_match_to_4, _coconut.abc.Mapping):  #278 (line in Coconut source)
        _coconut_match_temp_19 = _coconut_match_to_4.get(name, _coconut_sentinel)  #278 (line in Coconut source)
        if _coconut_match_temp_19 is not _coconut_sentinel:  #278 (line in Coconut source)
            _coconut_match_set_name_value = _coconut_match_temp_19  #278 (line in Coconut source)
            _coconut_match_check_6 = True  #278 (line in Coconut source)
    if _coconut_match_check_6:  #278 (line in Coconut source)
        if _coconut_match_set_name_value is not _coconut_sentinel:  #278 (line in Coconut source)
            value = _coconut_match_set_name_value  #278 (line in Coconut source)
    if _coconut_match_check_6:  #278 (line in Coconut source)
        return value  #279 (line in Coconut source)
    else:  #280 (line in Coconut source)
        _coconut_match_to_3 = kwargs  #280 (line in Coconut source)
        _coconut_match_check_5 = False  #280 (line in Coconut source)
        _coconut_match_set_name_guess = _coconut_sentinel  #280 (line in Coconut source)
        if _coconut.isinstance(_coconut_match_to_3, _coconut.abc.Mapping):  #280 (line in Coconut source)
            _coconut_match_temp_18 = _coconut_match_to_3.get("guess", _coconut_sentinel)  #280 (line in Coconut source)
            if _coconut_match_temp_18 is not _coconut_sentinel:  #280 (line in Coconut source)
                _coconut_match_set_name_guess = _coconut_match_temp_18  #280 (line in Coconut source)
                _coconut_match_check_5 = True  #280 (line in Coconut source)
        if _coconut_match_check_5:  #280 (line in Coconut source)
            if _coconut_match_set_name_guess is not _coconut_sentinel:  #280 (line in Coconut source)
                guess = _coconut_match_set_name_guess  #280 (line in Coconut source)
        if _coconut_match_check_5:  #280 (line in Coconut source)
            return guess  #281 (line in Coconut source)
        else:  #282 (line in Coconut source)
            return fallback_func(name, func, *args, **kwargs)  #283 (line in Coconut source)


# Backend base classes:


class Backend(_coconut.object):  #288 (line in Coconut source)
    """Base class for all BBopt backends."""  #289 (line in Coconut source)
# derived classes should always set this
    backend_name = None  #291 (line in Coconut source)

# derived classes can modify these if they want to further
#  restrict the set of supported funcs and/or kwargs
    implemented_funcs = None  #295 (line in Coconut source)
    supported_kwargs = ("guess", "placeholder_when_missing")  #296 (line in Coconut source)

# derived classes must set this on each run if they want to
#  use the default param implementation
    current_values = None  #303 (line in Coconut source)

# derived classes must set this if they want to use the
#  default fallback_func implementation
    fallback_backend = None  #307 (line in Coconut source)

# derived classes can implement tell_examples(new_examples)
#  to allow fast updating on new data
    tell_examples = None  #311 (line in Coconut source)

# derived classes can set this to True to have a _backend_store keyword
#  argument passed to __init__ with an object usable in get_backend
    request_backend_store = False  #315 (line in Coconut source)

    def __new__(cls, examples=None, params=None, *args, **kwargs):  #317 (line in Coconut source)
        __class__ = Backend  #318 (line in Coconut source)

        self = super().__new__(cls)  #318 (line in Coconut source)
        if self.tell_examples is not None:  #319 (line in Coconut source)
            self._examples = examples  #320 (line in Coconut source)
            self._params = params  #321 (line in Coconut source)
            self._args = args  #322 (line in Coconut source)
            self._kwargs = kwargs  #323 (line in Coconut source)
        return self  #324 (line in Coconut source)


    def __init__(self, examples=None, params=None, *args, **kwargs):  #326 (line in Coconut source)
        """Just call attempt_update by default."""  #327 (line in Coconut source)
        self._examples = []  #328 (line in Coconut source)
        result = self.attempt_update(examples, params, *args, **kwargs)  #329 (line in Coconut source)
        assert result, "Backend.__init__: {_coconut_format_0}.attempt_update(*{_coconut_format_1}, **{_coconut_format_2}) failed with result {_coconut_format_3!r}".format(_coconut_format_0=(self.__class__.__name__), _coconut_format_1=(args), _coconut_format_2=(kwargs), _coconut_format_3=(result))  #330 (line in Coconut source)


    def attempt_update(self, examples=None, params=None, *args, **kwargs):  #332 (line in Coconut source)
        """Attempt to update this backend with new arguments. False indicates that the
        update failed while True indicates a successful update."""  #334 (line in Coconut source)
        if (self.tell_examples is None or not self._params or params != self._params or args != self._args or kwargs != self._kwargs):  #335 (line in Coconut source)
            return False  #340 (line in Coconut source)
        old_examples, new_examples = examples[:len(self._examples)], examples[len(self._examples):]  #341 (line in Coconut source)
        if old_examples != self._examples:  #342 (line in Coconut source)
            return False  #343 (line in Coconut source)
        if new_examples:  #344 (line in Coconut source)
            try:  #345 (line in Coconut source)
                self.tell_examples(new_examples)  #346 (line in Coconut source)
            except NotImplementedError:  #347 (line in Coconut source)
                return False  #348 (line in Coconut source)
        self._examples = examples  #349 (line in Coconut source)
        return True  #350 (line in Coconut source)


    def init_fallback_backend(self):  #352 (line in Coconut source)
        """Set fallback_backend to a new random backend instance."""  #353 (line in Coconut source)
        self.fallback_backend = backend_registry[constants.default_fallback_backend]()  #354 (line in Coconut source)


    def fallback_func(self, name, func, *args, **kwargs):  #356 (line in Coconut source)
        """Default fallback_func calls self.fallback_backend.param."""  #357 (line in Coconut source)
        assert self.fallback_backend is not None, "Backend subclasses using Backend.fallback_func must set fallback_backend"  #358 (line in Coconut source)
        return self.fallback_backend.param(name, func, *args, **kwargs)  #359 (line in Coconut source)


    def param(self, name, func, *args, **kwargs):  #361 (line in Coconut source)
        """Default param calls serve_values with self.current_values and self.fallback_func."""  #362 (line in Coconut source)
        assert self.current_values is not None and (isinstance)(self.current_values, dict), "Backend subclasses using Backend.param must set current_values"  #363 (line in Coconut source)
        return serve_values(name, func, args, kwargs, serving_values=self.current_values, fallback_func=self.fallback_func, backend_name=self.backend_name, implemented_funcs=self.implemented_funcs, supported_kwargs=self.supported_kwargs)  #364 (line in Coconut source)


    registered_algs = None  #376 (line in Coconut source)

    @classmethod  #378 (line in Coconut source)
    def register(cls):  #379 (line in Coconut source)
        """Register this backend to the backend registry."""  #380 (line in Coconut source)
        assert cls.backend_name is not None, "Backend subclasses using Backend.register must set backend_name on the class"  #381 (line in Coconut source)
        backend_registry.register(cls.backend_name, cls)  #382 (line in Coconut source)

# clear out registered_algs when register is called, since that
#  probably indicates a subclass is trying to register new algs
        cls.registered_algs = []  #386 (line in Coconut source)


    @classmethod  #388 (line in Coconut source)
    def register_alias(cls, alias):  #389 (line in Coconut source)
        """Register an alias for this backend."""  #390 (line in Coconut source)
        assert cls.backend_name is not None, "Backend subclasses using Backend.register_alias must set backend_name on the class"  #391 (line in Coconut source)
        backend_registry.register_alias(cls.backend_name, alias)  #392 (line in Coconut source)


    @classmethod  #394 (line in Coconut source)
    def register_alg(cls, alg_name, **options):  #395 (line in Coconut source)
        """Register an algorithm under the given name that calls this backend with the given options."""  #396 (line in Coconut source)
        assert cls.backend_name is not None, "Backend subclasses using Backend.register_alg must set backend_name on the class"  #397 (line in Coconut source)
        alg_registry.register(alg_name, (cls.backend_name, options))  #398 (line in Coconut source)

        assert cls.registered_algs is not None, "Backend.register_alg must come after Backend.register"  #400 (line in Coconut source)
        cls.registered_algs.append(alg_name)  #401 (line in Coconut source)


    @classmethod  #403 (line in Coconut source)
    def register_meta_for_all_algs(cls, alg_name, meta_alg=constants.default_alg_sentinel):  #404 (line in Coconut source)
        """Register a meta algorithm for all the algs registered on this class."""  #405 (line in Coconut source)
        assert cls.registered_algs is not None, "register_meta_for_all_algs requires prior register_alg calls"  #406 (line in Coconut source)
        cls.register_meta(alg_name, cls.registered_algs, meta_alg)  #407 (line in Coconut source)


    @staticmethod  #409 (line in Coconut source)
    def register_meta(alg_name, algs, meta_alg=constants.default_alg_sentinel):  #410 (line in Coconut source)
        """Register an algorithm that defers to run_meta."""  #411 (line in Coconut source)
        meta_registry.register(alg_name, (algs, meta_alg))  #412 (line in Coconut source)


    @staticmethod  #414 (line in Coconut source)
    def register_param_func(func_name, handler, placeholder_generator, support_check_func):  #415 (line in Coconut source)
        """Register a new parameter definition function. See bbopt.params for examples."""  #416 (line in Coconut source)
        param_processor.register(func_name, handler, placeholder_generator, support_check_func)  #417 (line in Coconut source)



_coconut_call_set_names(Backend)  #420 (line in Coconut source)
class StandardBackend(Backend):  #420 (line in Coconut source)
    """Base class for standard BBopt backends."""  #421 (line in Coconut source)

    def __init__(self, examples, params, *args, **kwargs):  #423 (line in Coconut source)
        """Implement __init__ using setup_backend and tell_examples."""  #424 (line in Coconut source)
        self.init_fallback_backend()  #425 (line in Coconut source)

        if not params:  #427 (line in Coconut source)
            self.current_values = _coconut.dict()  #428 (line in Coconut source)
            return  #429 (line in Coconut source)

        self.setup_backend(params, *args, **kwargs)  #431 (line in Coconut source)

        if examples:  #433 (line in Coconut source)
            self.tell_examples(examples)  #434 (line in Coconut source)
        else:  #435 (line in Coconut source)
            self.current_values = _coconut.dict()  #436 (line in Coconut source)


    @override  #438 (line in Coconut source)
    def tell_examples(self, new_examples):  #439 (line in Coconut source)
        """Implements tell_examples by calling tell_data."""  #440 (line in Coconut source)
        new_data, new_losses = get_named_data_points_and_losses(new_examples, self._params)  #441 (line in Coconut source)
        self.tell_data(new_data, new_losses)  #442 (line in Coconut source)
        self.current_values = self.get_next_values()  #443 (line in Coconut source)


    def setup_backend(self, params, *args, **kwargs):  #445 (line in Coconut source)
        """Override setup_backend with any setup work that needs to be done."""  #446 (line in Coconut source)
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.__init__ must define a setup_backend(params, *args, **kwargs) method")  #447 (line in Coconut source)


    def tell_data(self, new_data, new_losses):  #449 (line in Coconut source)
        """Override tell_data with any work that needs to be done to add the given data and losses."""  #450 (line in Coconut source)
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.tell_examples must define a tell_data(new_data, new_losses) method")  #451 (line in Coconut source)


    def get_next_values(self):  #453 (line in Coconut source)
        """Override get_next_values to produce the next set of values that should be evaluated."""  #454 (line in Coconut source)
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.tell_examples must define a get_next_values() method")  #455 (line in Coconut source)


_coconut_call_set_names(StandardBackend)  #457 (line in Coconut source)
