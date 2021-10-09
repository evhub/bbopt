#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2ae96406

# Compiled with Coconut version 1.5.0-post_dev91 [Fish License]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == str("__coconut__"):
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
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

from bbopt.util import mean
from bbopt.util import median


# Constants:

NUM_TRIALS = 24
NUM_PROCS = 2

example_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")

random_file = os.path.join(example_dir, "random_example.py")
random_data = os.path.join(example_dir, "random_example.bbopt.pickle")

skopt_file = os.path.join(example_dir, "skopt_example.py")
skopt_data = os.path.join(example_dir, "skopt_example.bbopt.pickle")

pysot_file = os.path.join(example_dir, "pysot_example.py")
pysot_data = os.path.join(example_dir, "pysot_example.bbopt.pickle")

hyperopt_file = os.path.join(example_dir, "hyperopt_example.py")
hyperopt_data = os.path.join(example_dir, "hyperopt_example.bbopt.pickle")

conditional_hyperopt_file = os.path.join(example_dir, "conditional_hyperopt_example.py")
conditional_hyperopt_data = os.path.join(example_dir, "conditional_hyperopt_example.bbopt.pickle")

conditional_skopt_file = os.path.join(example_dir, "conditional_skopt_example.py")
conditional_skopt_data = os.path.join(example_dir, "conditional_skopt_example.bbopt.pickle")

bask_file = os.path.join(example_dir, "bask_example.py")
bask_data = os.path.join(example_dir, "bask_example.bbopt.pickle")

numpy_file = os.path.join(example_dir, "numpy_example.py")
numpy_data = os.path.join(example_dir, "numpy_example.bbopt.pickle")

meta_file = os.path.join(example_dir, "meta_example.py")
meta_data = os.path.join(example_dir, "meta_example.bbopt.pickle")

any_fast_file = os.path.join(example_dir, "any_fast_example.py")
any_fast_data = os.path.join(example_dir, "any_fast_example.bbopt.pickle")

mixture_file = os.path.join(example_dir, "mixture_example.py")
mixture_data = os.path.join(example_dir, "mixture_example.bbopt.pickle")

json_file = os.path.join(example_dir, "json_example.py")
json_data = os.path.join(example_dir, "json_example.bbopt.json")


# Utilities:

@contextmanager
def using(path, rem_on_start=True, rem_on_end=False):
    """Removes a path when the context is started and/or ended."""
    if rem_on_start and os.path.exists(path):
        if os.path.isdir(path):
            shutil.rmtree(path)
        elif os.path.isfile(path):
            os.remove(path)
        assert not os.path.exists(path), "failed to remove: {_coconut_format_0}".format(_coconut_format_0=(path))
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


always_ignore_errs = ("DeprecationWarning: numpy.core.umath_tests is an internal NumPy module", "from numpy.core.umath_tests import", "RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility.", "return f(*args, **kwds)", "UserWarning: The objective has been evaluated at this point before.", 'warnings.warn("The objective has been evaluated', "DeprecationWarning: sklearn.externals.joblib is deprecated", "warnings.warn(msg, category=DeprecationWarning)",)


def call_test(args, ignore_errs=(), prepend_py=True):
    """Call args on the command line for a test."""
    if prepend_py:
        args = [sys.executable, "-m"] + args
    print(">", " ".join(args))
    stdout, stderr, retcode = call_output(args)
    stdout, stderr = "".join(stdout), "".join(stderr)
    (print)((stdout + stderr).strip())
    clean_stderr = []
    for line in stderr.splitlines():
        if not any((ignore in line for ignore in _coconut.itertools.chain.from_iterable(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: always_ignore_errs, lambda: ignore_errs))))):
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


def middle_mean(xs):
    """Mean of the middle half of xs."""
    a, b = len(xs) // 4, 3 * len(xs) // 4
    return mean(xs[a:b])


def stdev(xs):
    """Standard deviation of xs."""
    mu = mean(xs)


    return mean(((x - mu)**2 for x in xs))**0.5
def assert_improving(data, ave_func=mean, within_stdevs=0.5):
    """Assert that the second half of data is greater/smaller than the first."""
    examples = data["examples"]
    assert len(examples) >= 2, data
    half_pt = len(examples) // 2
    first_half, second_half = examples[:half_pt], examples[half_pt:]
    if "loss" in first_half[0]:
        ave_func = min if ave_func is None else ave_func
        first_losses = (map)(_coconut.operator.itemgetter(("loss")), first_half)
        second_losses = (map)(_coconut.operator.itemgetter(("loss")), second_half)

        first_ave_loss = ave_func(first_losses)
        second_ave_loss = ave_func(second_losses)
        first_stdev = stdev(first_losses)
        assert second_ave_loss - first_ave_loss < first_stdev * within_stdevs
    else:
        ave_func = max if ave_func is None else ave_func
        first_gains = (map)(_coconut.operator.itemgetter(("gain")), first_half)
        second_gains = (map)(_coconut.operator.itemgetter(("gain")), second_half)

        first_ave_gain = ave_func(first_gains)
        second_ave_gain = ave_func(second_gains)
        first_stdev = stdev(first_gains)
        assert second_ave_gain - first_ave_gain > -first_stdev * within_stdevs


def call_bbopt(fpath, trials=NUM_TRIALS, procs=NUM_PROCS):
    """Call bbopt on the given file."""
    cmd = ["bbopt", fpath]
    if trials is not None:
        cmd += ["-n", str(trials)]
    if procs is not None:
        cmd += ["-j", str(procs)]
    return call_test(cmd)


# Tests:

class TestExamples(unittest.TestCase):

    def test_random(self):
        print("\ntest random:")
        with using(random_data):
            results = call_bbopt(random_file, procs=1)
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(random_data)

            from bbopt.examples import random_example
            random_example.bb.get_data(print_data=True)
            assert random_example.x == want
            assert 1 < random_example.x <= 10
            assert random_example.bb.num_examples == NUM_TRIALS

    def test_skopt(self):
        print("\ntest skopt:")
        with using(skopt_data):
            results = call_bbopt(skopt_file)
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(skopt_data)

            from bbopt.examples import skopt_example
            assert_improving(skopt_example.bb.get_data(print_data=True), ave_func=middle_mean)
            assert skopt_example.y == want
            assert -9 <= skopt_example.y < 21
            assert skopt_example.bb.num_examples == NUM_TRIALS

    def test_conditional_skopt(self):
        print("\ntest conditional_skopt:")
        with using(conditional_skopt_data):
            results = call_bbopt(conditional_skopt_file)
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(conditional_skopt_data)

            from bbopt.examples import conditional_skopt_example
            assert_improving(conditional_skopt_example.bb.get_data(print_data=True))
            assert conditional_skopt_example.x == want
            assert 0 < conditional_skopt_example.x <= 20
            assert conditional_skopt_example.bb.num_examples == NUM_TRIALS

    if sys.version_info >= (3, 7):
        def test_bask(self):
            print("\ntest bask:")
            with using(bask_data):
                results = call_bbopt(bask_file)
                want = max(get_nums(results, numtype=float))
                assert os.path.exists(bask_data)

                from bbopt.examples import bask_example
                assert_improving(bask_example.bb.get_data(print_data=True), ave_func=median)
                assert 0 < want <= 20
                assert 0 < bask_example.x <= 20
                assert bask_example.bb.num_examples == NUM_TRIALS

    if sys.version_info >= (3,):
        def test_pysot(self):
            print("\ntest pysot:")
            with using(pysot_data):
                results = call_bbopt(pysot_file, trials=2)
                want = min(get_nums(results, numtype=float))
                assert os.path.exists(pysot_data)

                from bbopt.examples import pysot_example
                assert_improving(pysot_example.bb.get_data(print_data=True))
                assert pysot_example.best_y == want
                assert -9 <= pysot_example.best_y < 21
                assert pysot_example.bb.num_examples == 20

    def test_hyperopt(self):
        print("\ntest hyperopt:")
        with using(hyperopt_data):
            results = call_bbopt(hyperopt_file)
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(hyperopt_data)

            from bbopt.examples import hyperopt_example
            assert_improving(hyperopt_example.bb.get_data(print_data=True), ave_func=None)
            assert hyperopt_example.y == want
            assert hyperopt_example.bb.num_examples == NUM_TRIALS

    def test_conditional_hyperopt(self):
        print("\ntest conditional_hyperopt:")
        with using(conditional_hyperopt_data):
            results = call_bbopt(conditional_hyperopt_file)
            want = max(get_nums(results, numtype=int))
            assert os.path.exists(conditional_hyperopt_data)

            from bbopt.examples import conditional_hyperopt_example
            assert_improving(conditional_hyperopt_example.bb.get_data(print_data=True))
            assert conditional_hyperopt_example.x == want
            assert 0 < conditional_hyperopt_example.x <= 20
            assert conditional_hyperopt_example.bb.num_examples == NUM_TRIALS

    def test_numpy(self):
        print("\ntest numpy:")
        with using(numpy_data):
            from bbopt.examples import numpy_example
            assert numpy_example.y == 0

            results = call_bbopt(numpy_file)
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(numpy_data)

            reload(numpy_example)
            assert_improving(numpy_example.bb.get_data(print_data=True))
            assert numpy_example.y == want
            assert numpy_example.bb.num_examples == NUM_TRIALS

    def test_meta(self):
        print("\ntest meta:")
        with using(meta_data):
            results = call_bbopt(meta_file)
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(meta_data)

            from bbopt.examples import meta_example
            assert_improving(meta_example.bb.get_data(print_data=True))
            assert meta_example.u == want
            assert 0 <= meta_example.u < 1
            assert meta_example.bb.num_examples == NUM_TRIALS

    def test_any_fast(self):
        print("\ntest any_fast:")
        with using(any_fast_data):
            results = call_bbopt(any_fast_file)

            want = min(get_nums(results, numtype=float))
            assert os.path.exists(any_fast_data)

            from bbopt.examples import any_fast_example
            assert_improving(any_fast_example.bb.get_data(print_data=True), ave_func=None)
            assert any_fast_example.u == want
            assert any_fast_example.u < 1
            assert any_fast_example.bb.num_examples == NUM_TRIALS

    def test_mixture(self):
        print("\ntest mixture:")
        with using(mixture_data):
            from bbopt.examples import mixture_example
            assert mixture_example.loss == abs(sum([3, 4, 5, 6, 7]) - 10)

            results = call_bbopt(mixture_file)
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(mixture_data)

            reload(mixture_example)
            assert_improving(mixture_example.bb.get_data(print_data=True))
            assert mixture_example.loss == want
            assert 0 <= mixture_example.loss < 85
            assert (len)((set)((map)(_coconut_base_compose(_coconut.operator.itemgetter(("memo")), (_coconut.operator.itemgetter(("alg")), 0)), mixture_example.bb.get_data()["examples"]))) > 1
            assert mixture_example.bb.num_examples == NUM_TRIALS

    def test_json(self):
        print("\ntest json:")
        with using(json_data):
            from bbopt.examples import json_example
            assert round(json_example.y, 5) == 6

            results = call_bbopt(json_file)
            want = min(get_nums(results, numtype=float))
            assert os.path.exists(json_data)

            reload(json_example)
            assert_improving(json_example.bb.get_data(print_data=True))
            assert json_example.y == want
            assert json_example.bb.num_examples == NUM_TRIALS


_coconut_call_set_names(TestExamples)
if __name__ == "__main__":
    unittest.main()
