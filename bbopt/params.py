#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x27320995

# Compiled with Coconut version 1.4.0-post_dev25 [Ernest Scribbler]

"""
Handles standardizing param calls to use standard library random functions.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel, _coconut_assert
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



if _coconut_sys.version_info < (3, 3):
    from collections import Iterable
else:
    from collections.abc import Iterable
from math import log as ln

from bbopt.util import Num
from bbopt.util import format_err
from bbopt.util import all_isinstance
from bbopt.util import denumpy_all


# Handlers:

def handle_randrange(args):
    if not all_isinstance(args, int):
        raise format_err(ValueError, "arguments to randrange must be integers, not", args)
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise format_err(ValueError, "randrange expects between 1 and 3 arguments, not", args)
    if start > stop:
        raise format_err(ValueError, "randrange start must be less than stop")
    return [start, stop, step]


def handle_choice(args):
    if len(args) != 1 or not isinstance(args[0], Iterable):
        raise format_err(ValueError, "invalid arguments to choice", args)
    return (list(args[0]),)


def handle_uniform(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to uniform", args)


def handle_triangular(args):
    if len(args) != 3 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to triangular", args)


def handle_betavariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to betavariate", args)


def handle_expovariate(args):
    if len(args) != 1 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to expovariate", args)


def handle_gammavariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to gammavariate", args)


def handle_normalvariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to normalvariate", args)


def handle_vonmisesvariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to vonmisesvariate", args)


def handle_paretovariate(args):
    if len(args) != 1 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to paretovariate", args)


def handle_weibullvariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to weibullvariate", args)


# Placeholders:

def placeholder_randrange(start, stop, step):
    rng = range(start, stop, step)
    return rng[len(rng) // 2]


def placeholder_choice(choices):
    return _coconut_igetitem(choices, len(choices) // 2)


def placeholder_uniform(start, stop):
    return (start + stop) / 2


def placeholder_triangular(low, high, mode):
    return mode


def placeholder_betavariate(alpha, beta):
    return alpha / (alpha + beta)


def placeholder_expovariate(lambd):
    return 1 / lambd


def placeholder_gammavariate(alpha, beta):
    return alpha / beta


def placeholder_normalvariate(mu, sigma):
    return mu


def placeholder_vonmisesvariate(mu, kappa):
    return mu


def placeholder_paretovariate(alpha):
    return 1 if alpha <= 1 else alpha / (alpha - 1)


def placeholder_weibullvariate(alpha, beta):
    return alpha * ln(2)**(1 / beta)


# Processor:

class ParamProcessor(_coconut.object):
    """Processes param keyword arguments."""
    handlers = {"randrange": handle_randrange, "choice": handle_choice, "uniform": handle_uniform, "triangular": handle_triangular, "betavariate": handle_betavariate, "expovariate": handle_expovariate, "gammavariate": handle_gammavariate, "normalvariate": handle_normalvariate, "vonmisesvariate": handle_vonmisesvariate, "paretovariate": handle_paretovariate, "weibullvariate": handle_weibullvariate}
    placeholder_funcs = {"randrange": placeholder_randrange, "choice": placeholder_choice, "uniform": placeholder_uniform, "triangular": placeholder_triangular, "betavariate": placeholder_betavariate, "expovariate": placeholder_expovariate, "gammavariate": placeholder_gammavariate, "normalvariate": placeholder_normalvariate, "vonmisesvariate": placeholder_vonmisesvariate, "paretovariate": placeholder_paretovariate, "weibullvariate": placeholder_weibullvariate}

    def modify_kwargs(self, func, kwargs):
        """Apply func to all kwargs with values in the random function's domain."""
        new_kwargs = {}
        for k, v in kwargs.items():
            if k in self.handlers:
                new_kwargs[k] = map(func, v)
            else:
                new_kwargs[k] = func(v)
        return new_kwargs

    def standardize_args(self, func, args):
        """Standardize param func and args."""
# denumpy args
        args = denumpy_all(args)

# standardize arguments to a list
        args = list(args)

# detect invalid funcs
        if func not in self.handlers:
            raise ValueError("unknown parameter definition function {_coconut_format_0}".format(_coconut_format_0=(func)))

# run handler
        result = self.handlers[func](args)
        args = result if result is not None else args

        return args

    def standardize_kwargs(self, kwargs):
        """Standardizes param keyword args."""
        return fmap(lambda k, v: denumpy_all((k, v)), kwargs)

    def choose_default_placeholder(self, name, func, *args, **kwargs):
        """Choose a default placeholder_when_missing value for the given parameter."""
        if func not in self.placeholder_funcs:
            raise ValueError("unknown parameter definition function {_coconut_format_0}".format(_coconut_format_0=(func)))
        return self.placeholder_funcs[func](*args)


param_processor = ParamProcessor()
