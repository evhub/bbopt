#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x50ce882

# Compiled with Coconut version 1.4.0-post_dev23 [Ernest Scribbler]

"""
The hyperopt backend. Does black box optimization using hyperopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import numpy as np

from hyperopt import hp
from hyperopt import tpe
from hyperopt import FMinIter
from hyperopt.pyll import as_apply
from hyperopt.base import Domain
from hyperopt.base import Trials
from hyperopt.base import STATUS_OK
from hyperopt.base import STATUS_RUNNING
from hyperopt.base import JOB_STATE_DONE
from hyperopt.base import spec_from_misc

from bbopt.util import sorted_items
from bbopt.backends.random import RandomBackend
from bbopt.backends.util import negate_objective
from bbopt.backends.util import make_features
from bbopt.backends.util import serve_values


# Utilities:

# decorator to turn kwargs into the random function and its args
def create_space(name, func, *args):
    """Create a hyperopt space for the given param kwargs."""
    _coconut_match_to = func
    _coconut_case_check_0 = False
    if _coconut_match_to == "choice":
        _coconut_case_check_0 = True
    if _coconut_case_check_0:
        return hp.choice(name, *args)
    if not _coconut_case_check_0:
        if _coconut_match_to == "randrange":
            _coconut_case_check_0 = True
        if _coconut_case_check_0:
            start, stop, step = args
            if step != 1:
                raise ValueError("the hyperopt backend only supports a randrange step size of 1")
            return start + hp.randint(name, stop)  # despite being called randint, stop is exclusive
    if not _coconut_case_check_0:
        if _coconut_match_to == "uniform":
            _coconut_case_check_0 = True
        if _coconut_case_check_0:
            return hp.uniform(name, *args)
    if not _coconut_case_check_0:
        if _coconut_match_to == "normalvariate":
            _coconut_case_check_0 = True
        if _coconut_case_check_0:
            return hp.normal(name, *args)
    raise TypeError("insufficiently specified parameter {_coconut_format_0}".format(_coconut_format_0=(name)))


def examples_to_trials(examples, params):
    """Create hyperopt trials from the given examples."""
    trials = []
    NA = object()  # used to mark missing values

    for tid, ex in enumerate(examples):

        _coconut_match_to = ex
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get("gain", _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                gain = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            loss = negate_objective(gain)
        else:
            loss = ex["loss"]
        result = {"status": STATUS_OK, "loss": loss}

        vals = {}
        idxs = {}
        for k, v in zip(sorted(params), make_features(ex["values"], params, fallback_func=lambda name, func, *args, **kwargs: NA, converters={"choice": lambda val, choices: choices.index(val), "randrange": lambda val, start, stop, step: val - start}, convert_fallback=False)):
            vals[k] = [v] if v is not NA else []
            idxs[k] = [tid] if v is not NA else []

        misc = {"tid": tid, "idxs": idxs, "vals": vals, "cmd": None}

        trials.append({"tid": tid, "result": result, "misc": misc, "spec": spec_from_misc(misc), "state": JOB_STATE_DONE, "owner": None, "book_time": None, "refresh_time": None, "exp_key": None})

    return trials


# Backend:

class HyperoptBackend(_coconut.object):
    """The hyperopt backend uses hyperopt for black box optimization."""
    random_backend = RandomBackend()
    current_values = None

    def __init__(self, examples, params, algo=tpe.suggest, rstate=np.random.RandomState(), show_progressbar=False, **kwargs):
        if not examples:
            self.current_values = {}
            return

        space = (as_apply)(dict(((name), (create_space(name, func, *args))) for name, (func, args, kwargs) in sorted_items(params)))

        domain = Domain(self.set_current_values, space)

        trial_list = examples_to_trials(examples, params)

        trials = Trials()
        trials.insert_trial_docs(trial_list)

# run one iteration of hyperparameter optimization, with values saved
#  to the self.set_current_values callback passed to Domain
        (next)(FMinIter(algo, domain, trials, rstate, show_progressbar=show_progressbar, **kwargs))

        assert self.current_values is not None, self.current_values
        assert set(self.current_values.keys()) == set(params), self.current_values

    def set_current_values(self, values):
        """Callback to set the values for this run."""
        assert isinstance(values, dict), values
        self.current_values = values
        return {"status": STATUS_RUNNING}

    def param(self, name, func, *args, **kwargs):
        return serve_values(name, func, args, kwargs, serving_values=self.current_values, fallback_func=self.random_backend.param, backend_name="hyperopt", implemented_funcs=("choice", "randrange", "uniform", "normalvariate",), supported_kwargs=("guess", "placeholder_when_missing",))
