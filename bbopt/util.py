#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xece4a3d2

# Compiled with Coconut version 1.5.0-post_dev91 [Fish License]

"""
Utilities for use across all of bbopt.
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
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import os
sys = _coconut_sys
if _coconut_sys.version_info < (3, 3):
    from collections import Mapping
else:
    from collections.abc import Mapping
if _coconut_sys.version_info < (3, 3):
    from collections import Iterable
else:
    from collections.abc import Iterable
from contextlib import contextmanager
from functools import wraps

import numpy as np
from portalocker import Lock

from bbopt import constants


Num = (int, float)
Str = (str, py_str)


def norm_path(path):
    """Normalize the given path."""
    return ((os.path.normcase)((os.path.realpath)((os.path.abspath)((os.path.expanduser)(path)))))


def isnumpy(obj):
    """Determines if obj is a numpy scalar."""
    return type(obj).__module__ == "numpy" and np.isscalar(obj)


def denumpy(obj, fallback=None):
    """Convert numpy data types to their Python equivalents."""
# the ordering here is extremely important; float must
#  come before int and int must come before bool
    if np.issubdtype(obj, np.complexfloating):
        return complex(obj)
    if np.issubdtype(obj, np.floating):
        return float(obj)
    if np.issubdtype(obj, np.signedinteger) or np.issubdtype(obj, np.unsignedinteger):
        return int(obj)
    if np.issubdtype(obj, np.bool_):
        return bool(obj)
    if np.issubdtype(obj, np.str_) or np.issubdtype(obj, np.unicode_):
        return str(obj)
    if fallback is not None:
        fallback()
    return obj


def denumpy_all(obj):
    """Recursively apply denumpy to the given obj."""
    if isinstance(obj, (list, tuple)):
        return (fmap)(denumpy_all, obj)
    elif isinstance(obj, dict):
        return dict(((denumpy_all(k)), (denumpy_all(v))) for k, v in obj.items())
    elif isnumpy(obj):
        return denumpy(obj)
    else:
        return obj


def json_serialize(obj):
    """Serialize obj for encoding in JSON."""
    if obj is None or isinstance(obj, (int, float, bool, str)):
        return obj
    if isinstance(obj, bytes):
        return str(obj, encoding="utf-8")
    if isinstance(obj, Mapping):
        serialized_dict = {}
        for k, v in obj.items():
            serialized_k = json_serialize(k)
            if not isinstance(serialized_k, str):
                raise TypeError("dict keys must be strings, not {_coconut_format_0}".format(_coconut_format_0=(k)))
            serialized_dict[k] = json_serialize(v)
        return serialized_dict
    if isinstance(obj, Iterable):
        serialized_list = []
        for x in obj:
            serialized_list.append(json_serialize(x))
        return serialized_list
    if isnumpy(obj):
        def _coconut_lambda_0(_=None):
            raise TypeError("cannot JSON serialize numpy dtype {_coconut_format_0}".format(_coconut_format_0=(obj.dtype)))
        return denumpy(obj, fallback=(_coconut_lambda_0))
    raise TypeError("cannot JSON serialize {_coconut_format_0}".format(_coconut_format_0=(obj)))


def sorted_items(params):
    """Return an iterator of the dict's items sorted by its keys."""
    return sorted(params.items())


def sorted_examples(examples):
    """Sort examples by their timestamp."""
    return sorted(examples, key=_coconut.operator.itemgetter(("timestamp")))


def running_best(examples):
    """Yield running best examples seen at each point."""
    best_example = max_gain = min_loss = None
    for example in examples:

        _coconut_case_match_to_0 = example
        _coconut_case_match_check_0 = False
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_case_match_to_0.get("values", _coconut_sentinel)
            _coconut_match_temp_1 = _coconut_case_match_to_0.get("gain", _coconut_sentinel)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                values = _coconut_match_temp_0
                gain = _coconut_match_temp_1
                _coconut_case_match_check_0 = True
        if _coconut_case_match_check_0:
            if min_loss is not None:
                raise ValueError("cannot have examples with maximize and examples with minimize")
            if max_gain is None or gain >= max_gain:
                best_example = example
                max_gain = gain

        if not _coconut_case_match_check_0:
            if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_case_match_to_0.get("values", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_case_match_to_0.get("loss", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    values = _coconut_match_temp_0
                    loss = _coconut_match_temp_1
                    _coconut_case_match_check_0 = True
            if _coconut_case_match_check_0:
                if max_gain is not None:
                    raise ValueError("cannot have examples with maximize and examples with minimize")
                if min_loss is None or loss <= min_loss:
                    best_example = example
                    min_loss = loss

        if not _coconut_case_match_check_0:
            raise ValueError("invalid example {_coconut_format_0}".format(_coconut_format_0=(example)))

        yield best_example


def best_example(examples):
    """Return the best example seen so far."""
    best = consume(running_best(examples), keep_last=1)
    if best:
        assert len(best) == 1, "{_coconut_format_0} != 1".format(_coconut_format_0=(len(best)))
        return best[0]
    else:
        return {"values": {}}


def all_isinstance(objs, types):
    """Return whether all the objects have the desired type(s)."""
    return (all)((map)(_coconut_partial(isinstance, {1: types}, 2), objs))


def format_err(Error, message, obj):
    """Creates an error with a formatted error message."""
    return Error(message + ": " + repr(obj))


def sync_file(file_handle):
    """Forcibly flush and sync the given file."""
    file_handle.flush()
    os.fsync(file_handle.fileno())


def ensure_file(fpath):
    """Ensure that the given file exists."""
    if sys.version_info >= (3,):
        try:
            with open(fpath, "x"):
                pass
        except FileExistsError:
            pass
    else:
        with open(fpath, "a"):
            pass


def clear_file(file_handle):
    """Empties the contents of the given file."""
    file_handle.seek(0)
    file_handle.truncate()


def plot(xs, ys, ax=None, yscale=None, title=None, xlabel=None, ylabel=None, marker=".", markersize=12, linewidth=2, grid=True,):
    """Construct a matplotlib plot with the given parameters."""
    if ax is None:
        from matplotlib import pyplot as plt
        ax = plt.gca()
    if title is not None:
        ax.set_title(title)
    if xlabel is not None:
        ax.set_xlabel(xlabel)
    if ylabel is not None:
        ax.set_ylabel(ylabel)
    if grid:
        ax.grid()
    if yscale is not None:
        ax.set_yscale(yscale)
    ax.plot(xs, ys, marker=marker, markersize=markersize, linewidth=linewidth)
    return ax


@contextmanager
def open_with_lock(fpath, mode="rb+", timeout=None, **kwargs):
    """Open file with lock."""
    if timeout is None:
        timeout = constants.lock_timeout
    with Lock(fpath, mode, timeout=timeout, **kwargs) as file_handle:
        try:
            yield file_handle
        finally:
            file_handle.flush()
            if "w" in mode or "+" in mode or "a" in mode:
                try:
                    os.fsync(file_handle.fileno())
                except OSError:
                    pass


def convert_match_errors(func):
    """Re-raise MatchErrors as TypeErrors."""
    @wraps(func)
    def match_errors_converted_func(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except MatchError as err:
            func_name = getattr(func, "__qualname__", func.__name__)
            _coconut_raise_from_0 = TypeError("arguments did not match call signature for function {_coconut_format_0}".format(_coconut_format_0=(func_name)))
            _coconut_raise_from_0.__cause__ = err
            raise _coconut_raise_from_0
    return match_errors_converted_func


def printerr(*args):
    """Print to stderr."""
    print(*args, file=sys.stderr)


class ListProxy(_coconut.object):
    """Behaves like new_list, but appends new elements to old_list."""

    def __init__(self, old_list, new_list):
        self.old_list = old_list
        self.new_list = new_list

    def __iter__(self):
        _coconut_yield_from_1 = _coconut.iter(self.new_list)
        while True:
            try:
                yield _coconut.next(_coconut_yield_from_1)
            except _coconut.StopIteration as _coconut_yield_err_0:
                _coconut_yield_from_0 = _coconut_yield_err_0.args[0] if _coconut.len(_coconut_yield_err_0.args) > 0 else None
                break

        _coconut_yield_from_0

    def __getitem__(self, index):
        return self.new_list[index]

    def append(self, obj):
        self.new_list.append(obj)
        if obj not in self.old_list:
            self.old_list.append(obj)

    def __setitem__(self, index, obj):
        self.new_list[index] = obj
        if obj not in self.old_list:
            self.old_list.append(obj)

    def __repr__(self):
        return "ListProxy(\n\tself.old_list={_coconut_format_0},\n\tself.new_list={_coconut_format_1},\n)".format(_coconut_format_0=(self.old_list), _coconut_format_1=(self.new_list))


_coconut_call_set_names(ListProxy)
class DictProxy(_coconut.object):
    """Behaves like new_dict, but adds new keys to old_dict."""

    def __init__(self, old_dict, new_dict):
        self.old_dict = old_dict
        self.new_dict = new_dict

    def __iter__(self):
        _coconut_yield_from_3 = _coconut.iter(self.new_dict)
        while True:
            try:
                yield _coconut.next(_coconut_yield_from_3)
            except _coconut.StopIteration as _coconut_yield_err_1:
                _coconut_yield_from_2 = _coconut_yield_err_1.args[0] if _coconut.len(_coconut_yield_err_1.args) > 0 else None
                break

        _coconut_yield_from_2

    def items(self):
        return self.new_dict.items()

    def keys(self):
        return self.new_dict.keys()

    def values(self):
        return self.new_dict.values()

    def __getitem__(self, key):
        value = self.new_dict[key]
        if key not in self.old_dict:
            self.old_dict[key] = value
        return value

    def __setitem__(self, key, value):
        self.new_dict[key] = value
        if key not in self.old_dict:
            self.old_dict[key] = value

    def __repr__(self):
        return "DictProxy(\n\tself.old_dict={_coconut_format_0},\n\tself.new_dict={_coconut_format_1},\n)".format(_coconut_format_0=(self.old_dict), _coconut_format_1=(self.new_dict))


_coconut_call_set_names(DictProxy)
@_coconut_mark_as_match
def mean(*_coconut_match_args, **_coconut_match_kwargs):
    _coconut_match_check_0 = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_args) == 1) and (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) >= 0):
        xs = _coconut.list(_coconut_match_args[0])
        if not _coconut_match_kwargs:
            _coconut_match_check_0 = True
    if not _coconut_match_check_0:
        raise _coconut_FunctionMatchError('match def mean([] + xs) =', _coconut_match_args)

    return sum(xs) / len(xs)

@_coconut_addpattern(mean)
@_coconut_mark_as_match
def mean(*_coconut_match_args, **_coconut_match_kwargs):
    """Compute the arithmetic mean of the given sequence."""
    _coconut_match_check_1 = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.len(_coconut_match_args) == 1) and (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Iterable)):
        xs = _coconut_match_args[0]
        if not _coconut_match_kwargs:
            _coconut_match_check_1 = True
    if not _coconut_match_check_1:
        raise _coconut_FunctionMatchError('addpattern def mean(() :: xs) =', _coconut_match_args)

    return (mean)((tuple)(xs))


def median(xs):
    """Compute the median of the given sequence."""
    sorted_xs = (tuple)((sorted)(xs))
    return mean((sorted_xs[len(sorted_xs) // 2], sorted_xs[(len(sorted_xs) + 1) // 2],))
