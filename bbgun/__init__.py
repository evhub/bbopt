#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x443d2782

# Compiled with Coconut version 1.3.0-post_dev2 [Dead Parrot]

"""
BBGun is a universal black box optimization library.

To use BBGun, just add

    # BBGun boilerplate:
    from bbgun import BB
    bb = BB(file=__file__)
    if __name__ == "__main__":
        bb.run(backend=<your backend here>)

to the top of your file, then call

    x = bb.param(name="x", <your parameters here>)

for each of the tunable parameters in your model, and finally add

    bb.maximize(x)      or      bb.minimize(x)

to set the value being optimized. Then, run

    python <your file here>

to train your model, and just

    import <your module here>

to serve it.
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



from bbgun.interface import BB
