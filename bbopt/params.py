#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x286b50da

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
Handles standardizing param calls to use standard library random functions.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



# Imports:

from bbopt.util import Num
from bbopt.util import json_serialize
from bbopt.util import format_err
from bbopt.util import all_isinstance

# Handlers:

def handle_randrange(args):
    if not all_isinstance(args, int):
        raise format_err(ValueError, "invalid arguments to randrange", args)
    if len(args) == 1:
        start, stop, step = 0, args[0], 1
    elif len(args) == 2:
        start, stop, step = args[0], args[1], 1
    elif len(args) == 3:
        start, stop, step = args
    else:
        raise format_err(ValueError, "invalid arguments to randrange", args)
    return [start, stop, step]

def handle_choice(args):
    if len(args) != 1 or not isinstance(args[0], list):
        raise format_err(ValueError, "invalid arguments to choice", args)
    return args

def handle_sample(args):
    if len(args) != 2 or not isinstance(args[0], list) or not isinstance(args[1], int):
        raise format_err(ValueError, "invalid arguments to sample", args)
    return args

def handle_uniform(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to uniform", args)
    return args

def handle_triangular(args):
    if len(args) != 3 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to triangular", args)
    return args

def handle_betavariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to betavariate", args)
    return args

def handle_expovariate(args):
    if len(args) != 1 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to expovariate", args)
    return args

def handle_gammavariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to gammavariate", args)
    return args

def handle_normalvariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to normalvariate", args)
    return args

def handle_lognormvariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to lognormvariate", args)
    return args

def handle_vonmisesvariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to vonmisesvariate", args)
    return args

def handle_paretovariate(args):
    if len(args) != 1 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to paretovariate", args)
    return args

def handle_weibullvariate(args):
    if len(args) != 2 or not all_isinstance(args, Num):
        raise format_err(ValueError, "invalid arguments to weibullvariate", args)
    return args

# Functions:

class ParamProcessor(_coconut.object):
    """Processes param keyword arguments."""
    ignored = ["guess", "placeholder_when_missing",]
    handlers = {"randrange": handle_randrange, "choice": handle_choice, "sample": handle_sample, "uniform": handle_uniform, "triangular": handle_triangular, "betavariate": handle_betavariate, "expovariate": handle_expovariate, "gammavariate": handle_gammavariate, "normalvariate": handle_normalvariate, "lognormvariate": handle_lognormvariate, "vonmisesvariate": handle_vonmisesvariate, "paretovariate": handle_paretovariate, "weibullvariate": handle_weibullvariate}

    def supported_funcs(self):
        """List all random functions that backends should support."""
        return list(handlers)

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
                raise ValueError("cannot have both %s and %s for a single param" % (saw_func, func))

# standardize arguments to a list
            if not isinstance(args, list):
                args = [args]

# run handlers
            if func in self.handlers:
                args = self.handlers[func](args)
            else:
                raise TypeError("unknown param option %r" % func)

            new_kwargs[func] = args
            saw_func = func

# require some function
        if saw_func is None:
            raise TypeError("param requires a keyword option of the form <random function>=<args>")

        return (json_serialize)(new_kwargs)

param_processor = ParamProcessor()
