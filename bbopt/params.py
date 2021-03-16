#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x203e2d57

# Compiled with Coconut version 1.5.0-post_dev7 [Fish License]

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
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



if _coconut_sys.version_info < (3, 3):
    from collections import Iterable
else:
    from collections.abc import Iterable
from math import pi
from math import log as ln

from bbopt import constants
from bbopt.util import Num
from bbopt.util import format_err
from bbopt.util import all_isinstance
from bbopt.util import denumpy_all
from bbopt.util import printerr


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
    return choices[len(choices) // 2]


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


# Support checkers:


def support_check_randrange(val, start, stop, step):
    return val in range(start, stop, step)


def support_check_choice(val, choices):
    return val in choices


def support_check_uniform(val, start, stop):
    return start <= val <= stop or stop <= val <= start


def support_check_triangular(val, low, high, mode):
    return low <= val <= high


def support_check_betavariate(val, alpha, beta):
    return 0 <= val <= 1


def support_check_expovariate(val, lambd):
    return val >= 0 if lambd >= 0 else val <= 0


def support_check_gammavariate(val, alpha, beta):
    return val > 0


def support_check_normalvariate(val, mu, sigma):
    return True


def support_check_vonmisesvariate(val, mu, kappa):
    return 0 <= val <= 2 * pi


def support_check_paretovariate(val, alpha):
    return val >= 1


def support_check_weibullvariate(val, alpha, beta):
    return val >= 0


# Processor:

class ParamProcessor(_coconut.object):
    """Processes param keyword arguments."""

    def __init__(self):
        self.handlers = {}
        self.placeholder_funcs = {}
        self.support_checkers = {}

    def register(self, func, handler, placeholder_generator, support_check_func, replace=False):
        """Register a new parameter definition function. See bbopt.params for examples."""
        if not replace and func in self.handlers:
            raise ValueError("cannot register already existing parameter definition function {_coconut_format_0!r}".format(_coconut_format_0=(func)))
        self.handlers[func] = handler
        self.placeholder_funcs[func] = placeholder_generator
        self.support_checkers[func] = support_check_func

    def verify_support(self, name, val, func, *args, **kwargs):
        if func not in self.support_checkers:
            raise ValueError("unknown parameter definition function {_coconut_format_0} (register with bbopt.params.param_processor.register)".format(_coconut_format_0=(func)))
        if not self.support_checkers[func](val, *args):
            printerr("BBopt Warning: {_coconut_format_0} not in support of {_coconut_format_1}(*{_coconut_format_2}) for parameter {_coconut_format_3} (adjust parameter definition to ensure support is always maximally broad)".format(_coconut_format_0=(val), _coconut_format_1=(func), _coconut_format_2=(args), _coconut_format_3=(name)))
            if constants.use_placeholder_when_outside_support:
                val = kwargs.get("placeholder_when_missing", self.choose_default_placeholder(name, func, *args, **kwargs))
        return val

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
            raise ValueError("unknown parameter definition function {_coconut_format_0} (register with bbopt.params.param_processor.register)".format(_coconut_format_0=(func)))

# run handler
        result = self.handlers[func](args)
        args = result if result is not None else args

        return args

    def standardize_kwargs(self, kwargs):
        """Standardizes param keyword args."""
        return (fmap)(lambda k, v: denumpy_all((k, v)), kwargs)

    def choose_default_placeholder(self, name, func, *args, **kwargs):
        """Choose a default placeholder_when_missing value for the given parameter."""
        if func not in self.placeholder_funcs:
            raise ValueError("unknown parameter definition function {_coconut_format_0} (register with bbopt.params.param_processor.register)".format(_coconut_format_0=(func)))
        return self.placeholder_funcs[func](*args)


# Registration:

param_processor = ParamProcessor()

param_processor.register("randrange", handle_randrange, placeholder_randrange, support_check_randrange)
param_processor.register("choice", handle_choice, placeholder_choice, support_check_choice)
param_processor.register("uniform", handle_uniform, placeholder_uniform, support_check_uniform)
param_processor.register("triangular", handle_triangular, placeholder_triangular, support_check_triangular)
param_processor.register("betavariate", handle_betavariate, placeholder_betavariate, support_check_betavariate)
param_processor.register("expovariate", handle_expovariate, placeholder_expovariate, support_check_expovariate)
param_processor.register("gammavariate", handle_gammavariate, placeholder_gammavariate, support_check_gammavariate)
param_processor.register("normalvariate", handle_normalvariate, placeholder_normalvariate, support_check_normalvariate)
param_processor.register("vonmisesvariate", handle_vonmisesvariate, placeholder_vonmisesvariate, support_check_vonmisesvariate)
param_processor.register("paretovariate", handle_paretovariate, placeholder_paretovariate, support_check_paretovariate)
param_processor.register("weibullvariate", handle_weibullvariate, placeholder_weibullvariate, support_check_weibullvariate)
