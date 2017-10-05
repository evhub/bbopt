#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x3c6fb95f

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
Utilities for use across all of bbopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



# Imports:

import os.path
if _coconut_sys.version_info < (3, 3):
    from collections import Mapping
else:
    from collections.abc import Mapping
if _coconut_sys.version_info < (3, 3):
    from collections import Iterable
else:
    from collections.abc import Iterable

# Objects:

Num = (int, float)
Str = (str, py_str)

# Functions:

def norm_path(path):
    return ((os.path.normcase)((os.path.realpath)((os.path.abspath)((os.path.expanduser)(path)))))

def json_serialize(obj):
    """Serialize obj for encoding in JSON."""
    if obj is None or isinstance(obj, (bool, int, float, str)):
        return obj
    if isinstance(obj, bytes):
        return str(obj, encoding="utf-8")
    if isinstance(obj, Mapping):
        serialized_dict = {}
        for k, v in obj.items():
            serialized_k = json_serialize(k)
            if not isinstance(serialized_k, str):
                raise TypeError("dict keys must be strings, not %r" % k)
            serialized_dict[k] = json_serialize(v)
        return serialized_dict
    if isinstance(obj, Iterable):
        serialized_list = []
        for x in obj:
            serialized_list.append(json_serialize(x))
        return serialized_list
    if type(obj).__module__ == "numpy":
        import numpy as np
        if np.issubdtype(obj, int):
            return int(obj)
        if np.issubdtype(obj, float):
            return float(obj)
        if np.issubdtype(obj, bool):
            return bool(obj)
    raise TypeError("invalid JSON object %r" % obj)

def sorted_items(params):
    """Return an iterator of the dict's items sorted by its keys."""
    return sorted(params.items())

def negate_objective(objective):
    if isinstance(objective, list):
        return (list)(map(negate_objective, objective))
    else:
        return -objective

def make_features(values, params, default_placeholder=None):
    """Return an iterator of the values for the parameters in sorted order."""
    for feature, param_kwargs in sorted_items(params):
        if feature in values:
            yield values[feature]
        elif "placeholder_when_missing" in param_kwargs:
            yield param_kwargs["placeholder_when_missing"]
        else:
            yield default_placeholder

def split_examples(examples, params, default_placeholder=None):
    """Split examples into a list of data points and a list of losses."""
    data_points, losses = [], []
    for example in examples:
        _coconut_match_to = example
        _coconut_match_check = False
        _coconut_sentinel = _coconut.object()
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
            _coconut_match_temp_1 = _coconut_match_to.get("gain", _coconut_sentinel)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                values = _coconut_match_temp_0
                gain = _coconut_match_temp_1
                _coconut_match_check = True
        if _coconut_match_check:
            loss = negate_objective(gain)
        if not _coconut_match_check:
            _coconut_sentinel = _coconut.object()
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_match_to.get("loss", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    values = _coconut_match_temp_0
                    loss = _coconut_match_temp_1
                    _coconut_match_check = True
            if _coconut_match_check:
                pass
        if not _coconut_match_check:
            raise ValueError("invalid example %r" % example)
        (data_points.append)((list)(make_features(values, params, default_placeholder)))
        (losses.append)(loss)
    return data_points, losses

def replace_values(params, point):
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
        _coconut_match_check = False
        _coconut_sentinel = _coconut.object()
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
            _coconut_match_temp_1 = _coconut_match_to.get("gain", _coconut_sentinel)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                values = _coconut_match_temp_0
                gain = _coconut_match_temp_1
                _coconut_match_check = True
        if _coconut_match_check:
            if min_loss is not None:
                raise ValueError("cannot have examples with maximize and examples with minimize")
            if max_gain is None or gain >= max_gain:
                selected_example = example
                max_gain = gain
        if not _coconut_match_check:
            _coconut_sentinel = _coconut.object()
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_match_to.get("loss", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    values = _coconut_match_temp_0
                    loss = _coconut_match_temp_1
                    _coconut_match_check = True
            if _coconut_match_check:
                if max_gain is not None:
                    raise ValueError("cannot have examples with maximize and examples with minimize")
                if min_loss is None or loss <= min_loss:
                    selected_example = example
                    min_loss = loss
        if not _coconut_match_check:
            raise ValueError("invalid example %r" % example)
    return selected_example
