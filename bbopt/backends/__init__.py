#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8546572c

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
Backends contains all of bbopt's different backends.
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



registered_backends = {}

def init_backend(name, examples, params, **kwargs):
    """Create a backend object of the given name with the given example data."""
    if name in registered_backends:
        return registered_backends[name]
    elif name == "serving":
        from bbopt.backends.serving import ServingBackend as Backend
    elif name == "random":
        from bbopt.backends.random import RandomBackend as Backend
    elif name == "scikit-optimize":
        from bbopt.backends.skopt import SkoptBackend as Backend
    else:
        raise ValueError("unknown backend %r" % name)
    return Backend(examples, params, **kwargs)

def register_backend(name, backend):
    """Register a new backend under the given name."""
    registered_backends[name] = backend
