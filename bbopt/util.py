#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa3b8501b

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

# Functions:

def is_str(obj):
    return isinstance(obj, (str, py_str))

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

def values_sorted_by_keys(params):
    """Return an iterator of the dict's values sorted by its keys."""
    for _, v in sorted(params.items()):
        yield v

def split_examples(examples):
    """Split examples into a list of data points, a list of objectives, and whether minimizing (True), maximizing (False), or no data (None)."""
    data_points, objectives, minimizing = [], [], None
    for example in examples:
        _coconut_match_to = example
        _coconut_match_check = False
        _coconut_sentinel = _coconut.object()
        if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
            _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
            _coconut_match_temp_1 = _coconut_match_to.get("gain", _coconut_sentinel)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                values = _coconut_match_temp_0
                gain = _coconut_match_temp_1
                _coconut_match_check = True
        if _coconut_match_check:
            if minimizing is True:
                raise ValueError("cannot have examples with maximize and examples with minimize")
            minimizing = False
            data_points.append((list)((values_sorted_by_keys)(values)))
            objectives.append(gain)
        if not _coconut_match_check:
            _coconut_sentinel = _coconut.object()
            if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
                _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_match_to.get("loss", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    values = _coconut_match_temp_0
                    loss = _coconut_match_temp_1
                    _coconut_match_check = True
            if _coconut_match_check:
                if minimizing is False:
                    raise ValueError("cannot have examples with maximize and examples with minimize")
                minimizing = True
                data_points.append((list)((values_sorted_by_keys)(values)))
                objectives.append(loss)
        if not _coconut_match_check:
            raise ValueError("invalid example %r" % example)
    return data_points, objectives, minimizing

def replace_values(params, point):
    """Return a dictionary with the values replaced."""
    values = {}
    for i, (k, _) in enumerate(sorted(params.items())):
        values[k] = point[i]
    return values
