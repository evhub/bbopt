#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4009dcfe

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

import os
import shutil
import traceback
import unittest
from contextlib import contextmanager

from coconut.command.util import call_output

# Utilities:

@contextmanager
def remove_when_done(path):
    """Removes a path when done."""
    try:
        yield
    finally:
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
            elif os.path.isfile(path):
                os.remove(path)
        except OSError:
            traceback.print_exc()

def call_test(args):
    """Call args on the command line for a test."""
    stdout, stderr, retcode = call_output(args)
    stdout, stderr = "".join(stdout), "".join(stderr)
    (print)((stdout + stderr).strip())
    assert not retcode and not stderr, stderr
    return stdout

# Constants:

example_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")

random_file = os.path.join(example_dir, "random_example.py")
random_data = os.path.join(example_dir, "random_example.bbopt.json")

skopt_file = os.path.join(example_dir, "skopt_example.py")
skopt_data = os.path.join(example_dir, "skopt_example.bbopt.json")

# Tests:

class TestExamples(unittest.TestCase):

    def test_random(self):
        print("\ntest_random:")
        with remove_when_done(random_data):
            want_x = -1
            for _ in range(10):
                stdout = call_test(["python", random_file])
                want_x = max(int(stdout.strip()), want_x)
            assert os.path.exists(random_data)
            from bbopt.examples.random_example import x as got_x
            assert got_x == want_x

    def test_skopt(self):
        print("\ntest_skopt:")
        with remove_when_done(skopt_data):
            want_y = float("inf")
            for _ in range(10):
                stdout = call_test(["python", skopt_file])
                want_y = min(float(stdout.strip()), want_y)
            assert os.path.exists(skopt_data)
            from bbopt.examples.skopt_example import y as got_y
            assert got_y == want_y
