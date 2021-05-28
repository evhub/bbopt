#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xd7668260

# Compiled with Coconut version 1.5.0-post_dev57 [Fish License]

"""
The hyperopt backend. Does black box optimization using hyperopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os.path.dirname(_coconut_cached_module.__file__) != _coconut_file_dir:
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
                _coconut_vtype = type(_coconut_v)
                _coconut_vtype.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)
# Compiled Coconut: -----------------------------------------------------------



sys = _coconut_sys

import numpy as np

from hyperopt import hp
from hyperopt import FMinIter
from hyperopt import tpe
from hyperopt import anneal
from hyperopt.pyll import as_apply
from hyperopt.base import Domain
from hyperopt.base import Trials
from hyperopt.base import STATUS_OK
from hyperopt.base import STATUS_RUNNING
from hyperopt.base import JOB_STATE_DONE
from hyperopt.base import spec_from_misc

from bbopt.util import sorted_items
from bbopt.backends.util import StandardBackend
from bbopt.backends.util import negate_objective
from bbopt.backends.util import get_names_and_features


# Utilities:

def create_space(name, func, *args):
    """Create a hyperopt space for the given parameter."""
    _coconut_case_match_to_0 = func, args
    _coconut_case_match_check_0 = False
    if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == "choice") and (_coconut.isinstance(_coconut_case_match_to_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0[1]) == 1):
        choices = _coconut_case_match_to_0[1][0]
        _coconut_case_match_check_0 = True
    if _coconut_case_match_check_0:
        return hp.choice(name, choices)
    if not _coconut_case_match_check_0:
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == "randrange") and (_coconut.isinstance(_coconut_case_match_to_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0[1]) == 3):
            start = _coconut_case_match_to_0[1][0]
            stop = _coconut_case_match_to_0[1][1]
            step = _coconut_case_match_to_0[1][2]
            _coconut_case_match_check_0 = True
        if _coconut_case_match_check_0:
            if step != 1:
                raise ValueError("the hyperopt backend only supports a randrange step size of 1 (use bb.choice(name, range(start, stop, step)) instead)")
# despite being called randint, hp.randint is exclusive
            return start + hp.randint(name, stop - start)
    if not _coconut_case_match_check_0:
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == "uniform") and (_coconut.isinstance(_coconut_case_match_to_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0[1]) == 2):
            a = _coconut_case_match_to_0[1][0]
            b = _coconut_case_match_to_0[1][1]
            _coconut_case_match_check_0 = True
        if _coconut_case_match_check_0:
            return hp.uniform(name, a, b)
    if not _coconut_case_match_check_0:
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == "normalvariate") and (_coconut.isinstance(_coconut_case_match_to_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0[1]) == 2):
            mu = _coconut_case_match_to_0[1][0]
            sigma = _coconut_case_match_to_0[1][1]
            _coconut_case_match_check_0 = True
        if _coconut_case_match_check_0:
            return hp.normal(name, mu, sigma)
    raise TypeError("invalid parameter {_coconut_format_0}".format(_coconut_format_0=(name)))


def examples_to_trials(examples, params):
    """Create hyperopt trials from the given examples."""
    trials = []
    NA = object()  # used to mark missing values

    for tid, ex in enumerate(examples):

        _coconut_match_to_0 = ex
        _coconut_match_check_0 = False
        if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to_0.get("gain", _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                gain = _coconut_match_temp_0
                _coconut_match_check_0 = True
        if _coconut_match_check_0:
            loss = negate_objective(gain)
        else:
            loss = ex["loss"]
        result = {"status": STATUS_OK, "loss": loss}

        vals = {}
        idxs = {}
        for k, v in get_names_and_features(ex["values"], params, fallback_func=lambda name, func, *args, **kwargs: NA, converters={"choice": lambda val, choices: choices.index(val), "randrange": lambda val, start, stop, step: val - start}, convert_fallback=False):
            vals[k] = [v] if v is not NA else []
            idxs[k] = [tid] if v is not NA else []

        misc = {"tid": tid, "idxs": idxs, "vals": vals, "cmd": None}

        trials.append({"tid": tid, "result": result, "misc": misc, "spec": spec_from_misc(misc), "state": JOB_STATE_DONE, "owner": None, "book_time": None, "refresh_time": None, "exp_key": None})

    return trials


# Backend:

class HyperoptBackend(StandardBackend):
    """The hyperopt backend uses hyperopt for black box optimization."""
    backend_name = "hyperopt"
    implemented_funcs = ("choice", "randrange", "uniform", "normalvariate",)

    @override
    def setup_backend(self, params, algo=tpe.suggest, rstate=np.random.RandomState(), show_progressbar=False, **options):
        """Special method to initialize the backend from params."""
        self.params = params

        space = (as_apply)(dict(((name), (create_space(name, func, *args))) for name, (func, args, kwargs) in sorted_items(params)))

        domain = Domain(self.set_current_values, space)

        self.trials = Trials()

        self.fmin_iter = FMinIter(algo, domain, self.trials, rstate, show_progressbar=show_progressbar, **options)

    @override
    def tell_examples(self, new_examples):
        """Special method that allows fast updating of the backend with new examples."""
        trial_list = examples_to_trials(new_examples, self.params)
        self.trials.insert_trial_docs(trial_list)
        self.trials.refresh()

# run one iteration of hyperparameter optimization, with values saved
#  to the self.set_current_values callback passed to Domain
        next(self.fmin_iter)

        assert self.current_values is not None, self.current_values
        assert set(self.current_values.keys()) == set(self.params), self.current_values

    def set_current_values(self, values):
        """Callback to set the values for this run."""
        assert isinstance(values, dict), values
        self.current_values = values
        return {"status": STATUS_RUNNING}


# Registered names:

_coconut_call_set_names(HyperoptBackend)
HyperoptBackend.register()

HyperoptBackend.register_alg("tree_structured_parzen_estimator", algo=tpe.suggest)
HyperoptBackend.register_alg("annealing", algo=anneal.suggest)

if sys.version_info >= (3,):
    from hyperopt import atpe
    HyperoptBackend.register_alg("adaptive_tpe", algo=atpe.suggest)

HyperoptBackend.register_meta("tpe_or_gp", ("tree_structured_parzen_estimator", "_safe_gaussian_process",))
