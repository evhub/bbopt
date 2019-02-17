#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x87a4db7c

# Compiled with Coconut version 1.4.0-post_dev7 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
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


def get_nums(inputstr, numtype=float):
    """Get only the lines that are numbers."""
    for line in inputstr.splitlines():
        try:
            yield numtype(line.strip())
        except ValueError:
            pass


# Constants:

example_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")

random_file = os.path.join(example_dir, "random_example.py")
random_data = os.path.join(example_dir, "random_example.bbopt.pickle")

skopt_file = os.path.join(example_dir, "skopt_example.py")
skopt_data = os.path.join(example_dir, "skopt_example.bbopt.pickle")

hyperopt_file = os.path.join(example_dir, "hyperopt_example.py")
hyperopt_data = os.path.join(example_dir, "hyperopt_example.bbopt.pickle")

conditional_file = os.path.join(example_dir, "conditional_hyperopt_example.py")
conditional_data = os.path.join(example_dir, "conditional_hyperopt_example.bbopt.pickle")

conditional_skopt_file = os.path.join(example_dir, "conditional_skopt_example.py")
conditional_skopt_data = os.path.join(example_dir, "conditional_skopt_example.bbopt.pickle")

numpy_file = os.path.join(example_dir, "numpy_example.py")
numpy_data = os.path.join(example_dir, "numpy_example.bbopt.pickle")

json_file = os.path.join(example_dir, "json_example.py")
json_data = os.path.join(example_dir, "json_example.bbopt.json")


# Tests:

class TestExamples(unittest.TestCase):

    def test_random(self):
        print("\ntest_random:")
        with remove_when_done(random_data):
            results = call_test(["bbopt", random_file, "-n", "15"])
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(random_data)
            from bbopt.examples.random_example import x as got_x
            assert got_x == want

    def test_skopt(self):
        print("\ntest_skopt:")
        with remove_when_done(skopt_data):
            results = call_test(["bbopt", skopt_file, "-n", "15", "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(skopt_data)
            from bbopt.examples.skopt_example import y as got
            assert got == want

    def test_hyperopt(self):
        print("\ntest_hyperopt:")
        with remove_when_done(hyperopt_data):
            results = call_test(["bbopt", hyperopt_file, "-n", "15", "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(hyperopt_data)
            from bbopt.examples.hyperopt_example import y as got
            assert got == want

    def test_conditional(self):
        print("\ntest conditional:")
        with remove_when_done(conditional_data):
            results = call_test(["bbopt", conditional_file, "-n", "15", "-j", "4"])
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(conditional_data)
            from bbopt.examples.conditional_hyperopt_example import x as got
            assert got == want

    def test_conditional_skopt(self):
        print("\ntest conditional_skopt:")
        with remove_when_done(conditional_skopt_data):
            results = call_test(["bbopt", conditional_skopt_file, "-n", "15", "-j", "4"])
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(conditional_skopt_data)
            from bbopt.examples.conditional_skopt_example import x as got
            assert got == want

    def test_numpy(self):
        print("\ntest numpy:")
        with remove_when_done(numpy_data):
            results = call_test(["bbopt", numpy_file, "-n", "15", "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(numpy_data)
            from bbopt.examples.numpy_example import y as got
            assert got == want

    def test_json(self):
        print("\ntest json:")
        with remove_when_done(json_data):
            results = call_test(["bbopt", json_file, "-n", "15", "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(json_data)
            from bbopt.examples.json_example import y as got
            assert got == want
