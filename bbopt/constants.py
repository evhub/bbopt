#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc6424c9f

# Compiled with Coconut version 1.3.0-post_dev3 [Dead Parrot]

"""
Constants for use across all of bbopt.
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
version = "0.1.0"
description = "Black box optimization made simple."
github_url = "https://github.com/evhub/bbopt"
author = "Evan Hubinger"
author_email = "evanjhub@gmail.com"
classifiers = ("Development Status :: 3 - Alpha", "License :: OSI Approved :: Apache Software License", "Topic :: Software Development :: Libraries :: Python Modules", "Operating System :: OS Independent",)
requirements = ()
extra_requirements = {"scikit-optimize": ("scikit-optimize",)}

# Interface constants:

default_backend = "serving"
data_file_ext = ".bbopt.json"
