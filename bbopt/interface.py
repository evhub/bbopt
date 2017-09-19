#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x120892a5

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
The interface into bbopt for a file with black-box parameters.
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

from bbopt.backends import init_backend
from bbopt.util import norm_path
from bbopt.util import is_str
from bbopt.util import json_serialize
from bbopt.constants import default_backend
from bbopt.constants import data_file_ext

# Interface:

class BlackBoxOptimizer(_coconut.object):
    _optimizers_by_file = {}  # all Optimizer instances by file

    def __init__(self, file):
        if not is_str(file):
            raise TypeError("file must be a string")
        self._file = norm_path(file)
        if self._file in self._optimizers_by_file:
            raise ValueError("BlackBox instance for file %r already exists" % self.file)
        self._optimizers_by_file[self._file] = self
        self.reset()

    def reset(self):
        """Reset to allow another run."""
        self._old_params = {}
        self._examples = []
        self._load_examples()
        self.run(default_backend)
        self._new_params = {}
        self._current_example = {"values": {}}

    def run(self, backend, **kwargs):
        """Optimize parameters using the given backend."""
        self._backend = init_backend(backend, self._examples, self._old_params, **kwargs)

    def param(self, name, **kwargs):
        """Create a black box parameter and return its value."""
        if self._current_example is None:
            raise ValueError("param calls must come before maximize/minimize")
        if not is_str(name):
            raise TypeError("name must be a string")
        if name in self._new_params:
            raise ValueError("parameter of name %r already exists" % name)
        kwargs = (json_serialize)(kwargs)
        value = (json_serialize)(self._backend.param(name, **kwargs))
        self._new_params[name] = kwargs
        self._current_example["values"][name] = value
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

    @property
    def _data_file(self):
        return os.path.splitext(self._file)[0] + data_file_ext

    def _load_examples(self):
        """Load example data."""
        if os.path.exists(self._data_file):
            with open(self._data_file, "r") as df:
                contents = df.read()
                if contents:
                    _coconut_match_check = False
                    _coconut_match_to = json.loads(contents)
                    _coconut_sentinel = _coconut.object()
                    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
                        _coconut_match_temp_0 = _coconut_match_to.get("params", _coconut_sentinel)
                        _coconut_match_temp_1 = _coconut_match_to.get("examples", _coconut_sentinel)
                        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                            params = _coconut_match_temp_0
                            examples = _coconut_match_temp_1
                            _coconut_match_check = True
                    if not _coconut_match_check:
                        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"params": params, "examples": examples} = json.loads(contents)\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
                        _coconut_match_err.pattern = '{"params": params, "examples": examples} = json.loads(contents)'
                        _coconut_match_err.value = _coconut_match_to
                        raise _coconut_match_err

                    self._old_params = params
                    self._examples = examples

    @property
    def _json_data(self):
        return {"params": self._new_params, "examples": self._examples}

    def _save_examples(self):
        """Save example data."""
        self._load_examples()
        if self._current_example not in self._examples:
            self._examples.append(self._current_example)
        with open(self._data_file, "w+") as df:
            (df.write)((str)((json.dumps)(self._json_data)))
        self._current_example = None
