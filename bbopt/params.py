#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2e206f4a

# Compiled with Coconut version 1.4.0-post_dev7 [Ernest Scribbler]

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
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



import functools

from bbopt.util import Num
from bbopt.util import json_serialize
from bbopt.util import format_err
from bbopt.util import all_isinstance


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


def handle_sample(args):
    if len(args) != 2 or not isinstance(args[0], list) or not isinstance(args[1], int):
        raise format_err(ValueError, "invalid arguments to sample", args)


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


def handle_lognormvariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to lognormvariate", args)


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
    ignored = ["guess", "placeholder_when_missing",]
    handlers = {"randrange": handle_randrange, "choice": handle_choice, "sample": handle_sample, "uniform": handle_uniform, "triangular": handle_triangular, "betavariate": handle_betavariate, "expovariate": handle_expovariate, "gammavariate": handle_gammavariate, "normalvariate": handle_normalvariate, "lognormvariate": handle_lognormvariate, "vonmisesvariate": handle_vonmisesvariate, "paretovariate": handle_paretovariate, "weibullvariate": handle_weibullvariate}

    def supported_funcs(self):
        """Return an iterator of all random functions that backends should support."""
        _coconut_yield_from = self.handlers
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


    def modify_kwargs(self, func, kwargs):
        """Apply func to all kwargs with values in the random function's domain."""
        new_kwargs = {}
        for k, v in kwargs.items():
            if k in self.handlers:
# random functions hold lots of arguments, so map the function over them
                new_kwargs[k] = map(func, v)
            elif k in self.ignored:
# ignored kwargs hold extra parameters, so call the function on them
                new_kwargs[k] = func(v)
            else:
# otherwise, just pass the kwarg through
                new_kwargs[k] = v
        return new_kwargs

    def filter_kwargs(self, kwargs):
        """Remove ignored keyword args."""
        new_kwargs = {}
        for k, v in kwargs.items():
            if k not in self.ignored:
                new_kwargs[k] = v
        return new_kwargs

    def only_random_function_kwargs(self, param_func):
        """Wrap the given param_func by filtering out non-function kwargs."""
        @functools.wraps(param_func)
        def wrapped_param_func(*args, **kwargs):
            return param_func(*args, **self.filter_kwargs(kwargs))
        return wrapped_param_func

    def implements_params(self, param_func, backend_name, implemented_params):
        """Wrap the given param_func with a check that only implemented parameters are passed."""
        implemented_param_set = set(implemented_params)
        assert implemented_param_set <= set(self.supported_funcs())
        @functools.wraps(param_func)
        def wrapped_param_func(*args, **kwargs):
            filtered_kwarg_set = (set)((self.filter_kwargs)(kwargs))
            if not filtered_kwarg_set < implemented_param_set:
                raise TypeError("the {} backend does not implement the {} function(s)".format(backend_name, ", ".join(filtered_kwarg_set)))
            return param_func(*args, **kwargs)
        return wrapped_param_func

    def standardize_kwargs(self, kwargs):
        """Standardizes param keyword args."""
        new_kwargs = {}
        saw_func = None
        for func, args in json_serialize(kwargs).items():
# pass through ignored kwargs
            if func in self.ignored:
                new_kwargs[func] = args
                continue

# only allow one function
            if saw_func is not None:
                raise ValueError("cannot have both {} and {} for a single param".format(saw_func, func))

# standardize arguments to a list
            if not isinstance(args, list):
                args = [args]

# run handlers
            if func in self.handlers:
                result = self.handlers[func](args)
                args = result if result is not None else args
            else:
                raise TypeError("unknown param option {}".format(func))

            new_kwargs[func] = args
            saw_func = func

# require some function
        if saw_func is None:
            raise TypeError("param requires a keyword option of the form <random function>=<args>")

        return (json_serialize)(new_kwargs)


param_processor = ParamProcessor()
