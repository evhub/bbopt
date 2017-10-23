#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x20b71b28

# Compiled with Coconut version 1.3.1 [Dead Parrot]

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------

# BBopt boilerplate:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run(backend="scikit-optimize")

use_high = bb.randbool("use high", guess=False)
assert isinstance(use_high, bool)
if use_high:
    reward = bb.randrange("x high", 10, 20, placeholder_when_missing=10)
else:
    reward = bb.randrange("x low", 10, placeholder_when_missing=0)

bb.maximize(reward)

if __name__ == "__main__":
    print(repr(reward))
