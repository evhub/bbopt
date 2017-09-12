#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb5458c01

# Compiled with Coconut version 1.3.0-post_dev2 [Dead Parrot]

"""
Utilities for use across all of BBGun.
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
    if isinstance(obj, (int, float, str)):
        return obj
    elif isinstance(obj, bytes):
        return str(obj, encoding="utf-8")
    elif isinstance(obj, Mapping):
        serialized_dict = {}
        for k, v in obj.items():
            serialized_k = json_serialize(k)
            if not isinstance(serialized_k, str):
                raise TypeError("dict keys must be strings, not %r" % k)
            serialized_dict[k] = json_serialize(v)
        return serialized_dict
    elif isinstance(obj, Iterable):
        serialized_list = []
        for x in obj:
            serialized_list.append(json_serialize(x))
        return serialized_list
    else:
        raise TypeError("invalid JSON object %r" % obj)
