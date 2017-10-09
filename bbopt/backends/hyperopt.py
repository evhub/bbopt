#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x4c165a6b

# Compiled with Coconut version 1.3.0-post_dev4 [Dead Parrot]

"""
The hyperopt backend. Does black box optimization using hyperopt.
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



# Imports:

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

from bbopt.backends.random import RandomBackend
from bbopt.params import param_processor
from bbopt.util import sorted_items
from bbopt.util import negate_objective
from bbopt.util import format_err
from bbopt.util import make_features

# Utilities:

def create_space(name, choice=None, randrange=None, uniform=None, normalvariate=None,):
    """Create a hyperopt space for the given param kwargs."""
    if choice is not None:
        return hp.choice(name, *choice)
    if randrange is not None:
        start, stop, step = randrange
        if step != 1:
            raise ValueError("the hyperopt backend only supports a randrange step size of 1")
        return start + hp.randint(name, stop)  # despite being called randint, stop is exclusive
    if uniform is not None:
        return hp.uniform(name, *uniform)
    if normalvariate is not None:
        return hp.normal(name, *normalvariate)
    raise TypeError("insufficiently specified parameter %r" % name)

def examples_to_trials(examples, params):
    """Create hyperopt trials from the given examples."""
    trials = []
    NA = object()
    for tid, ex in enumerate(examples):
        _coconut_match_check = False
        _coconut_match_to = ex
        _coconut_sentinel = _coconut.object()
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
        for k, v in zip(sorted(params), make_features(ex["values"], params, default_placeholder=NA)):
            vals[k] = [v] if v is not NA else []
            idxs[k] = [tid] if v is not NA else []
        misc = {"tid": tid, "idxs": idxs, "vals": vals, "cmd": None}
        trials.append({"tid": tid, "result": result, "misc": misc, "spec": spec_from_misc(misc), "state": JOB_STATE_DONE, "owner": None, "book_time": None, "refresh_time": None, "exp_key": None})
    return trials

# Backend:

class HyperoptBackend(_coconut.object):
    """The hyperopt backend uses hyperopt for black box optimization."""
    current_values = None

    def __init__(self, examples, params, algo=tpe.suggest, rstate=np.random.RandomState(), **kwargs):
        if not examples:
            self.current_values = {}
            return
        space = (as_apply)(dict(((name), (create_space(name, **param_processor.filter_kwargs(param_kwargs)))) for name, param_kwargs in sorted_items(params)))
        domain = Domain(self.set_current_values, space)
        trials = Trials()
        trials.insert_trial_docs(examples_to_trials(examples, params))
        (next)(FMinIter(algo, domain, trials, rstate, **kwargs))
        assert self.current_values is not None
        assert set(self.current_values.keys()) == set(params)

    def set_current_values(self, values):
        assert isinstance(values, dict)
        self.current_values = values
        return {"status": STATUS_RUNNING}

    def param(self, name, **kwargs):
        _coconut_match_check = False
        _coconut_match_to = self.current_values
        _coconut_sentinel = _coconut.object()
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                value = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            return value
        else:
            if "guess" in kwargs:
                return kwargs["guess"]
            else:
                return RandomBackend().param(**kwargs)
