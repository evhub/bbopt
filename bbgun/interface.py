#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb80a97ab

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



# Imports:

import json
import os.path

from bbgun.backends import init_backend
from bbgun.util import norm_path
from bbgun.constants import default_backend
from bbgun.constants import data_file_ext

# Interface:

class BB(_coconut.object):
    _bbs_by_file = {}  # all BB instances by file

    def __init__(self, file):
        if not isinstance(file, str):
            raise TypeError("file must be a string")
        self._file = norm_path(file)
        if self._file in self._bbs_by_file:
            raise ValueError("BB instance for file %r already exists" % self.file)
        self._bbs_by_file[self._file] = self
        self.reset()

    def reset(self):
        """Reset to allow another run."""
        self._load_examples()
        self._backend = init_backend(default_backend, self.examples)
        self._params = {}
        self._current_example = {"params": {}}

    def param(self, name, *args, **kwargs):
        """Create a black box parameter and return its value."""
        if self._current_example is None:
            raise ValueError("param calls must come before maximize/minimize")
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if name in self._params:
            raise ValueError("parameter of name %r already exists" % name)
        value = self._backend.param(name, *args, **kwargs)
        self._current_example["params"][name] = value
        return value

    def maximize(self, value):
        """Set the gain of the current run."""
        if self._current_example is None:
            raise ValueError("only one of maximize/minimize may be used")
        if callable(value):
            value = value()
        self._current_example["gain"] = value
        self._save_examples()

    def minimize(self, value):
        """Set the loss of the current run."""
        if self._current_example is None:
            raise ValueError("only one of maximize/minimize may be used")
        if callable(value):
            value = value()
        self._current_example["loss"] = value
        self._save_examples()

    def run(self, backend):
        """Optimize parameters using the given backend."""
        self._backend = init_backend(backend, self.examples)

    @property
    def _data_file(self):
        return os.path.splitext(self._file)[0] + data_file_ext

    def _load_examples(self):
        """Load example data."""
        if os.path.exists(self._data_file):
            with open(self._data_file, "r") as df:
                contents = df.read()
                if contents:
                    self.examples = json.loads(contents)
                else:
                    self.examples = []
        else:
            self.examples = []

    def _save_examples(self):
        """Save example data."""
        if self._current_example not in self.examples:
            self.examples.append(self._current_example)
        self._current_example = None
        with open(self._data_file, "w+") as df:
            json.dump(self.examples, df)
