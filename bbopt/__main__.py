#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xac10a0c1

# Compiled with Coconut version 1.4.0-post_dev3 [Ernest Scribbler]

"""
BBopt command line interface.
"""

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



import os
import argparse
import subprocess

from bbopt.constants import description
from bbopt.constants import default_trials
from bbopt.optimizer import BlackBoxOptimizer


parser = argparse.ArgumentParser(prog="bbopt", description=description)

parser.add_argument("file", metavar="file", type=str, help="path of the Python file to run")

parser.add_argument("-n", "--num-trials", metavar="trials", type=int, default=default_trials, help="number of trials to run (defaults to {})".format(default_trials))

parser.add_argument("-q", "--quiet", action="store_true", help="suppress all informational output")

parser.add_argument("--python", metavar="executable", type=str, default="python", help="the python executable to use for running the file (defaults to 'python')")

parser.add_argument("--args", type=str, nargs=argparse.REMAINDER, help="arguments to pass to the file being run")


def main():
    args = parser.parse_args()
    if not os.path.isfile(args.file):
        raise ValueError("could not find file {}".format(args.file))

    def show(msg):
        if not args.quiet:
            print(msg)

    show("[BBopt] Starting black box optimization of {}...".format(args.file))

    for i in range(args.num_trials):
        show("[BBopt] Running black box optimization trial {}/{}...".format(i + 1, args.num_trials))

        cmd = [args.python, args.file] + ((lambda _coconut_none_coalesce_item: [] if _coconut_none_coalesce_item is None else _coconut_none_coalesce_item)(args.args))
        show("> {}".format(" ".join(cmd)))
        subprocess.check_call(cmd)

    show("[BBopt] Black box optimization finished; data saved to {}.".format(BlackBoxOptimizer(args.file).data_file))


if __name__ == "__main__":
    main()
