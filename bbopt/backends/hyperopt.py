#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfdeb9be1

# Compiled with Coconut version 2.0.0-a_dev53 [How Not to Be Seen]

"""
The hyperopt backend. Does black box optimization using hyperopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.dirname(_coconut_os.path.abspath(__file__)))
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



sys = _coconut_sys  #5 (line num in coconut source)

import numpy as np  #7 (line num in coconut source)

from hyperopt import hp  #9 (line num in coconut source)
from hyperopt import FMinIter  #9 (line num in coconut source)
from hyperopt import tpe  #9 (line num in coconut source)
from hyperopt import anneal  #9 (line num in coconut source)
from hyperopt.pyll import as_apply  #15 (line num in coconut source)
from hyperopt.base import Domain  #16 (line num in coconut source)
from hyperopt.base import Trials  #16 (line num in coconut source)
from hyperopt.base import STATUS_OK  #16 (line num in coconut source)
from hyperopt.base import STATUS_RUNNING  #16 (line num in coconut source)
from hyperopt.base import JOB_STATE_DONE  #16 (line num in coconut source)
from hyperopt.base import spec_from_misc  #16 (line num in coconut source)

from bbopt.util import sorted_items  #25 (line num in coconut source)
from bbopt.backends.util import StandardBackend  #26 (line num in coconut source)
from bbopt.backends.util import negate_objective  #26 (line num in coconut source)
from bbopt.backends.util import get_names_and_features  #26 (line num in coconut source)


# Utilities:

def create_space(name, func, *args):  #35 (line num in coconut source)
    """Create a hyperopt space for the given parameter."""  #36 (line num in coconut source)
    _coconut_case_match_to_0 = func, args  #37 (line num in coconut source)
    _coconut_case_match_check_0 = False  #37 (line num in coconut source)
    _coconut_match_set_name_choices = _coconut_sentinel  #37 (line num in coconut source)
    if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #37 (line num in coconut source)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_case_match_to_0)  #37 (line num in coconut source)
        if (_coconut.len(_coconut_match_temp_0) == 2) and (_coconut_match_temp_0[0] == "choice") and (_coconut.isinstance(_coconut_match_temp_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_0[1]) == 1):  #37 (line num in coconut source)
            _coconut_match_set_name_choices = _coconut_match_temp_0[1][0]  #37 (line num in coconut source)
            _coconut_case_match_check_0 = True  #37 (line num in coconut source)
    if _coconut_case_match_check_0:  #37 (line num in coconut source)
        if _coconut_match_set_name_choices is not _coconut_sentinel:  #37 (line num in coconut source)
            choices = _coconut_match_set_name_choices  #37 (line num in coconut source)
    if _coconut_case_match_check_0:  #37 (line num in coconut source)
        return hp.choice(name, choices)  #39 (line num in coconut source)
    if not _coconut_case_match_check_0:  #40 (line num in coconut source)
        _coconut_match_set_name_start = _coconut_sentinel  #40 (line num in coconut source)
        _coconut_match_set_name_stop = _coconut_sentinel  #40 (line num in coconut source)
        _coconut_match_set_name_step = _coconut_sentinel  #40 (line num in coconut source)
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #40 (line num in coconut source)
            _coconut_match_temp_1 = _coconut.tuple(_coconut_case_match_to_0)  #40 (line num in coconut source)
            if (_coconut.len(_coconut_match_temp_1) == 2) and (_coconut_match_temp_1[0] == "randrange") and (_coconut.isinstance(_coconut_match_temp_1[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_1[1]) == 3):  #40 (line num in coconut source)
                _coconut_match_set_name_start = _coconut_match_temp_1[1][0]  #40 (line num in coconut source)
                _coconut_match_set_name_stop = _coconut_match_temp_1[1][1]  #40 (line num in coconut source)
                _coconut_match_set_name_step = _coconut_match_temp_1[1][2]  #40 (line num in coconut source)
                _coconut_case_match_check_0 = True  #40 (line num in coconut source)
        if _coconut_case_match_check_0:  #40 (line num in coconut source)
            if _coconut_match_set_name_start is not _coconut_sentinel:  #40 (line num in coconut source)
                start = _coconut_match_set_name_start  #40 (line num in coconut source)
            if _coconut_match_set_name_stop is not _coconut_sentinel:  #40 (line num in coconut source)
                stop = _coconut_match_set_name_stop  #40 (line num in coconut source)
            if _coconut_match_set_name_step is not _coconut_sentinel:  #40 (line num in coconut source)
                step = _coconut_match_set_name_step  #40 (line num in coconut source)
        if _coconut_case_match_check_0:  #40 (line num in coconut source)
            if step != 1:  #41 (line num in coconut source)
                raise ValueError("the hyperopt backend only supports a randrange step size of 1 (use bb.choice(name, range(start, stop, step)) instead)")  #42 (line num in coconut source)
# despite being called randint, hp.randint is exclusive
            return start + hp.randint(name, stop - start)  #44 (line num in coconut source)
    if not _coconut_case_match_check_0:  #45 (line num in coconut source)
        _coconut_match_set_name_a = _coconut_sentinel  #45 (line num in coconut source)
        _coconut_match_set_name_b = _coconut_sentinel  #45 (line num in coconut source)
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #45 (line num in coconut source)
            _coconut_match_temp_2 = _coconut.tuple(_coconut_case_match_to_0)  #45 (line num in coconut source)
            if (_coconut.len(_coconut_match_temp_2) == 2) and (_coconut_match_temp_2[0] == "uniform") and (_coconut.isinstance(_coconut_match_temp_2[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_2[1]) == 2):  #45 (line num in coconut source)
                _coconut_match_set_name_a = _coconut_match_temp_2[1][0]  #45 (line num in coconut source)
                _coconut_match_set_name_b = _coconut_match_temp_2[1][1]  #45 (line num in coconut source)
                _coconut_case_match_check_0 = True  #45 (line num in coconut source)
        if _coconut_case_match_check_0:  #45 (line num in coconut source)
            if _coconut_match_set_name_a is not _coconut_sentinel:  #45 (line num in coconut source)
                a = _coconut_match_set_name_a  #45 (line num in coconut source)
            if _coconut_match_set_name_b is not _coconut_sentinel:  #45 (line num in coconut source)
                b = _coconut_match_set_name_b  #45 (line num in coconut source)
        if _coconut_case_match_check_0:  #45 (line num in coconut source)
            return hp.uniform(name, a, b)  #46 (line num in coconut source)
    if not _coconut_case_match_check_0:  #47 (line num in coconut source)
        _coconut_match_set_name_mu = _coconut_sentinel  #47 (line num in coconut source)
        _coconut_match_set_name_sigma = _coconut_sentinel  #47 (line num in coconut source)
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #47 (line num in coconut source)
            _coconut_match_temp_3 = _coconut.tuple(_coconut_case_match_to_0)  #47 (line num in coconut source)
            if (_coconut.len(_coconut_match_temp_3) == 2) and (_coconut_match_temp_3[0] == "normalvariate") and (_coconut.isinstance(_coconut_match_temp_3[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_3[1]) == 2):  #47 (line num in coconut source)
                _coconut_match_set_name_mu = _coconut_match_temp_3[1][0]  #47 (line num in coconut source)
                _coconut_match_set_name_sigma = _coconut_match_temp_3[1][1]  #47 (line num in coconut source)
                _coconut_case_match_check_0 = True  #47 (line num in coconut source)
        if _coconut_case_match_check_0:  #47 (line num in coconut source)
            if _coconut_match_set_name_mu is not _coconut_sentinel:  #47 (line num in coconut source)
                mu = _coconut_match_set_name_mu  #47 (line num in coconut source)
            if _coconut_match_set_name_sigma is not _coconut_sentinel:  #47 (line num in coconut source)
                sigma = _coconut_match_set_name_sigma  #47 (line num in coconut source)
        if _coconut_case_match_check_0:  #47 (line num in coconut source)
            return hp.normal(name, mu, sigma)  #48 (line num in coconut source)
    raise TypeError("invalid parameter {_coconut_format_0}".format(_coconut_format_0=(name)))  #49 (line num in coconut source)



def examples_to_trials(examples, params):  #52 (line num in coconut source)
    """Create hyperopt trials from the given examples."""  #53 (line num in coconut source)
    trials = []  #54 (line num in coconut source)
    NA = object()  # used to mark missing values  #55 (line num in coconut source)

    for tid, ex in enumerate(examples):  #57 (line num in coconut source)

        _coconut_match_to_0 = ex  #59 (line num in coconut source)
        _coconut_match_check_0 = False  #59 (line num in coconut source)
        _coconut_match_set_name_gain = _coconut_sentinel  #59 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #59 (line num in coconut source)
            _coconut_match_temp_4 = _coconut_match_to_0.get("gain", _coconut_sentinel)  #59 (line num in coconut source)
            if _coconut_match_temp_4 is not _coconut_sentinel:  #59 (line num in coconut source)
                _coconut_match_set_name_gain = _coconut_match_temp_4  #59 (line num in coconut source)
                _coconut_match_check_0 = True  #59 (line num in coconut source)
        if _coconut_match_check_0:  #59 (line num in coconut source)
            if _coconut_match_set_name_gain is not _coconut_sentinel:  #59 (line num in coconut source)
                gain = _coconut_match_set_name_gain  #59 (line num in coconut source)
        if _coconut_match_check_0:  #59 (line num in coconut source)
            loss = negate_objective(gain)  #60 (line num in coconut source)
        else:  #61 (line num in coconut source)
            loss = ex["loss"]  #62 (line num in coconut source)
        result = {"status": STATUS_OK, "loss": loss}  #63 (line num in coconut source)

        vals = {}  #68 (line num in coconut source)
        idxs = {}  #69 (line num in coconut source)
        for k, v in get_names_and_features(ex["values"], params, fallback_func=lambda name, func, *args, **kwargs: NA, converters={"choice": lambda val, choices: choices.index(val), "randrange": lambda val, start, stop, step: val - start}, convert_fallback=False):  #70 (line num in coconut source)
            vals[k] = [v,] if v is not NA else []  #80 (line num in coconut source)
            idxs[k] = [tid,] if v is not NA else []  #81 (line num in coconut source)

        misc = {"tid": tid, "idxs": idxs, "vals": vals, "cmd": None}  #83 (line num in coconut source)

        trials.append({"tid": tid, "result": result, "misc": misc, "spec": spec_from_misc(misc), "state": JOB_STATE_DONE, "owner": None, "book_time": None, "refresh_time": None, "exp_key": None})  #90 (line num in coconut source)

    return trials  #102 (line num in coconut source)


# Backend:


class HyperoptBackend(StandardBackend):  #107 (line num in coconut source)
    """The hyperopt backend uses hyperopt for black box optimization."""  #108 (line num in coconut source)
    backend_name = "hyperopt"  #109 (line num in coconut source)
    implemented_funcs = ("choice", "randrange", "uniform", "normalvariate")  #110 (line num in coconut source)

    @override  #118 (line num in coconut source)
    def setup_backend(self, params, algo=tpe.suggest, rstate=None, show_progressbar=False, **options):  #119 (line num in coconut source)
        """Special method to initialize the backend from params."""  #120 (line num in coconut source)
        if rstate is None:  #121 (line num in coconut source)
            try:  #122 (line num in coconut source)
                rstate = np.random.default_rng()  #123 (line num in coconut source)
            except AttributeError:  #124 (line num in coconut source)
                rstate = np.random.RandomState()  #125 (line num in coconut source)
        self.params = params  #126 (line num in coconut source)

        space = (as_apply)(dict(((name), (create_space(name, func, *args))) for name, (func, args, kwargs) in sorted_items(params)))  #128 (line num in coconut source)

        domain = Domain(self.set_current_values, space)  #133 (line num in coconut source)

        self.trials = Trials()  #135 (line num in coconut source)

        self.fmin_iter = FMinIter(algo, domain, self.trials, rstate, show_progressbar=show_progressbar, **options)  #137 (line num in coconut source)


    @override  #146 (line num in coconut source)
    def tell_examples(self, new_examples):  #147 (line num in coconut source)
        """Special method that allows fast updating of the backend with new examples."""  #148 (line num in coconut source)
        trial_list = examples_to_trials(new_examples, self.params)  #149 (line num in coconut source)
        self.trials.insert_trial_docs(trial_list)  #150 (line num in coconut source)
        self.trials.refresh()  #151 (line num in coconut source)

# run one iteration of hyperparameter optimization, with values saved
#  to the self.set_current_values callback passed to Domain
        next(self.fmin_iter)  #155 (line num in coconut source)

        assert self.current_values is not None, self.current_values  #157 (line num in coconut source)
        assert set(self.current_values.keys()) == set(self.params), self.current_values  #158 (line num in coconut source)


    def set_current_values(self, values):  #160 (line num in coconut source)
        """Callback to set the values for this run."""  #161 (line num in coconut source)
        assert isinstance(values, dict), values  #162 (line num in coconut source)
        self.current_values = values  #163 (line num in coconut source)
        return {"status": STATUS_RUNNING}  #164 (line num in coconut source)


# Registered names:


_coconut_call_set_names(HyperoptBackend)  #171 (line num in coconut source)
HyperoptBackend.register()  #171 (line num in coconut source)

HyperoptBackend.register_alg("tree_structured_parzen_estimator", algo=tpe.suggest)  #173 (line num in coconut source)
HyperoptBackend.register_alg("annealing", algo=anneal.suggest)  #174 (line num in coconut source)
if sys.version_info >= (3,):  #175 (line num in coconut source)
    from hyperopt import atpe  #176 (line num in coconut source)
    HyperoptBackend.register_alg("adaptive_tpe", algo=atpe.suggest)  #177 (line num in coconut source)

HyperoptBackend.register_meta_for_all_algs("any_hyperopt")  #179 (line num in coconut source)
