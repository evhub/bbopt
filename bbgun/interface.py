#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x131ab6c4

# Compiled with Coconut version 1.3.0-post_dev2 [Dead Parrot]

"""
The interface into BBGun for a file with black-box parameters.
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



from bbgun.util import is_str
from bbgun.util import is_num
from bbgun.util import norm_path

global bbs_by_file
bbs_by_file = {}

class BB(_coconut.object):
    def __init__(self, *, file=None):
        if not is_str(file):
            raise TypeError("file must be a string")
        self._file = norm_path(file)
        if self._file in bbs_by_file:
            raise ValueError("BB instance for file %r already exists" % self.file)
        bbs_by_file[self.file] = self
        self._params = {}
        self._examples = []
        self._current_example = {}
        self._backend = None
        self._load_examples()

    def param(self, *, name=None, choose=None):
        if not is_str(name):
            raise TypeError("name must be a string")
        if name in self._params:
            raise ValueError("parameter of name %r already exists" % name)
        if choose is None:
            raise TypeError("choose must be an iterable")
        self._params[name] = {"choose": choose}
        value = self._select_value(name)
        self._current_example[name] = value
        return value

    def maximize(self, *, value=None):
        if callable(value):
            value = value()
        if not is_num(value):
            raise TypeError("value must be a number")
        self._current_example["gain"] = value

    def minimize(self, *, value=None):
        if callable(value):
            value = value()
        if not is_num(value):
            raise TypeError("value must be a number")
        self._current_example["loss"] = value

    def run(self, *, backend=None):
        from bbgun.backends import get_backend
        self._backend = get_backend(backend)
