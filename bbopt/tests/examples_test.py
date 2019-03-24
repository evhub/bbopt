#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xbf38ee72

# Compiled with Coconut version 1.4.0-post_dev25 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel, _coconut_assert
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:

import os
sys = _coconut_sys
import shutil
import unittest
import traceback
from contextlib import contextmanager
if _coconut_sys.version_info < (3, 4):
    from imp import reload
else:
    from importlib import reload

from coconut.command.util import call_output


# Utilities:

@contextmanager
def using(path, rem_on_start=True, rem_on_end=False):
    """Removes a path when the context is started and/or ended."""
    if rem_on_start and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
    try:
        yield
    finally:
        if rem_on_end:
            try:
                if os.path.isdir(path):
                    shutil.rmtree(path)
                elif os.path.isfile(path):
                    os.remove(path)
            except OSError:
                traceback.print_exc()


always_ignore_errs = ("DeprecationWarning: numpy.core.umath_tests is an internal NumPy module", "from numpy.core.umath_tests import", "RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility.", "return f(*args, **kwds)", "UserWarning: The objective has been evaluated at this point before.", 'warnings.warn("The objective has been evaluated',)


def call_test(args, ignore_errs=(), prepend_py=True):
    """Call args on the command line for a test."""
    if prepend_py:
        args = [sys.executable, "-m"] + args
    stdout, stderr, retcode = call_output(args)
    stdout, stderr = "".join(stdout), "".join(stderr)
    (print)((stdout + stderr).strip())
    clean_stderr = []
    for line in stderr.splitlines():
        if not any((ignore in line for ignore in _coconut.itertools.chain.from_iterable((_coconut_func() for _coconut_func in (lambda: always_ignore_errs, lambda: ignore_errs))))):
            clean_stderr.append(line)
    clean_stderr = "\n".join(clean_stderr)
    assert not retcode and not clean_stderr, clean_stderr
    return stdout


def get_nums(inputstr, numtype=float):
    """Get only the lines that are numbers."""
    for line in inputstr.splitlines():
        try:
            yield numtype(line.strip())
        except ValueError:
            pass


# Constants:

NUM_TRIALS = 25

example_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")

random_file = os.path.join(example_dir, "random_example.py")
random_data = os.path.join(example_dir, "random_example.bbopt.pickle")

skopt_file = os.path.join(example_dir, "skopt_example.py")
skopt_data = os.path.join(example_dir, "skopt_example.bbopt.pickle")

hyperopt_file = os.path.join(example_dir, "hyperopt_example.py")
hyperopt_data = os.path.join(example_dir, "hyperopt_example.bbopt.pickle")

conditional_hyperopt_file = os.path.join(example_dir, "conditional_hyperopt_example.py")
conditional_hyperopt_data = os.path.join(example_dir, "conditional_hyperopt_example.bbopt.pickle")

conditional_skopt_file = os.path.join(example_dir, "conditional_skopt_example.py")
conditional_skopt_data = os.path.join(example_dir, "conditional_skopt_example.bbopt.pickle")

numpy_file = os.path.join(example_dir, "numpy_example.py")
numpy_data = os.path.join(example_dir, "numpy_example.bbopt.pickle")

mixture_file = os.path.join(example_dir, "mixture_example.py")
mixture_data = os.path.join(example_dir, "mixture_example.bbopt.pickle")

json_file = os.path.join(example_dir, "json_example.py")
json_data = os.path.join(example_dir, "json_example.bbopt.json")


# Tests:

class TestExamples(unittest.TestCase):

    def test_random(self):
        print("\ntest random:")
        with using(random_data):
            results = call_test(["bbopt", random_file, "-n", str(NUM_TRIALS)])
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(random_data)

            from bbopt.examples import random_example
            assert random_example.x == want
            assert 1 <= random_example.x <= 10
            assert random_example.bb.num_examples == NUM_TRIALS

    def test_skopt(self):
        print("\ntest skopt:")
        with using(skopt_data):
            results = call_test(["bbopt", skopt_file, "-n", str(NUM_TRIALS), "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(skopt_data)

            from bbopt.examples import skopt_example
            assert skopt_example.y == want
            assert -9 <= skopt_example.y <= 21
            assert skopt_example.bb.num_examples == NUM_TRIALS

    def test_hyperopt(self):
        print("\ntest hyperopt:")
        with using(hyperopt_data):
            results = call_test(["bbopt", hyperopt_file, "-n", str(NUM_TRIALS), "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(hyperopt_data)

            from bbopt.examples import hyperopt_example
            assert hyperopt_example.y == want
            assert hyperopt_example.bb.num_examples == NUM_TRIALS

    def test_conditional_hyperopt(self):
        print("\ntest conditional_hyperopt:")
        with using(conditional_hyperopt_data):
            results = call_test(["bbopt", conditional_hyperopt_file, "-n", str(NUM_TRIALS), "-j", "4"])
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(conditional_hyperopt_data)

            from bbopt.examples import conditional_hyperopt_example
            assert conditional_hyperopt_example.x == want
            assert 0 <= conditional_hyperopt_example.x <= 20
            assert conditional_hyperopt_example.bb.num_examples == NUM_TRIALS

    def test_conditional_skopt(self):
        print("\ntest conditional_skopt:")
        with using(conditional_skopt_data):
            results = call_test(["bbopt", conditional_skopt_file, "-n", str(NUM_TRIALS), "-j", "4"])
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(conditional_skopt_data)

            from bbopt.examples import conditional_skopt_example
            assert conditional_skopt_example.x == want
            assert 0 <= conditional_skopt_example.x <= 20
            assert conditional_skopt_example.bb.num_examples == NUM_TRIALS

    def test_numpy(self):
        print("\ntest numpy:")
        with using(numpy_data):
            from bbopt.examples import numpy_example
            assert numpy_example.y == 0

            results = call_test(["bbopt", numpy_file, "-n", str(NUM_TRIALS), "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(numpy_data)

            reload(numpy_example)
            assert numpy_example.y == want
            assert numpy_example.bb.num_examples == NUM_TRIALS

    def test_mixture(self):
        print("\ntest mixture:")
        with using(mixture_data):
            from bbopt.examples import mixture_example
            assert mixture_example.loss == abs(sum([3, 4, 5, 6, 7]) - 10)

            results = call_test(["bbopt", mixture_file, "-n", str(NUM_TRIALS), "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(mixture_data)

            reload(mixture_example)
            assert mixture_example.loss == want
            assert 0 <= mixture_example.loss <= 85
            assert mixture_example.bb.num_examples == NUM_TRIALS

    def test_json(self):
        print("\ntest json:")
        with using(json_data):
            from bbopt.examples import json_example
            assert round(json_example.y, 5) == 6

            results = call_test(["bbopt", json_file, "-n", str(NUM_TRIALS), "-j", "4"])
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(json_data)

            reload(json_example)
            assert json_example.y == want
            assert json_example.bb.num_examples == NUM_TRIALS
