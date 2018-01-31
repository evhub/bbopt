#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x8e4905bb

# Compiled with Coconut version 1.3.1-post_dev14 [Dead Parrot]

"""
Constants for use across all of BBopt.
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



# Installation constants:

name = "bbopt"
version = "0.2.5"
description = "The easiest hyperparameter optimization you'll ever do."
github_url = "https://github.com/evhub/bbopt"
author = "Evan Hubinger"
author_email = "evanjhub@gmail.com"
classifiers = ("Development Status :: 3 - Alpha", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent",)
requirements = ()
extra_requirements = {"scikit-optimize": ("scikit-optimize",), "hyperopt": ("hyperopt", "networkx<2.0",)}
extra_requirements["all"] = (tuple)(reduce(_coconut.operator.or_, map(set, extra_requirements.values())))

# Optimizer constants:

data_file_ext = ".bbopt.json"
