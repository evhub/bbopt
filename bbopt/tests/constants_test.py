#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x49b6da1e

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

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

import unittest

from bbopt import constants

# Utilities:

def is_hashable(obj):
    """Determine if obj is hashable."""
    try:
        hash(obj)
    except Exception:
        return False
    else:
        return True


def assert_hashable_or_dict(name, obj):
    """Assert obj is hashable, or for dicts apply recursively to values."""
    if isinstance(obj, dict):
        for val in obj.values():
            assert_hashable_or_dict(name, val)
    else:
        assert is_hashable(obj), "Constant " + name + " contains unhashable values"

# Tests:

class TestConstants(unittest.TestCase):

    def test_immutable(self):
        for name, value in vars(constants).items():
            if not name.startswith("__"):
                assert not isinstance(value, list), "Constant " + name + " should be tuple, not list"
                assert not isinstance(value, set), "Constant " + name + " should be frozenset, not set"
                assert_hashable_or_dict(name, value)
