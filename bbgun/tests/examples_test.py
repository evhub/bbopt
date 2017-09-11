#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xcabb01a8

# Compiled with Coconut version 1.3.0-post_dev2 [Dead Parrot]

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

import os
import unittest

from coconut.command.util import call_output

# Tests:

example_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")
example_file = os.path.join(example_dir, "test_example.py")
example_data = os.path.join(example_dir, "test_example.bbdata.json")

class TestExamples(unittest.TestCase):

    def test_example(self):
        want_x = -1
        for _ in range(10):
            stdout, stderr, retcode = call_output(["python", example_file])
            stdout, stderr = "".join(stdout), "".join(stderr)
            assert not retcode and not stderr, stderr
            want_x = max(int(stdout.strip()), want_x)
        from bbgun.examples.test_example import x as got_x
        assert got_x == want_x
        assert os.path.exists(example_data)
        os.remove(example_data)
