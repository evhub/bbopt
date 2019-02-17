#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd44f7e6d

# Compiled with Coconut version 1.4.0-post_dev7 [Ernest Scribbler]

"""
Utilities for use across all of bbopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

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

import numpy as np


Num = (int, float)
Str = (str, py_str)


def norm_path(path):
    """Normalize the given path."""
    return ((os.path.normcase)((os.path.realpath)((os.path.abspath)((os.path.expanduser)(path)))))


def json_serialize(obj):
    """Serialize obj for encoding in JSON."""
    while True:
        if obj is None or isinstance(obj, (int, float, bool, str)):
            return obj
        if isinstance(obj, bytes):
            return str(obj, encoding="utf-8")
        if isinstance(obj, Mapping):
            serialized_dict = {}
            for k, v in obj.items():
                serialized_k = json_serialize(k)
                if not isinstance(serialized_k, str):
                    raise TypeError("dict keys must be strings, not {}".format(k))
                serialized_dict[k] = json_serialize(v)
            return serialized_dict
        if isinstance(obj, Iterable):
            serialized_list = []
            for x in obj:
                serialized_list.append(json_serialize(x))
            return serialized_list
        if type(obj).__module__ == "numpy":
# the ordering here is extremely important; int must come before
#  bool, since otherwise this will cast all ints to bools
            if np.issubdtype(obj, np.number) or np.issubdtype(obj, np.unsignedinteger):
                return int(obj)
            if np.issubdtype(obj, np.floating):
                return float(obj)
            if np.issubdtype(obj, np.bool_):
                return bool(obj)
            if np.issubdtype(obj, np.str_):
                try:
                    _coconut_is_recursive = json_serialize is _coconut_recursive_func_1
                except _coconut.NameError:
                    _coconut_is_recursive = False
                if _coconut_is_recursive:
                    obj = py_str(obj)
                    continue
                else:
                    return json_serialize(py_str(obj))

        raise TypeError("cannot JSON serialize {}".format(obj))


        return None
_coconut_recursive_func_1 = json_serialize
def sorted_items(params):
    """Return an iterator of the dict's items sorted by its keys."""
    return sorted(params.items())


def negate_objective(objective):
    if isinstance(objective, list):
        return (list)(map(negate_objective, objective))
    else:
        return -objective


def make_features(values, params, fallback_func):
    """Return an iterator of the values for the parameters in sorted order with the given fallback function."""
    for name, param_kwargs in sorted_items(params):
        _coconut_match_to = values
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                feature = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            yield feature
        else:
            _coconut_match_to = param_kwargs
            _coconut_match_check = False
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get("placeholder_when_missing", _coconut_sentinel)
                if _coconut_match_temp_0 is not _coconut_sentinel:
                    placeholder_value = _coconut_match_temp_0
                    _coconut_match_check = True
            if _coconut_match_check:
                yield placeholder_value
            else:
                yield fallback_func(name, **param_kwargs)


def split_examples(examples, params, fallback_func):
    """Split examples into a list of data points and a list of losses with the given fallback function."""
    data_points, losses = [], []
    for example in examples:
        _coconut_match_to = example
        _coconut_case_check_0 = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
            _coconut_match_temp_1 = _coconut_match_to.get("gain", _coconut_sentinel)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                values = _coconut_match_temp_0
                gain = _coconut_match_temp_1
                _coconut_case_check_0 = True
        if _coconut_case_check_0:
            loss = negate_objective(gain)
        if not _coconut_case_check_0:
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_match_to.get("loss", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    values = _coconut_match_temp_0
                    loss = _coconut_match_temp_1
                    _coconut_case_check_0 = True
            if _coconut_case_check_0:
                pass
        if not _coconut_case_check_0:
            raise ValueError("invalid example {}".format(example))
        (data_points.append)((list)(make_features(values, params, fallback_func)))
        (losses.append)(loss)
    return data_points, losses


def make_values(params, point):
    """Return a dictionary with the values replaced by the values in point,
    where point is a list of the values corresponding to the sorted params."""
    values = {}
    for i, k in (enumerate)((sorted)(params)):
        values[k] = point[i]
    return values


def all_isinstance(objs, types):
    """Return whether all the objects have the desired type(s)."""
    return (all)(map(_coconut_partial(isinstance, {1: types}, 2), objs))


def format_err(Error, message, obj):
    """Creates an error with a formatted error message."""
    return Error(message + ": " + repr(obj))


def best_example(examples):
    """Return the best example seen so far."""
    selected_example = {"values": {}}
    max_gain, min_loss = None, None
    for example in examples:
        _coconut_match_to = example
        _coconut_case_check_1 = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
            _coconut_match_temp_1 = _coconut_match_to.get("gain", _coconut_sentinel)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                values = _coconut_match_temp_0
                gain = _coconut_match_temp_1
                _coconut_case_check_1 = True
        if _coconut_case_check_1:
            if min_loss is not None:
                raise ValueError("cannot have examples with maximize and examples with minimize")
            if max_gain is None or gain >= max_gain:
                selected_example = example
                max_gain = gain
        if not _coconut_case_check_1:
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_match_to.get("loss", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    values = _coconut_match_temp_0
                    loss = _coconut_match_temp_1
                    _coconut_case_check_1 = True
            if _coconut_case_check_1:
                if max_gain is not None:
                    raise ValueError("cannot have examples with maximize and examples with minimize")
                if min_loss is None or loss <= min_loss:
                    selected_example = example
                    min_loss = loss
        if not _coconut_case_check_1:
            raise ValueError("invalid example {}".format(example))
    return selected_example


def serve_values(param_name, param_kwargs, serving_values, fallback_func):
    """Determines the parameter value to serve for the given parameter
    name and kwargs. Uses the following algorithm:
    1. if param_name in serving_values, use serving_values[param_name], else
    2. if guess in param_kwargs, use the guess, else
    3. call fallback_func(param_name, **param_kwargs)."""
    _coconut_match_to = serving_values
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
        _coconut_match_temp_0 = _coconut_match_to.get(param_name, _coconut_sentinel)
        if _coconut_match_temp_0 is not _coconut_sentinel:
            value = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check:
        return value
    else:
        _coconut_match_to = param_kwargs
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get("guess", _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                guess = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            return guess
        else:
            return fallback_func(param_name, **param_kwargs)


def sync_file(file_handle):
    """Forcibly flush and sync the given file."""
    file_handle.flush()
    os.fsync(file_handle.fileno())


def ensure_file(fpath):
    """Ensure that the given file exists."""
    try:
        with open(fpath, "x" if sys.version_info >= (3,) else "a"):
            pass
    except IOError:
        pass


def clear_file(file_handle):
    """Empties the contents of the given file."""
    file_handle.seek(0)
    file_handle.truncate()
