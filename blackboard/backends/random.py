#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x1981faa8

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
The random backend. Used for testing purposes.
Does not use existing data, simply spits out random valid values.
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

sys = _coconut_sys
import random

# Backend:

class RandomBackend(_coconut.object):
    """The random backend chooses parameter values randomly."""

    def __init__(self, examples=None, params=None):
        pass  # we're choosing randomly, so we ignore everything

    random_functions = {"getrandbits": (random.getrandbits, False), "randrange": (random.randrange, False), "randint": (random.randint, False), "choice": (random.choice, True), "sample": (random.sample, False), "random": (random.random, False), "uniform": (random.uniform, False), "triangular": (random.triangular, False), "betavariate": (random.betavariate, False), "expovariate": (random.expovariate, False), "gammavariate": (random.gammavariate, False), "gauss": (random.gauss, False), "lognormvariate": (random.lognormvariate, False), "vonmisesvariate": (random.vonmisesvariate, False), "paretovariate": (random.paretovariate, False), "weibullvariate": (random.weibullvariate, False)}
    if sys.version_info > (3,):
        random_functions["choices"] = (random.choices, False)

    def call_random(self, cmd, args):
        """Call the random function cmd with the arguments args."""
        func, takes_iterable = self.random_functions[cmd]
        if takes_iterable or not isinstance(args, (list, tuple)):
            return func(args)
        else:
            return func(*args)

    def param(self, name=None, **kwargs):
        if len(kwargs) != 1:
            raise TypeError("the random backend requires exactly one parameter," " <name of the random function to call>=<argument(s) to that function>")
        cmd, args = _coconut_igetitem(kwargs.items(), 0)
        if cmd not in self.random_functions:
            raise ValueError("unknown random function %r" % cmd)
        return self.call_random(cmd, args)
