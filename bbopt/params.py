#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa53a40d3

# Compiled with Coconut version 1.4.0-post_dev23 [Ernest Scribbler]

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
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import functools
if _coconut_sys.version_info < (3, 3):
    from collections import Iterable
else:
    from collections.abc import Iterable

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
    return [start, stop, step]


def handle_choice(args):
    if len(args) != 1 or not isinstance(args[0], list):
        raise format_err(ValueError, "invalid arguments to choice", args)


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


# Processor:

class ParamProcessor(_coconut.object):
    """Processes param keyword arguments."""
    handlers = {"randrange": handle_randrange, "choice": handle_choice, "uniform": handle_uniform, "triangular": handle_triangular, "betavariate": handle_betavariate, "expovariate": handle_expovariate, "gammavariate": handle_gammavariate, "normalvariate": handle_normalvariate, "vonmisesvariate": handle_vonmisesvariate, "paretovariate": handle_paretovariate, "weibullvariate": handle_weibullvariate}

    @property
    def supported_funcs(self):
        return list(self.handlers)

    def modify_kwargs(self, func, kwargs):
        """Apply func to all kwargs with values in the random function's domain."""
        new_kwargs = {}
        for k, v in kwargs.items():
            if k in self.supported_funcs:
                new_kwargs[k] = map(func, v)
            else:
                new_kwargs[k] = func(v)
        return new_kwargs

    def standardize_kwargs(self, kwargs):
        """Standardizes param keyword args."""
        new_kwargs = {}
        saw_func = None
        for func, args in kwargs.items():
# denumpy args
            args = denumpy_all(args)

# pass through non-function kwargs
            if func not in self.supported_funcs:
                new_kwargs[func] = args
                continue

# only allow one function
            if saw_func is not None:
                raise ValueError("cannot have both {} and {} for a single param".format(saw_func, func))

# standardize arguments to a list
            if isinstance(args, Iterable):
                args = list(args)
            else:
                args = [args]

# run handlers
            result = self.handlers[func](args)
            args = result if result is not None else args

            new_kwargs[func] = args
            saw_func = func

# require some function
        if saw_func is None:
            raise TypeError("param requires a keyword option of the form <random function>=<args>")

        return new_kwargs

    def split_kwargs(self, kwargs):
        """Processes kwargs into func, args, options."""
        func = None
        args = ()
        options = {}
        for k, v in kwargs.items():
            if k in self.supported_funcs:
                func = k
                args = v
            else:
                options[k] = v
        return func, args, options

    def splitting_kwargs(self, base_func, ignore_options=False):
        """Turns base_func(*args, **kwargs) into base_func(*args, func, args, **options)."""
        @functools.wraps(base_func)
        def wrapped_func(*args, **kwargs):
            func, func_args, options = self.split_kwargs(kwargs)
            if ignore_options:
                options = {}
            args = args + (func, func_args)
            return base_func(*args, **options)
        return wrapped_func

    def implements_params(self, base_func, backend_name, implemented_funcs, supported_options):
        """Ensures base_func is only called with the given funcs and options."""
        supported_option_set = set(supported_options)
        @functools.wraps(base_func)
        def wrapped_func(*args, **kwargs):
            func, func_args, options = self.split_kwargs(kwargs)

            if func not in implemented_funcs:
                raise ValueError("the {} backend does not implement the {} function".format(backend_name, func))

            unsupported_options = set(options) - supported_option_set
            if unsupported_options:
                raise ValueError("the {} backend does not support the {} option(s)".format(backend_name, unsupported_options))

            return base_func(*args, **kwargs)
        return wrapped_func


param_processor = ParamProcessor()
