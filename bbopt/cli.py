#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4d96a62c

# Compiled with Coconut version 2.0.0-a_dev53 [How Not to Be Seen]

"""
BBopt command line interface.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:  # type: ignore
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_dir)
_coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
    _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
    import __coconut__ as _coconut__coconut__
    _coconut__coconut__.__name__ = _coconut_full_module_name
    for _coconut_v in vars(_coconut__coconut__).values():
        if getattr(_coconut_v, "__module__", None) == str("__coconut__"):
            try:
                _coconut_v.__module__ = _coconut_full_module_name
            except AttributeError:
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import os  #5 (line num in coconut source)
sys = _coconut_sys  #6 (line num in coconut source)
import argparse  #7 (line num in coconut source)
import subprocess  #8 (line num in coconut source)
from pprint import pprint  #9 (line num in coconut source)

if sys.version_info >= (3, 3):  #11 (line num in coconut source)
    from concurrent.futures.process import BrokenProcessPool  #12 (line num in coconut source)
else:  #13 (line num in coconut source)
    BrokenProcessPool = KeyboardInterrupt  #14 (line num in coconut source)

from bbopt import constants  #16 (line num in coconut source)
from bbopt.optimizer import BlackBoxOptimizer  #17 (line num in coconut source)


parser = argparse.ArgumentParser(prog="bbopt", description=constants.description)  #20 (line num in coconut source)

parser.add_argument("file", metavar="file", type=str, help="path to the Python file to run")  #25 (line num in coconut source)

parser.add_argument("-n", "--num-trials", metavar="trials", type=int, default=constants.default_trials, help="number of trials to run (defaults to {_coconut_format_0})".format(_coconut_format_0=(constants.default_trials)))  #32 (line num in coconut source)

parser.add_argument("-j", "--jobs", metavar="processes", type=int, default=constants.default_jobs, help="number of processes to use (defaults to {_coconut_format_0})".format(_coconut_format_0=(constants.default_jobs)))  #40 (line num in coconut source)

parser.add_argument("-q", "--quiet", action="store_true", help="suppress all informational output")  #48 (line num in coconut source)

parser.add_argument("--python", metavar="executable", type=str, default=sys.executable, help="the python executable to use (defaults to the current python)")  #54 (line num in coconut source)

parser.add_argument("--args", type=str, nargs=argparse.REMAINDER, help="arguments to pass to the file being run")  #62 (line num in coconut source)

parser.add_argument("-v", "--version", action="version", version="%(prog)s " + constants.version)  #69 (line num in coconut source)


def base_show(quiet, msg):  #76 (line num in coconut source)
    """Show the given message with [BBopt] if not quiet."""  #77 (line num in coconut source)
    if not quiet:  #78 (line num in coconut source)
        print("[BBopt]", msg)  #79 (line num in coconut source)



def run_trial(args, cmd, i):  #82 (line num in coconut source)
    """Pickleable function for running trials in parallel."""  #83 (line num in coconut source)
    try:  #84 (line num in coconut source)
        show = _coconut.functools.partial(base_show, args.quiet)  #85 (line num in coconut source)

        show("{_coconut_format_0}/{_coconut_format_1} starting...".format(_coconut_format_0=(i + 1), _coconut_format_1=(args.num_trials)))  #87 (line num in coconut source)

        sub_proc_env = os.environ.copy()  #89 (line num in coconut source)
        sub_proc_env[py_str(constants.run_id_env_var)] = py_str(i)  #90 (line num in coconut source)
        subprocess.check_call(cmd, env=sub_proc_env)  #91 (line num in coconut source)

        show("{_coconut_format_0}/{_coconut_format_1} finished.".format(_coconut_format_0=(i + 1), _coconut_format_1=(args.num_trials)))  #93 (line num in coconut source)

    except BrokenProcessPool as err:  #95 (line num in coconut source)
        raise KeyboardInterrupt(str(err))  #96 (line num in coconut source)



def main(*args, **kwargs):  #99 (line num in coconut source)
    args = parser.parse_args(*args, **kwargs)  #100 (line num in coconut source)
    if not os.path.isfile(args.file):  #101 (line num in coconut source)
        raise ValueError("could not find file {_coconut_format_0}".format(_coconut_format_0=(args.file)))  #102 (line num in coconut source)

    show = _coconut.functools.partial(base_show, args.quiet)  #104 (line num in coconut source)
    cmd = [args.python, args.file] + ((lambda _coconut_x: [] if _coconut_x is None else _coconut_x)(args.args))  #105 (line num in coconut source)

    cmd_str = " ".join(cmd)  #107 (line num in coconut source)
    show("Running {_coconut_format_0} trials using {_coconut_format_1} process(es) of:\n\t> {_coconut_format_2}".format(_coconut_format_0=(args.num_trials), _coconut_format_1=(args.jobs), _coconut_format_2=(cmd_str)))  #108 (line num in coconut source)

    if args.jobs <= 1:  #110 (line num in coconut source)
        (consume)((map)(_coconut.functools.partial(run_trial, args, cmd), range(args.num_trials)))  #111 (line num in coconut source)
    else:  #112 (line num in coconut source)
        with parallel_map.multiple_sequential_calls(max_workers=args.jobs):  #113 (line num in coconut source)
            (consume)((parallel_map)(_coconut.functools.partial(run_trial, args, cmd), range(args.num_trials)))  #114 (line num in coconut source)

    if not args.quiet:  #116 (line num in coconut source)
        bb = BlackBoxOptimizer(args.file)  #117 (line num in coconut source)
        rel_data_file = os.path.relpath(bb.data_file)  #118 (line num in coconut source)
        show("Black box optimization finished; data saved to {_coconut_format_0}.".format(_coconut_format_0=(rel_data_file)))  #119 (line num in coconut source)

        best_example = bb.get_best_run()  #121 (line num in coconut source)
        show("Summary of best run:")  #122 (line num in coconut source)
        pprint(bb.get_best_run())  #123 (line num in coconut source)
