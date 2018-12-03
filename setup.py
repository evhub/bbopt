#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa28512ff

# Compiled with Coconut version 1.4.0-post_dev2 [Ernest Scribbler]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

import setuptools

sys = _coconut_sys
import os.path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from bbopt.constants import name
from bbopt.constants import version
from bbopt.constants import description
from bbopt.constants import github_url
from bbopt.constants import author
from bbopt.constants import author_email
from bbopt.constants import requirements
from bbopt.constants import classifiers
from bbopt.constants import extra_requirements


setuptools.setup(name=name, version=version, description=description, url=github_url, author=author, author_email=author_email, classifiers=(list)(classifiers), packages=setuptools.find_packages(), install_requires=(list)(requirements), extras_require=fmap(lambda k, v: (k, list(v)), extra_requirements))
