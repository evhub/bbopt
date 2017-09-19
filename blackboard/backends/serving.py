#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc0300635

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
The serving backend. Selects the best existing data point.
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



# Backend:

class ServingBackend(_coconut.object):
    """The serving backend uses the parameter values from the best example."""

    def __init__(self, examples, params):  # ignore params since we're serving
        self.serving_values = {}
        max_gain, min_loss = None, None
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
                if min_loss is not None:
                    raise ValueError("cannot have examples with maximize and examples with minimize")
                if max_gain is None or gain >= max_gain:
                    self.serving_values = values
                    max_gain = gain
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
                    if max_gain is not None:
                        raise ValueError("cannot have examples with maximize and examples with minimize")
                    if min_loss is None or loss <= min_loss:
                        self.serving_values = values
                        min_loss = loss
            if not _coconut_match_check:
                raise ValueError("invalid example %r" % example)

    def param(self, name, **kwargs):  # ignore kwargs since we're serving
        try:
            return self.serving_values[name]
        except KeyError:
            raise ValueError("missing data for parameter %r" % name)
