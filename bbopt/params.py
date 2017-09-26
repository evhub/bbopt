#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2950e746

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

# Functions:

def standardize_kwargs(kwargs):
    """Standardizes param keyword args."""
    stdkwargs = {}
    saw_random_func = None
    for func, args in json_serialize(kwargs).items():
        orig_func, orig_args = func, args

# standardize arguments to a list
        if not isinstance(args, list):
            args = [args]

# alias randint, random, and normalvariate calls
        if func == "randint":  # randint -> randrange
            if len(args) == 0 or len(args) > 3 or not all_isinstance(args, int):
                raise format_err(ValueError, "invalid arguments to randint", randint)
            func = "randrange"
            args[-1] += 1
        elif func == "random":  # random -> uniform
            if args:
                raise format_err(ValueError, "invalid arguments to random", random)
            func, args = "uniform", [0, 1]
        elif func == "gauss":  # gauss -> normalvariate
            if len(args) != 2 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to gauss", gauss)
            func = "normalvariate"

# process standard random functions
        got_random_func = True
        if func == "getrandbits":
            if len(args) != 1 or not isinstance(args[0], int):
                raise format_err(ValueError, "invalid arguments to getrandbits", getrandbits)
        elif func == "randrange":
            if not all_isinstance(args, int):
                raise format_err(ValueError, "invalid arguments to randrange", randrange)
            if len(args) == 1:
                start, stop, step = 0, args[0], 1
            elif len(args) == 2:
                start, stop, step = args[0], args[1], 1
            elif len(args) == 3:
                start, stop, step = args
            else:
                raise format_err(ValueError, "invalid arguments to randrange", randrange)
            args = [start, stop, step]
        elif func == "choice":
            if len(args) != 1 or not isinstance(args[0], list):
                raise format_err(ValueError, "invalid arguments to choice", choice)
        elif func == "sample":
            if len(args) != 2 or not isinstance(args[0], list) or not isinstance(args[1], int):
                raise format_err(ValueError, "invalid arguments to sample", sample)
        elif func == "uniform":
            if len(args) != 2 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to uniform", uniform)
        elif func == "triangular":
            if len(args) != 3 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to triangular", triangular)
        elif func == "betavariate":
            if len(args) != 2 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to betavariate", betavariate)
        elif func == "expovariate":
            if len(args) != 1 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to expovariate", expovariate)
        elif func == "gammavariate":
            if len(args) != 2 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to gammavariate", gammavariate)
        elif func == "normalvariate":
            if len(args) != 2 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to normalvariate", normalvariate)
        elif func == "lognormvariate":
            if len(args) != 2 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to lognormvariate", lognormvariate)
        elif func == "vonmisesvariate":
            if len(args) != 2 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to vonmisesvariate", vonmisesvariate)
        elif func == "paretovariate":
            if len(args) != 1 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to paretovariate", paretovariate)
        elif func == "weibullvariate":
            if len(args) != 2 or not all_isinstance(args, Num):
                raise format_err(ValueError, "invalid arguments to weibullvariate", weibullvariate)
        else:
            got_random_func = False

# disallow multiple random functions and ignore other parameters
        if saw_random_func and got_random_func:
            raise ValueError("cannot have both %s and %s for a single parameter" % (saw_random_func, func))
        elif got_random_func:
            saw_random_func = func
            stdkwargs[func] = args
        else:
            stdkwargs[orig_func] = orig_args

# require some random function
    if saw_random_func is None:
        raise TypeError("param requires a keyword option of the form random_function=args")
    return stdkwargs
