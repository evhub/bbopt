#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb2225c8b

# Compiled with Coconut version 3.0.0-a_dev36

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
_coconut_header_info = ('3.0.0-a_dev36', '', True)
import os as _coconut_os
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in
if _coconut_pop_path:
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------

import math  #1 (line in Coconut source)

import numpy as np  #3 (line in Coconut source)
from matplotlib import pyplot as plt  #4 (line in Coconut source)

from bbopt import BlackBoxOptimizer  #6 (line in Coconut source)


# Benchmarks

OPT_FUNCS = []  #11 (line in Coconut source)


def cond_sin_func(bb):  #14 (line in Coconut source)
    dist = bb.choice("dist", ["uniform", "normal"])  #15 (line in Coconut source)
    if dist == "normal":  #16 (line in Coconut source)
        u = bb.normalvariate("x0_n", 0, 1) * math.sin(bb.normalvariate("x1_n", 0, 1))  #17 (line in Coconut source)
    else:  #18 (line in Coconut source)
        u = bb.random("x0_u") * math.sin(bb.random("x1_u"))  #19 (line in Coconut source)
    bb.minimize(u)  #20 (line in Coconut source)


OPT_FUNCS.append(cond_sin_func)  #22 (line in Coconut source)


def trisum_func(bb):  #25 (line in Coconut source)
    x0 = bb.randrange("x0", 1, 11, guess=5)  #26 (line in Coconut source)
    x1 = bb.uniform("x1", 0, 1)  #27 (line in Coconut source)
    x2 = bb.choice("x2", [-10, -1, 0, 1, 10])  #28 (line in Coconut source)
    y = x0 + x1 * x2  #29 (line in Coconut source)
    bb.minimize(y)  #30 (line in Coconut source)


OPT_FUNCS.append(trisum_func)  #32 (line in Coconut source)


def numpy_func(bb):  #35 (line in Coconut source)
    x0 = bb.rand("x0", 1, 5, guess=np.zeros((1, 5)))  #36 (line in Coconut source)
    x1 = bb.randn("x1", 5, 1, guess=np.zeros((5, 1)))  #37 (line in Coconut source)
    y = float(x0.dot(x1))  #38 (line in Coconut source)
    bb.minimize(y)  #39 (line in Coconut source)


OPT_FUNCS.append(numpy_func)  #41 (line in Coconut source)


def sample_func(bb):  #44 (line in Coconut source)
    xs = bb.unshuffled_sample("xs", range(10), 5, guess=[3, 4, 5, 6, 7])  #45 (line in Coconut source)
    y = bb.choice("y", [1, 10, 100], guess=10)  #46 (line in Coconut source)
    loss = abs(sum(xs) - y)  #47 (line in Coconut source)
    bb.minimize(loss)  #48 (line in Coconut source)


OPT_FUNCS.append(sample_func)  #50 (line in Coconut source)


def sin_prod_func(bb):  #53 (line in Coconut source)
    u = bb.random("x0") * math.sin(bb.random("x1"))  #54 (line in Coconut source)
    bb.minimize(u)  #55 (line in Coconut source)


OPT_FUNCS.append(sin_prod_func)  #57 (line in Coconut source)


def lognorm_func(bb):  #60 (line in Coconut source)
    x0 = bb.loguniform("x0", 1, 10, guess=5)  #61 (line in Coconut source)
    x1 = bb.lognormvariate("x1", 0, 1, guess=1)  #62 (line in Coconut source)
    y = x0 + x1  #63 (line in Coconut source)
    bb.minimize(y)  #64 (line in Coconut source)


OPT_FUNCS.append(lognorm_func)  #66 (line in Coconut source)


def norm_func(bb):  #69 (line in Coconut source)
    x0 = bb.randint("x0", 1, 10, guess=5)  #70 (line in Coconut source)
    x1 = bb.normalvariate("x1", mu=0, sigma=1)  #71 (line in Coconut source)
    x2 = bb.choice("x2", [-10, -1, 0, 1, 10])  #72 (line in Coconut source)
    y = x0 + x1 * x2  #73 (line in Coconut source)
    bb.minimize(y)  #74 (line in Coconut source)


OPT_FUNCS.append(norm_func)  #76 (line in Coconut source)


def cond_gain_func(bb):  #79 (line in Coconut source)
    use_high = bb.randbool("use_high", guess=False)  #80 (line in Coconut source)
    if use_high:  #81 (line in Coconut source)
        x = bb.uniform("x_high", 10, 20)  #82 (line in Coconut source)
    else:  #83 (line in Coconut source)
        x = bb.randrange("x_low", 10)  #84 (line in Coconut source)
    bb.maximize(x)  #85 (line in Coconut source)


OPT_FUNCS.append(cond_gain_func)  #87 (line in Coconut source)


# Main

def benchmark(algs, plot_func="plot_convergence", n=10):  #92 (line in Coconut source)
    figsize = (int)((math.ceil)((math.sqrt)(len(OPT_FUNCS))))  #93 (line in Coconut source)
    fig, axs = plt.subplots(figsize, figsize)  #94 (line in Coconut source)
    for i, func in enumerate(OPT_FUNCS):  #95 (line in Coconut source)
        ax = axs[i // figsize, i % figsize]  #96 (line in Coconut source)
        for alg in algs:  #97 (line in Coconut source)
            bb = BlackBoxOptimizer(__file__, tag="{_coconut_format_0}_{_coconut_format_1}".format(_coconut_format_0=(func.__name__), _coconut_format_1=(alg)))  #98 (line in Coconut source)
            if bb.num_examples < n:  #99 (line in Coconut source)
                for _ in range(n - bb.num_examples):  #100 (line in Coconut source)
                    if isinstance(alg, tuple):  #101 (line in Coconut source)
                        bb.run_meta(alg)  #102 (line in Coconut source)
                    else:  #103 (line in Coconut source)
                        bb.run(alg)  #104 (line in Coconut source)
                    func(bb)  #105 (line in Coconut source)
            getattr(bb, plot_func)(ax, label=str(alg))  #106 (line in Coconut source)
        ax.set_title(func.__name__)  #107 (line in Coconut source)
        ax.set_xlabel("")  #108 (line in Coconut source)
        ax.legend()  #109 (line in Coconut source)
    plt.show()  #110 (line in Coconut source)



if __name__ == "__main__":  #113 (line in Coconut source)
    benchmark(("safe_gaussian_process", "openai", ("openai", "safe_gaussian_process")))  #114 (line in Coconut source)
