#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x516b5464

# Compiled with Coconut version 2.0.0-a_dev53 [How Not to Be Seen]

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
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

# Imports:

import os  #3 (line num in coconut source)
sys = _coconut_sys  #4 (line num in coconut source)
import shutil  #5 (line num in coconut source)
import unittest  #6 (line num in coconut source)
import traceback  #7 (line num in coconut source)
from contextlib import contextmanager  #8 (line num in coconut source)
if _coconut_sys.version_info < (3, 4):  #9 (line num in coconut source)
    from imp import reload  #9 (line num in coconut source)
else:  #9 (line num in coconut source)
    from importlib import reload  #9 (line num in coconut source)

from coconut.command.util import call_output  #11 (line num in coconut source)

from bbopt.util import mean  #13 (line num in coconut source)
from bbopt.util import median  #13 (line num in coconut source)


# Constants:

NUM_TRIALS = 24  #21 (line num in coconut source)
NUM_PROCS = 2  #22 (line num in coconut source)

example_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "examples")  #24 (line num in coconut source)

random_file = os.path.join(example_dir, "random_example.py")  #26 (line num in coconut source)
random_data = os.path.join(example_dir, "random_example.bbopt.pickle")  #27 (line num in coconut source)

skopt_file = os.path.join(example_dir, "skopt_example.py")  #29 (line num in coconut source)
skopt_data = os.path.join(example_dir, "skopt_example.bbopt.pickle")  #30 (line num in coconut source)

pysot_file = os.path.join(example_dir, "pysot_example.py")  #32 (line num in coconut source)
pysot_data = os.path.join(example_dir, "pysot_example.bbopt.pickle")  #33 (line num in coconut source)

hyperopt_file = os.path.join(example_dir, "hyperopt_example.py")  #35 (line num in coconut source)
hyperopt_data = os.path.join(example_dir, "hyperopt_example.bbopt.pickle")  #36 (line num in coconut source)

conditional_hyperopt_file = os.path.join(example_dir, "conditional_hyperopt_example.py")  #38 (line num in coconut source)
conditional_hyperopt_data = os.path.join(example_dir, "conditional_hyperopt_example.bbopt.pickle")  #39 (line num in coconut source)

conditional_skopt_file = os.path.join(example_dir, "conditional_skopt_example.py")  #41 (line num in coconut source)
conditional_skopt_data = os.path.join(example_dir, "conditional_skopt_example.bbopt.pickle")  #42 (line num in coconut source)

bask_file = os.path.join(example_dir, "bask_example.py")  #44 (line num in coconut source)
bask_data = os.path.join(example_dir, "bask_example.bbopt.pickle")  #45 (line num in coconut source)

numpy_file = os.path.join(example_dir, "numpy_example.py")  #47 (line num in coconut source)
numpy_data = os.path.join(example_dir, "numpy_example.bbopt.pickle")  #48 (line num in coconut source)

meta_file = os.path.join(example_dir, "meta_example.py")  #50 (line num in coconut source)
meta_data = os.path.join(example_dir, "meta_example.bbopt.pickle")  #51 (line num in coconut source)

any_fast_file = os.path.join(example_dir, "any_fast_example.py")  #53 (line num in coconut source)
any_fast_data = os.path.join(example_dir, "any_fast_example.bbopt.pickle")  #54 (line num in coconut source)

mixture_file = os.path.join(example_dir, "mixture_example.py")  #56 (line num in coconut source)
mixture_data = os.path.join(example_dir, "mixture_example.bbopt.pickle")  #57 (line num in coconut source)

json_file = os.path.join(example_dir, "json_example.py")  #59 (line num in coconut source)
json_data = os.path.join(example_dir, "json_example.bbopt.json")  #60 (line num in coconut source)


# Utilities:

@contextmanager  #65 (line num in coconut source)
def using(path, rem_on_start=True, rem_on_end=False):  #66 (line num in coconut source)
    """Removes a path when the context is started and/or ended."""  #67 (line num in coconut source)
    if rem_on_start and os.path.exists(path):  #68 (line num in coconut source)
        if os.path.isdir(path):  #69 (line num in coconut source)
            shutil.rmtree(path)  #70 (line num in coconut source)
        elif os.path.isfile(path):  #71 (line num in coconut source)
            os.remove(path)  #72 (line num in coconut source)
        assert not os.path.exists(path), "failed to remove: {_coconut_format_0}".format(_coconut_format_0=(path))  #73 (line num in coconut source)
    try:  #74 (line num in coconut source)
        yield  #75 (line num in coconut source)
    finally:  #76 (line num in coconut source)
        if rem_on_end:  #77 (line num in coconut source)
            try:  #78 (line num in coconut source)
                if os.path.isdir(path):  #79 (line num in coconut source)
                    shutil.rmtree(path)  #80 (line num in coconut source)
                elif os.path.isfile(path):  #81 (line num in coconut source)
                    os.remove(path)  #82 (line num in coconut source)
            except OSError:  #83 (line num in coconut source)
                traceback.print_exc()  #84 (line num in coconut source)



always_ignore_errs = ("DeprecationWarning: numpy.core.umath_tests is an internal NumPy module", "from numpy.core.umath_tests import", "RuntimeWarning: numpy.dtype size changed, may indicate binary incompatibility.", "return f(*args, **kwds)", "UserWarning: The objective has been evaluated at this point before.", 'warnings.warn("The objective has been evaluated', "DeprecationWarning: sklearn.externals.joblib is deprecated", "warnings.warn(msg, category=DeprecationWarning)")  #87 (line num in coconut source)


def call_test(args, ignore_errs=(), prepend_py=True):  #99 (line num in coconut source)
    """Call args on the command line for a test."""  #100 (line num in coconut source)
    if prepend_py:  #101 (line num in coconut source)
        args = [sys.executable, "-m"] + args  #102 (line num in coconut source)
    print(">", " ".join(args))  #103 (line num in coconut source)
    stdout, stderr, retcode = call_output(args)  #104 (line num in coconut source)
    stdout, stderr = "".join(stdout), "".join(stderr)  #105 (line num in coconut source)
    (print)((stdout + stderr).strip())  #106 (line num in coconut source)
    clean_stderr = []  #107 (line num in coconut source)
    for line in stderr.splitlines():  #108 (line num in coconut source)
        if not any((ignore in line for ignore in _coconut.itertools.chain.from_iterable(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: always_ignore_errs, lambda: ignore_errs))))):  #109 (line num in coconut source)
            clean_stderr.append(line)  #110 (line num in coconut source)
    clean_stderr = "\n".join(clean_stderr)  #111 (line num in coconut source)
    assert not retcode and not clean_stderr, clean_stderr  #112 (line num in coconut source)
    return stdout  #113 (line num in coconut source)



def get_nums(inputstr, numtype=float):  #116 (line num in coconut source)
    """Get only the lines that are numbers."""  #117 (line num in coconut source)
    for line in inputstr.splitlines():  #118 (line num in coconut source)
        try:  #119 (line num in coconut source)
            yield numtype(line.strip())  #120 (line num in coconut source)
        except ValueError:  #121 (line num in coconut source)
            pass  #122 (line num in coconut source)



def middle_mean(xs):  #125 (line num in coconut source)
    """Mean of the middle half of xs."""  #126 (line num in coconut source)
    a, b = len(xs) // 4, 3 * len(xs) // 4  #127 (line num in coconut source)
    return mean(xs[a:b])  #128 (line num in coconut source)



def stdev(xs):  #131 (line num in coconut source)
    """Standard deviation of xs."""  #132 (line num in coconut source)
    mu = mean(xs)  #134 (line num in coconut source)


    return mean(((x - mu)**2 for x in xs))**0.5  #137 (line num in coconut source)

def assert_improving(data, ave_func=mean, within_stdevs=0.5):  #137 (line num in coconut source)
    """Assert that the second half of data is greater/smaller than the first."""  #138 (line num in coconut source)
    examples = data["examples"]  #139 (line num in coconut source)
    assert len(examples) >= 2, data  #140 (line num in coconut source)
    half_pt = len(examples) // 2  #141 (line num in coconut source)
    first_half, second_half = examples[:half_pt], examples[half_pt:]  #142 (line num in coconut source)
    if "loss" in first_half[0]:  #143 (line num in coconut source)
        ave_func = min if ave_func is None else ave_func  #144 (line num in coconut source)
        first_losses = (map)(_coconut.operator.itemgetter(("loss")), first_half)  #145 (line num in coconut source)
        second_losses = (map)(_coconut.operator.itemgetter(("loss")), second_half)  #146 (line num in coconut source)

        first_ave_loss = ave_func(first_losses)  #148 (line num in coconut source)
        second_ave_loss = ave_func(second_losses)  #149 (line num in coconut source)
        first_stdev = stdev(first_losses)  #150 (line num in coconut source)
        assert second_ave_loss - first_ave_loss < first_stdev * within_stdevs  #151 (line num in coconut source)
    else:  #152 (line num in coconut source)
        ave_func = max if ave_func is None else ave_func  #153 (line num in coconut source)
        first_gains = (map)(_coconut.operator.itemgetter(("gain")), first_half)  #154 (line num in coconut source)
        second_gains = (map)(_coconut.operator.itemgetter(("gain")), second_half)  #155 (line num in coconut source)

        first_ave_gain = ave_func(first_gains)  #157 (line num in coconut source)
        second_ave_gain = ave_func(second_gains)  #158 (line num in coconut source)
        first_stdev = stdev(first_gains)  #159 (line num in coconut source)
        assert second_ave_gain - first_ave_gain > -first_stdev * within_stdevs  #160 (line num in coconut source)



def call_bbopt(fpath, trials=NUM_TRIALS, procs=NUM_PROCS):  #163 (line num in coconut source)
    """Call bbopt on the given file."""  #164 (line num in coconut source)
    cmd = ["bbopt", fpath]  #165 (line num in coconut source)
    if trials is not None:  #166 (line num in coconut source)
        cmd += ["-n", str(trials)]  #167 (line num in coconut source)
    if procs is not None:  #168 (line num in coconut source)
        cmd += ["-j", str(procs)]  #169 (line num in coconut source)
    return call_test(cmd)  #170 (line num in coconut source)


# Tests:


class TestExamples(unittest.TestCase):  #175 (line num in coconut source)

    def test_random(self):  #177 (line num in coconut source)
        print("\ntest random:")  #178 (line num in coconut source)
        with using(random_data):  #179 (line num in coconut source)
            results = call_bbopt(random_file, procs=1)  #180 (line num in coconut source)
            want = max(get_nums(results, numtype=int))  #181 (line num in coconut source)
            assert os.path.exists(random_data)  #182 (line num in coconut source)

            from bbopt.examples import random_example  #184 (line num in coconut source)
            random_example.bb.get_data(print_data=True)  #185 (line num in coconut source)
            assert random_example.x == want  #186 (line num in coconut source)
            assert 1 < random_example.x <= 10  #187 (line num in coconut source)
            assert random_example.bb.num_examples == NUM_TRIALS  #188 (line num in coconut source)


    def test_skopt(self):  #190 (line num in coconut source)
        print("\ntest skopt:")  #191 (line num in coconut source)
        with using(skopt_data):  #192 (line num in coconut source)
            results = call_bbopt(skopt_file)  #193 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #194 (line num in coconut source)
            assert os.path.exists(skopt_data)  #195 (line num in coconut source)

            from bbopt.examples import skopt_example  #197 (line num in coconut source)
            assert_improving(skopt_example.bb.get_data(print_data=True), ave_func=middle_mean)  #198 (line num in coconut source)
            assert skopt_example.y == want  #199 (line num in coconut source)
            assert -9 <= skopt_example.y < 21  #200 (line num in coconut source)
            assert skopt_example.bb.num_examples == NUM_TRIALS  #201 (line num in coconut source)


    def test_conditional_skopt(self):  #203 (line num in coconut source)
        print("\ntest conditional_skopt:")  #204 (line num in coconut source)
        with using(conditional_skopt_data):  #205 (line num in coconut source)
            results = call_bbopt(conditional_skopt_file)  #206 (line num in coconut source)
            want = max(get_nums(results, numtype=int))  #207 (line num in coconut source)
            assert os.path.exists(conditional_skopt_data)  #208 (line num in coconut source)

            from bbopt.examples import conditional_skopt_example  #210 (line num in coconut source)
            assert_improving(conditional_skopt_example.bb.get_data(print_data=True))  #211 (line num in coconut source)
            assert conditional_skopt_example.x == want  #212 (line num in coconut source)
            assert 0 < conditional_skopt_example.x <= 20  #213 (line num in coconut source)
            assert conditional_skopt_example.bb.num_examples == NUM_TRIALS  #214 (line num in coconut source)


    if sys.version_info >= (3, 7):  #216 (line num in coconut source)
        def test_bask(self):  #217 (line num in coconut source)
            print("\ntest bask:")  #218 (line num in coconut source)
            with using(bask_data):  #219 (line num in coconut source)
                results = call_bbopt(bask_file)  #220 (line num in coconut source)
                want = max(get_nums(results, numtype=float))  #221 (line num in coconut source)
                assert os.path.exists(bask_data)  #222 (line num in coconut source)

                from bbopt.examples import bask_example  #224 (line num in coconut source)
                assert_improving(bask_example.bb.get_data(print_data=True), ave_func=median)  #225 (line num in coconut source)
                assert 0 < want <= 20  #226 (line num in coconut source)
                assert 0 < bask_example.x <= 20  #227 (line num in coconut source)
                assert bask_example.bb.num_examples == NUM_TRIALS  #228 (line num in coconut source)


    if sys.version_info >= (3,):  #230 (line num in coconut source)
        def test_pysot(self):  #231 (line num in coconut source)
            print("\ntest pysot:")  #232 (line num in coconut source)
            with using(pysot_data):  #233 (line num in coconut source)
                results = call_bbopt(pysot_file, trials=2)  #234 (line num in coconut source)
                want = min(get_nums(results, numtype=float))  #235 (line num in coconut source)
                assert os.path.exists(pysot_data)  #236 (line num in coconut source)

                from bbopt.examples import pysot_example  #238 (line num in coconut source)
                assert_improving(pysot_example.bb.get_data(print_data=True))  #239 (line num in coconut source)
                assert pysot_example.best_y == want  #240 (line num in coconut source)
                assert -9 <= pysot_example.best_y < 21  #241 (line num in coconut source)
                assert pysot_example.bb.num_examples == 20  #242 (line num in coconut source)


    def test_hyperopt(self):  #244 (line num in coconut source)
        print("\ntest hyperopt:")  #245 (line num in coconut source)
        with using(hyperopt_data):  #246 (line num in coconut source)
            results = call_bbopt(hyperopt_file)  #247 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #248 (line num in coconut source)
            assert os.path.exists(hyperopt_data)  #249 (line num in coconut source)

            from bbopt.examples import hyperopt_example  #251 (line num in coconut source)
            assert_improving(hyperopt_example.bb.get_data(print_data=True), ave_func=None)  #252 (line num in coconut source)
            assert hyperopt_example.y == want  #253 (line num in coconut source)
            assert hyperopt_example.bb.num_examples == NUM_TRIALS  #254 (line num in coconut source)


    def test_conditional_hyperopt(self):  #256 (line num in coconut source)
        print("\ntest conditional_hyperopt:")  #257 (line num in coconut source)
        with using(conditional_hyperopt_data):  #258 (line num in coconut source)
            results = call_bbopt(conditional_hyperopt_file)  #259 (line num in coconut source)
            want = max(get_nums(results, numtype=int))  #260 (line num in coconut source)
            assert os.path.exists(conditional_hyperopt_data)  #261 (line num in coconut source)

            from bbopt.examples import conditional_hyperopt_example  #263 (line num in coconut source)
            assert_improving(conditional_hyperopt_example.bb.get_data(print_data=True))  #264 (line num in coconut source)
            assert conditional_hyperopt_example.x == want  #265 (line num in coconut source)
            assert 0 < conditional_hyperopt_example.x <= 20  #266 (line num in coconut source)
            assert conditional_hyperopt_example.bb.num_examples == NUM_TRIALS  #267 (line num in coconut source)


    def test_numpy(self):  #269 (line num in coconut source)
        print("\ntest numpy:")  #270 (line num in coconut source)
        with using(numpy_data):  #271 (line num in coconut source)
            from bbopt.examples import numpy_example  #272 (line num in coconut source)
            assert numpy_example.y == 0  #273 (line num in coconut source)

            results = call_bbopt(numpy_file)  #275 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #276 (line num in coconut source)
            assert os.path.exists(numpy_data)  #277 (line num in coconut source)

            reload(numpy_example)  #279 (line num in coconut source)
            assert_improving(numpy_example.bb.get_data(print_data=True))  #280 (line num in coconut source)
            assert numpy_example.y == want  #281 (line num in coconut source)
            assert numpy_example.bb.num_examples == NUM_TRIALS  #282 (line num in coconut source)


    def test_meta(self):  #284 (line num in coconut source)
        print("\ntest meta:")  #285 (line num in coconut source)
        with using(meta_data):  #286 (line num in coconut source)
            results = call_bbopt(meta_file)  #287 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #288 (line num in coconut source)
            assert os.path.exists(meta_data)  #289 (line num in coconut source)

            from bbopt.examples import meta_example  #291 (line num in coconut source)
            assert_improving(meta_example.bb.get_data(print_data=True))  #292 (line num in coconut source)
            assert meta_example.u == want  #293 (line num in coconut source)
            assert 0 <= meta_example.u < 1  #294 (line num in coconut source)
            assert meta_example.bb.num_examples == NUM_TRIALS  #295 (line num in coconut source)


    def test_any_fast(self):  #297 (line num in coconut source)
        print("\ntest any_fast:")  #298 (line num in coconut source)
        with using(any_fast_data):  #299 (line num in coconut source)
            results = call_bbopt(any_fast_file)  #300 (line num in coconut source)

            want = min(get_nums(results, numtype=float))  #302 (line num in coconut source)
            assert os.path.exists(any_fast_data)  #303 (line num in coconut source)

            from bbopt.examples import any_fast_example  #305 (line num in coconut source)
            assert_improving(any_fast_example.bb.get_data(print_data=True), ave_func=None)  #306 (line num in coconut source)
            assert any_fast_example.u == want  #307 (line num in coconut source)
            assert any_fast_example.u < 1  #308 (line num in coconut source)
            assert any_fast_example.bb.num_examples == NUM_TRIALS  #309 (line num in coconut source)


    def test_mixture(self):  #311 (line num in coconut source)
        print("\ntest mixture:")  #312 (line num in coconut source)
        with using(mixture_data):  #313 (line num in coconut source)
            from bbopt.examples import mixture_example  #314 (line num in coconut source)
            assert mixture_example.loss == abs(sum([3, 4, 5, 6, 7]) - 10)  #315 (line num in coconut source)

            results = call_bbopt(mixture_file)  #317 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #318 (line num in coconut source)
            assert os.path.exists(mixture_data)  #319 (line num in coconut source)

            reload(mixture_example)  #321 (line num in coconut source)
            assert_improving(mixture_example.bb.get_data(print_data=True))  #322 (line num in coconut source)
            assert mixture_example.loss == want  #323 (line num in coconut source)
            assert 0 <= mixture_example.loss < 85  #324 (line num in coconut source)
            assert (len)((set)((map)(_coconut_base_compose(_coconut.operator.itemgetter(("memo")), (_coconut.operator.itemgetter(("alg")), 0)), mixture_example.bb.get_data()["examples"]))) > 1  #325 (line num in coconut source)
            assert mixture_example.bb.num_examples == NUM_TRIALS  #326 (line num in coconut source)


    def test_json(self):  #328 (line num in coconut source)
        print("\ntest json:")  #329 (line num in coconut source)
        with using(json_data):  #330 (line num in coconut source)
            from bbopt.examples import json_example  #331 (line num in coconut source)
            assert round(json_example.y, 5) == 6  #332 (line num in coconut source)

            results = call_bbopt(json_file)  #334 (line num in coconut source)
            want = min(get_nums(results, numtype=float))  #335 (line num in coconut source)
            assert os.path.exists(json_data)  #336 (line num in coconut source)

            reload(json_example)  #338 (line num in coconut source)
            assert_improving(json_example.bb.get_data(print_data=True))  #339 (line num in coconut source)
            assert json_example.y == want  #340 (line num in coconut source)
            assert json_example.bb.num_examples == NUM_TRIALS  #341 (line num in coconut source)



_coconut_call_set_names(TestExamples)  #344 (line num in coconut source)
if __name__ == "__main__":  #344 (line num in coconut source)
    unittest.main()  #345 (line num in coconut source)
