#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x9ea86716

# Compiled with Coconut version 2.0.0-a_dev63 [How Not to Be Seen]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:  # type: ignore
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
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:

import os  #3 (line num in coconut source)
sys = _coconut_sys  #4 (line num in coconut source)
import shutil  #5 (line num in coconut source)
import unittest  #6 (line num in coconut source)
import traceback  #7 (line num in coconut source)
from contextlib import contextmanager  #8 (line num in coconut source)
if _coconut_sys.version_info >= (3, 4):  #9 (line num in coconut source)
    from importlib import reload  #9 (line num in coconut source)
else:  #9 (line num in coconut source)
    from imp import reload  #9 (line num in coconut source)

from coconut.command.util import call_output  #11 (line num in coconut source)

from bbopt.util import mean  #13 (line num in coconut source)
from bbopt.util import median  #13 (line num in coconut source)
from bbopt.util import stdev  #13 (line num in coconut source)


# Constants:

NUM_TRIALS = 24  #22 (line num in coconut source)
NUM_PROCS = 2  #23 (line num in coconut source)

example_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")  #25 (line num in coconut source)

random_file = os.path.join(example_dir, "random_example.py")  #27 (line num in coconut source)
random_data = os.path.join(example_dir, "random_example.bbopt.pickle")  #28 (line num in coconut source)

skopt_file = os.path.join(example_dir, "skopt_example.py")  #30 (line num in coconut source)
skopt_data = os.path.join(example_dir, "skopt_example.bbopt.pickle")  #31 (line num in coconut source)

pysot_file = os.path.join(example_dir, "pysot_example.py")  #33 (line num in coconut source)
pysot_data = os.path.join(example_dir, "pysot_example.bbopt.pickle")  #34 (line num in coconut source)

hyperopt_file = os.path.join(example_dir, "hyperopt_example.py")  #36 (line num in coconut source)
hyperopt_data = os.path.join(example_dir, "hyperopt_example.bbopt.pickle")  #37 (line num in coconut source)

conditional_hyperopt_file = os.path.join(example_dir, "conditional_hyperopt_example.py")  #39 (line num in coconut source)
conditional_hyperopt_data = os.path.join(example_dir, "conditional_hyperopt_example.bbopt.pickle")  #40 (line num in coconut source)

conditional_skopt_file = os.path.join(example_dir, "conditional_skopt_example.py")  #42 (line num in coconut source)
conditional_skopt_data = os.path.join(example_dir, "conditional_skopt_example.bbopt.pickle")  #43 (line num in coconut source)

bask_file = os.path.join(example_dir, "bask_example.py")  #45 (line num in coconut source)
bask_data = os.path.join(example_dir, "bask_example.bbopt.pickle")  #46 (line num in coconut source)

numpy_file = os.path.join(example_dir, "numpy_example.py")  #48 (line num in coconut source)
numpy_data = os.path.join(example_dir, "numpy_example.bbopt.pickle")  #49 (line num in coconut source)

meta_file = os.path.join(example_dir, "meta_example.py")  #51 (line num in coconut source)
meta_data = os.path.join(example_dir, "meta_example.bbopt.pickle")  #52 (line num in coconut source)

any_fast_file = os.path.join(example_dir, "any_fast_example.py")  #54 (line num in coconut source)
any_fast_data = os.path.join(example_dir, "any_fast_example.bbopt.pickle")  #55 (line num in coconut source)

mixture_file = os.path.join(example_dir, "mixture_example.py")  #57 (line num in coconut source)
mixture_data = os.path.join(example_dir, "mixture_example.bbopt.pickle")  #58 (line num in coconut source)

json_file = os.path.join(example_dir, "json_example.py")  #60 (line num in coconut source)
json_data = os.path.join(example_dir, "json_example.bbopt.json")  #61 (line num in coconut source)


# Utilities:

@contextmanager  #66 (line num in coconut source)
def using(path, rem_on_start=True, rem_on_end=False):  #67 (line num in coconut source)
    """Removes a path when the context is started and/or ended."""  #68 (line num in coconut source)
    if rem_on_start and os.path.exists(path):  #69 (line num in coconut source)
        if os.path.isdir(path):  #70 (line num in coconut source)
            shutil.rmtree(path)  #71 (line num in coconut source)
        elif os.path.isfile(path):  #72 (line num in coconut source)
            os.remove(path)  #73 (line num in coconut source)
        assert not os.path.exists(path), "failed to remove: {_coconut_format_0}".format(_coconut_format_0=(path))  #74 (line num in coconut source)
    try:  #75 (line num in coconut source)
        yield  #76 (line num in coconut source)
    finally:  #77 (line num in coconut source)
        if rem_on_end:  #78 (line num in coconut source)
            try:  #79 (line num in coconut source)
                if os.path.isdir(path):  #80 (line num in coconut source)
                    shutil.rmtree(path)  #81 (line num in coconut source)
                elif os.path.isfile(path):  #82 (line num in coconut source)
                    os.remove(path)  #83 (line num in coconut source)
            except OSError:  #84 (line num in coconut source)
                traceback.print_exc()  #85 (line num in coconut source)



always_ignore_errs = ("DeprecationWarning: numpy.core.umath_tests is an internal NumPy module", "from numpy.core.umath_tests import", "RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility.", "return f(*args, **kwds)", "UserWarning: The objective has been evaluated at this point before.", 'warnings.warn("The objective has been evaluated', "DeprecationWarning: sklearn.externals.joblib is deprecated", "warnings.warn(msg, category=DeprecationWarning)")  #88 (line num in coconut source)


def call_test(args, ignore_errs=(), prepend_py=True):  #100 (line num in coconut source)
    """Call args on the command line for a test."""  #101 (line num in coconut source)
    if prepend_py:  #102 (line num in coconut source)
        args = [sys.executable, "-m"] + args  #103 (line num in coconut source)
    print(">", " ".join(args))  #104 (line num in coconut source)
    stdout, stderr, retcode = call_output(args)  #105 (line num in coconut source)
    stdout, stderr = "".join(stdout), "".join(stderr)  #106 (line num in coconut source)
    (print)((stdout + stderr).strip())  #107 (line num in coconut source)
    clean_stderr = []  #108 (line num in coconut source)
    for line in stderr.splitlines():  #109 (line num in coconut source)
        if not any((ignore in line for ignore in _coconut.itertools.chain.from_iterable(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: always_ignore_errs, lambda: ignore_errs))))):  #110 (line num in coconut source)
            clean_stderr.append(line)  #111 (line num in coconut source)
    clean_stderr = "\n".join(clean_stderr)  #112 (line num in coconut source)
    assert not retcode and not clean_stderr, clean_stderr  #113 (line num in coconut source)
    return stdout  #114 (line num in coconut source)



def get_nums(inputstr, numtype=float):  #117 (line num in coconut source)
    """Get only the lines that are numbers."""  #118 (line num in coconut source)
    for line in inputstr.splitlines():  #119 (line num in coconut source)
        try:  #120 (line num in coconut source)
            yield numtype(line.strip())  #121 (line num in coconut source)
        except ValueError:  #122 (line num in coconut source)
            pass  #123 (line num in coconut source)



def middle_mean(xs):  #126 (line num in coconut source)
    """Mean of the middle half of xs."""  #127 (line num in coconut source)
    a, b = len(xs) // 4, 3 * len(xs) // 4  #128 (line num in coconut source)
    return mean(xs[a:b])  #129 (line num in coconut source)



def assert_improving(data, ave_func=mean, within_stdevs=0.5):  #132 (line num in coconut source)
    """Assert that the second half of data is greater/smaller than the first."""  #133 (line num in coconut source)
    examples = data["examples"]  #134 (line num in coconut source)
    assert len(examples) >= 2, data  #135 (line num in coconut source)
    half_pt = len(examples) // 2  #136 (line num in coconut source)
    first_half, second_half = examples[:half_pt], examples[half_pt:]  #137 (line num in coconut source)
    if "loss" in first_half[0]:  #138 (line num in coconut source)
        ave_func = min if ave_func is None else ave_func  #139 (line num in coconut source)
        first_losses = (map)(_coconut.operator.itemgetter(("loss")), first_half)  #140 (line num in coconut source)
        second_losses = (map)(_coconut.operator.itemgetter(("loss")), second_half)  #141 (line num in coconut source)

        first_ave_loss = ave_func(first_losses)  #143 (line num in coconut source)
        second_ave_loss = ave_func(second_losses)  #144 (line num in coconut source)
        first_stdev = stdev(first_losses)  #145 (line num in coconut source)
        assert second_ave_loss - first_ave_loss < first_stdev * within_stdevs  #146 (line num in coconut source)
    else:  #147 (line num in coconut source)
        ave_func = max if ave_func is None else ave_func  #148 (line num in coconut source)
        first_gains = (map)(_coconut.operator.itemgetter(("gain")), first_half)  #149 (line num in coconut source)
        second_gains = (map)(_coconut.operator.itemgetter(("gain")), second_half)  #150 (line num in coconut source)

        first_ave_gain = ave_func(first_gains)  #152 (line num in coconut source)
        second_ave_gain = ave_func(second_gains)  #153 (line num in coconut source)
        first_stdev = stdev(first_gains)  #154 (line num in coconut source)
        assert second_ave_gain - first_ave_gain > -first_stdev * within_stdevs  #155 (line num in coconut source)



def call_bbopt(fpath, trials=NUM_TRIALS, procs=NUM_PROCS):  #158 (line num in coconut source)
    """Call bbopt on the given file."""  #159 (line num in coconut source)
    cmd = ["bbopt", fpath]  #160 (line num in coconut source)
    if trials is not None:  #161 (line num in coconut source)
        cmd += ["-n", str(trials)]  #162 (line num in coconut source)
    if procs is not None:  #163 (line num in coconut source)
        cmd += ["-j", str(procs)]  #164 (line num in coconut source)
    return call_test(cmd)  #165 (line num in coconut source)


# Tests:


class TestExamples(unittest.TestCase):  #170 (line num in coconut source)

    def test_random(self):  #172 (line num in coconut source)
        print("\ntest random:")  #173 (line num in coconut source)
        with using(random_data):  #174 (line num in coconut source)
            results = call_bbopt(random_file, procs=1)  #175 (line num in coconut source)
            want = max(get_nums(results, numtype=int))  #176 (line num in coconut source)
            assert os.path.exists(random_data)  #177 (line num in coconut source)

            from bbopt.examples import random_example  #179 (line num in coconut source)
            random_example.bb.get_data(print_data=True)  #180 (line num in coconut source)
            assert random_example.x == want  #181 (line num in coconut source)
            assert 1 < random_example.x <= 10  #182 (line num in coconut source)
            assert random_example.bb.num_examples == NUM_TRIALS  #183 (line num in coconut source)


    def test_skopt(self):  #185 (line num in coconut source)
        print("\ntest skopt:")  #186 (line num in coconut source)
        with using(skopt_data):  #187 (line num in coconut source)
            results = call_bbopt(skopt_file)  #188 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #189 (line num in coconut source)
            assert os.path.exists(skopt_data)  #190 (line num in coconut source)

            from bbopt.examples import skopt_example  #192 (line num in coconut source)
            assert_improving(skopt_example.bb.get_data(print_data=True), ave_func=middle_mean)  #193 (line num in coconut source)
            assert skopt_example.y == want  #194 (line num in coconut source)
            assert -9 <= skopt_example.y < 21  #195 (line num in coconut source)
            assert skopt_example.bb.num_examples == NUM_TRIALS  #196 (line num in coconut source)


    def test_conditional_skopt(self):  #198 (line num in coconut source)
        print("\ntest conditional_skopt:")  #199 (line num in coconut source)
        with using(conditional_skopt_data):  #200 (line num in coconut source)
            results = call_bbopt(conditional_skopt_file)  #201 (line num in coconut source)
            want = max(get_nums(results, numtype=int))  #202 (line num in coconut source)
            assert os.path.exists(conditional_skopt_data)  #203 (line num in coconut source)

            from bbopt.examples import conditional_skopt_example  #205 (line num in coconut source)
            assert_improving(conditional_skopt_example.bb.get_data(print_data=True))  #206 (line num in coconut source)
            assert conditional_skopt_example.x == want  #207 (line num in coconut source)
            assert 0 < conditional_skopt_example.x <= 20  #208 (line num in coconut source)
            assert conditional_skopt_example.bb.num_examples == NUM_TRIALS  #209 (line num in coconut source)


    if sys.version_info >= (3, 7):  #211 (line num in coconut source)
        def test_bask(self):  #212 (line num in coconut source)
            print("\ntest bask:")  #213 (line num in coconut source)
            with using(bask_data):  #214 (line num in coconut source)
                results = call_bbopt(bask_file)  #215 (line num in coconut source)
                want = max(get_nums(results, numtype=float))  #216 (line num in coconut source)
                assert os.path.exists(bask_data)  #217 (line num in coconut source)

                from bbopt.examples import bask_example  #219 (line num in coconut source)
                assert_improving(bask_example.bb.get_data(print_data=True), ave_func=median)  #220 (line num in coconut source)
                assert 0 < want <= 20  #221 (line num in coconut source)
                assert 0 < bask_example.x <= 20  #222 (line num in coconut source)
                assert bask_example.bb.num_examples == NUM_TRIALS  #223 (line num in coconut source)


    if sys.version_info >= (3,):  #225 (line num in coconut source)
        def test_pysot(self):  #226 (line num in coconut source)
            print("\ntest pysot:")  #227 (line num in coconut source)
            with using(pysot_data):  #228 (line num in coconut source)
                results = call_bbopt(pysot_file, trials=2)  #229 (line num in coconut source)
                want = min(get_nums(results, numtype=float))  #230 (line num in coconut source)
                assert os.path.exists(pysot_data)  #231 (line num in coconut source)

                from bbopt.examples import pysot_example  #233 (line num in coconut source)
                assert_improving(pysot_example.bb.get_data(print_data=True))  #234 (line num in coconut source)
                assert pysot_example.best_y == want  #235 (line num in coconut source)
                assert -9 <= pysot_example.best_y < 21  #236 (line num in coconut source)
                assert pysot_example.bb.num_examples == 20  #237 (line num in coconut source)


    def test_hyperopt(self):  #239 (line num in coconut source)
        print("\ntest hyperopt:")  #240 (line num in coconut source)
        with using(hyperopt_data):  #241 (line num in coconut source)
            results = call_bbopt(hyperopt_file)  #242 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #243 (line num in coconut source)
            assert os.path.exists(hyperopt_data)  #244 (line num in coconut source)

            from bbopt.examples import hyperopt_example  #246 (line num in coconut source)
            assert_improving(hyperopt_example.bb.get_data(print_data=True), ave_func=None)  #247 (line num in coconut source)
            assert hyperopt_example.y == want  #248 (line num in coconut source)
            assert hyperopt_example.bb.num_examples == NUM_TRIALS  #249 (line num in coconut source)


    def test_conditional_hyperopt(self):  #251 (line num in coconut source)
        print("\ntest conditional_hyperopt:")  #252 (line num in coconut source)
        with using(conditional_hyperopt_data):  #253 (line num in coconut source)
            results = call_bbopt(conditional_hyperopt_file)  #254 (line num in coconut source)
            want = max(get_nums(results, numtype=int))  #255 (line num in coconut source)
            assert os.path.exists(conditional_hyperopt_data)  #256 (line num in coconut source)

            from bbopt.examples import conditional_hyperopt_example  #258 (line num in coconut source)
            assert_improving(conditional_hyperopt_example.bb.get_data(print_data=True))  #259 (line num in coconut source)
            assert conditional_hyperopt_example.x == want  #260 (line num in coconut source)
            assert 0 < conditional_hyperopt_example.x <= 20  #261 (line num in coconut source)
            assert conditional_hyperopt_example.bb.num_examples == NUM_TRIALS  #262 (line num in coconut source)


    def test_numpy(self):  #264 (line num in coconut source)
        print("\ntest numpy:")  #265 (line num in coconut source)
        with using(numpy_data):  #266 (line num in coconut source)
            from bbopt.examples import numpy_example  #267 (line num in coconut source)
            assert numpy_example.y == 0  #268 (line num in coconut source)

            results = call_bbopt(numpy_file)  #270 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #271 (line num in coconut source)
            assert os.path.exists(numpy_data)  #272 (line num in coconut source)

            reload(numpy_example)  #274 (line num in coconut source)
            assert_improving(numpy_example.bb.get_data(print_data=True))  #275 (line num in coconut source)
            assert numpy_example.y == want  #276 (line num in coconut source)
            assert numpy_example.bb.num_examples == NUM_TRIALS  #277 (line num in coconut source)


    def test_meta(self):  #279 (line num in coconut source)
        print("\ntest meta:")  #280 (line num in coconut source)
        with using(meta_data):  #281 (line num in coconut source)
            results = call_bbopt(meta_file)  #282 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #283 (line num in coconut source)
            assert os.path.exists(meta_data)  #284 (line num in coconut source)

            from bbopt.examples import meta_example  #286 (line num in coconut source)
            assert_improving(meta_example.bb.get_data(print_data=True))  #287 (line num in coconut source)
            assert meta_example.u == want  #288 (line num in coconut source)
            assert 0 <= meta_example.u < 1  #289 (line num in coconut source)
            assert meta_example.bb.num_examples == NUM_TRIALS  #290 (line num in coconut source)


    def test_any_fast(self):  #292 (line num in coconut source)
        print("\ntest any_fast:")  #293 (line num in coconut source)
        with using(any_fast_data):  #294 (line num in coconut source)
            results = call_bbopt(any_fast_file)  #295 (line num in coconut source)

            want = min(get_nums(results, numtype=float))  #297 (line num in coconut source)
            assert os.path.exists(any_fast_data)  #298 (line num in coconut source)

            from bbopt.examples import any_fast_example  #300 (line num in coconut source)
            assert_improving(any_fast_example.bb.get_data(print_data=True), ave_func=None)  #301 (line num in coconut source)
            assert any_fast_example.u == want  #302 (line num in coconut source)
            assert any_fast_example.u < 1  #303 (line num in coconut source)
            assert any_fast_example.bb.num_examples == NUM_TRIALS  #304 (line num in coconut source)


    def test_mixture(self):  #306 (line num in coconut source)
        print("\ntest mixture:")  #307 (line num in coconut source)
        with using(mixture_data):  #308 (line num in coconut source)
            from bbopt.examples import mixture_example  #309 (line num in coconut source)
            assert mixture_example.loss == abs(sum([3, 4, 5, 6, 7]) - 10)  #310 (line num in coconut source)

            results = call_bbopt(mixture_file)  #312 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #313 (line num in coconut source)
            assert os.path.exists(mixture_data)  #314 (line num in coconut source)

            reload(mixture_example)  #316 (line num in coconut source)
            assert_improving(mixture_example.bb.get_data(print_data=True))  #317 (line num in coconut source)
            assert mixture_example.loss == want  #318 (line num in coconut source)
            assert 0 <= mixture_example.loss < 85  #319 (line num in coconut source)
            assert (len)((set)((map)(_coconut_base_compose(_coconut.operator.itemgetter(("memo")), (_coconut.operator.itemgetter(("alg")), 0)), mixture_example.bb.get_data()["examples"]))) > 1  #320 (line num in coconut source)
            assert mixture_example.bb.num_examples == NUM_TRIALS  #321 (line num in coconut source)


    def test_json(self):  #323 (line num in coconut source)
        print("\ntest json:")  #324 (line num in coconut source)
        with using(json_data):  #325 (line num in coconut source)
            from bbopt.examples import json_example  #326 (line num in coconut source)
            assert round(json_example.y, 5) == 6  #327 (line num in coconut source)

            results = call_bbopt(json_file)  #329 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #330 (line num in coconut source)
            assert os.path.exists(json_data)  #331 (line num in coconut source)

            reload(json_example)  #333 (line num in coconut source)
            assert_improving(json_example.bb.get_data(print_data=True))  #334 (line num in coconut source)
            assert json_example.y == want  #335 (line num in coconut source)
            assert json_example.bb.num_examples == NUM_TRIALS  #336 (line num in coconut source)



_coconut_call_set_names(TestExamples)  #339 (line num in coconut source)
if __name__ == "__main__":  #339 (line num in coconut source)
    unittest.main()  #340 (line num in coconut source)
