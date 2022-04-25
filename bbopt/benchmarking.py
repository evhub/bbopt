#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa087598

# Compiled with Coconut version 2.0.0-a_dev53 [How Not to Be Seen]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
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

import math

import numpy as np
from matplotlib import pyplot as plt

from bbopt import BlackBoxOptimizer


# Benchmarks

OPT_FUNCS = []


def cond_sin_func(bb):
    dist = bb.choice("dist", ["uniform", "normal"])
    if dist == "normal":
        u = bb.normalvariate("x0_n", 0, 1) * math.sin(bb.normalvariate("x1_n", 0, 1))
    else:
        u = bb.random("x0_u") * math.sin(bb.random("x1_u"))
    bb.minimize(u)


OPT_FUNCS.append(cond_sin_func)


def trisum_func(bb):
    x0 = bb.randrange("x0", 1, 11, guess=5)
    x1 = bb.uniform("x1", 0, 1)
    x2 = bb.choice("x2", [-10, -1, 0, 1, 10])
    y = x0 + x1 * x2
    bb.minimize(y)


OPT_FUNCS.append(trisum_func)


def numpy_func(bb):
    x0 = bb.rand("x0", 1, 5, guess=np.zeros((1, 5)))
    x1 = bb.randn("x1", 5, 1, guess=np.zeros((5, 1)))
    y = float(x0.dot(x1))
    bb.minimize(y)


OPT_FUNCS.append(numpy_func)


def sample_func(bb):
    xs = bb.sample("xs", range(10), 5, guess=[3, 4, 5, 6, 7])
    y = bb.choice("y", [1, 10, 100], guess=10)
    loss = abs(sum(xs) - y)
    bb.minimize(loss)


OPT_FUNCS.append(sample_func)


def sin_prod_func(bb):
    u = bb.random("x0") * math.sin(bb.random("x1"))
    bb.minimize(u)


OPT_FUNCS.append(sin_prod_func)


def lognorm_func(bb):
    x0 = bb.loguniform("x0", 1, 10, guess=5)
    x1 = bb.lognormvariate("x1", 0, 1, guess=1)
    y = x0 + x1
    bb.minimize(y)


OPT_FUNCS.append(lognorm_func)


def norm_func(bb):
    x0 = bb.randint("x0", 1, 10, guess=5)
    x1 = bb.normalvariate("x1", mu=0, sigma=1)
    x2 = bb.choice("x2", [-10, -1, 0, 1, 10])
    y = x0 + x1 * x2
    bb.minimize(y)


OPT_FUNCS.append(norm_func)


def cond_gain_func(bb):
    use_high = bb.randbool("use high", guess=False)
    if use_high:
        x = bb.randrange("x high", 10, 20)
    else:
        x = bb.randrange("x low", 10)
    bb.maximize(x)


OPT_FUNCS.append(cond_gain_func)


# Main

def benchmark(algs, plot_func="plot_history", n=50):
    figsize = (int)((math.ceil)((math.sqrt)(len(OPT_FUNCS))))
    fig, axs = plt.subplots(figsize, figsize)
    for i, func in enumerate(OPT_FUNCS):
        ax = axs[i // figsize, i % figsize]
        for alg in algs:
            bb = BlackBoxOptimizer(__file__, tag="{_coconut_format_0}_{_coconut_format_1}".format(_coconut_format_0=(func.__name__), _coconut_format_1=(alg)))
            if bb.num_examples < n:
                for _ in range(n - bb.num_examples):
                    bb.run(alg)
                    func(bb)
            getattr(bb, plot_func)(ax, label=alg)
        ax.set_title(func.__name__)
        ax.set_xlabel("")
        ax.legend()
    plt.show()



if __name__ == "__main__":
    benchmark(("any_fast", "tpe_or_gp", "openai"))
