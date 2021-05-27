#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb178b832

# Compiled with Coconut version 1.5.0-post_dev52 [Fish License]

"""
BBopt command line interface.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_module_name = _coconut_os_path.splitext(_coconut_os_path.basename(_coconut_file_path))[0]
if not _coconut_module_name or not _coconut_module_name[0].isalpha() or not all (c.isalpha() or c.isdigit() for c in _coconut_module_name):
    raise ImportError("invalid Coconut package name " + repr(_coconut_module_name) + " (pass --standalone to compile as individual files rather than a package)")
_coconut_cached_module = _coconut_sys.modules.get(str(_coconut_module_name + ".__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str(_coconut_module_name + ".__coconut__")]
_coconut_sys.path.insert(0, _coconut_os_path.dirname(_coconut_file_path))
exec("from " + _coconut_module_name + ".__coconut__ import *")
exec("from " + _coconut_module_name + ".__coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable")
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import os
sys = _coconut_sys
import argparse
import subprocess
from pprint import pprint

if sys.version_info >= (3, 3):
    from concurrent.futures.process import BrokenProcessPool
else:
    BrokenProcessPool = KeyboardInterrupt

from bbopt import constants
from bbopt.optimizer import BlackBoxOptimizer


parser = argparse.ArgumentParser(prog="bbopt", description=constants.description)

parser.add_argument("file", metavar="file", type=str, help="path to the Python file to run")

parser.add_argument("-n", "--num-trials", metavar="trials", type=int, default=constants.default_trials, help="number of trials to run (defaults to {_coconut_format_0})".format(_coconut_format_0=(constants.default_trials)))

parser.add_argument("-j", "--jobs", metavar="processes", type=int, default=constants.default_jobs, help="number of processes to use (defaults to {_coconut_format_0})".format(_coconut_format_0=(constants.default_jobs)))

parser.add_argument("-q", "--quiet", action="store_true", help="suppress all informational output")

parser.add_argument("--python", metavar="executable", type=str, default=sys.executable, help="the python executable to use (defaults to the current python)")

parser.add_argument("--args", type=str, nargs=argparse.REMAINDER, help="arguments to pass to the file being run")


def base_show(quiet, msg):
    """Show the given message with [BBopt] if not quiet."""
    if not quiet:
        print("[BBopt]", msg)


def run_trial(args, cmd, i):
    """Pickleable function for running trials in parallel."""
    try:
        show = _coconut.functools.partial(base_show, args.quiet)
        show("{_coconut_format_0}/{_coconut_format_1} starting...".format(_coconut_format_0=(i + 1), _coconut_format_1=(args.num_trials)))
        subprocess.check_call(cmd)
        show("{_coconut_format_0}/{_coconut_format_1} finished.".format(_coconut_format_0=(i + 1), _coconut_format_1=(args.num_trials)))
    except BrokenProcessPool as err:
        raise KeyboardInterrupt(str(err))


def main(*args, **kwargs):
    args = parser.parse_args(*args, **kwargs)
    if not os.path.isfile(args.file):
        raise ValueError("could not find file {_coconut_format_0}".format(_coconut_format_0=(args.file)))

    show = _coconut.functools.partial(base_show, args.quiet)
    cmd = [args.python, args.file] + ((lambda _coconut_x: [] if _coconut_x is None else _coconut_x)(args.args))

    cmd_str = " ".join(cmd)
    show("Running {_coconut_format_0} trials using {_coconut_format_1} process(es) of:\n\t> {_coconut_format_2}".format(_coconut_format_0=(args.num_trials), _coconut_format_1=(args.jobs), _coconut_format_2=(cmd_str)))

    if args.jobs <= 1:
        (consume)((map)(_coconut.functools.partial(run_trial, args, cmd), range(args.num_trials)))
    else:
        with parallel_map.multiple_sequential_calls(max_workers=args.jobs):
            (consume)((parallel_map)(_coconut.functools.partial(run_trial, args, cmd), range(args.num_trials)))


    if not args.quiet:
        bb = BlackBoxOptimizer(args.file)
        rel_data_file = os.path.relpath(bb.data_file)
        show("Black box optimization finished; data saved to {_coconut_format_0}.".format(_coconut_format_0=(rel_data_file)))

        best_example = bb.get_best_run()
        show("Summary of best run:")
        pprint(bb.get_best_run())
