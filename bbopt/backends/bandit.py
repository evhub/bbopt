#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x5d9e0eec

# Compiled with Coconut version 1.5.0-post_dev75 [Fish License]

"""
The bandit backend. Implementations of simple multi-armed bandit algorithms, primarily for run_meta.
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
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import random
import math

import numpy as np

from bbopt import constants
from bbopt.util import mean
from bbopt.backends.util import Backend
from bbopt.backends.util import get_named_data_points_and_losses
from bbopt.backends.util import marginalize


# Backend:

class BanditBackend(Backend):
    """The bandit backend implements simple multi-armed bandit algorithms."""
    backend_name = "bandit"

    def __init__(self, *args, **options):
        self.init_fallback_backend()
        super(BanditBackend, self).__init__(*args, **options)

    @override
    def attempt_update(self, examples, params, bandit_alg, eps=None, temp=None):
        """Update the bandit algorithm with new parameters."""
        self.bandit_alg = bandit_alg

        if len(examples) <= 1:
            self.named_data_points = self.losses = None
            return True

        self.named_data_points, self.losses = get_named_data_points_and_losses(examples, params)

        if bandit_alg == "greedy":
            if eps is None:
                eps = constants.eps_greedy_explore_prob
            assert temp is None, "temp parameter not supported for bandit_alg={_coconut_format_0}".format(_coconut_format_0=(bandit_alg))

        elif bandit_alg.startswith("boltzmann"):
            if eps is None:
# make sure we cover the full space before doing our bandit algorithm
                eps = 1 / math.sqrt(len(self.losses) - 1)
            if temp is None:
                temp = (np.std)((np.asarray)(self.losses), ddof=1)

        else:
            raise ValueError("invalid multi-armed bandit algorithm: {_coconut_format_0}".format(_coconut_format_0=(bandit_alg)))

        self.eps = eps
        self.temp = temp

        return True

    @override
    def param(self, name, *args, **kwargs):
        """Get a value for the given parameter."""
        if self.losses is None or random.random() < self.eps:
            rand_val = self.fallback_backend.param(name, *args, **kwargs)

# attempt to reroll once if we've already seen the value
            if self.named_data_points is not None:
                if any((point[name] == rand_val for point in self.named_data_points)):
                    rand_val = self.fallback_backend.param(name, *args, **kwargs)

            return rand_val

        elif self.bandit_alg == "greedy":
            marginals = marginalize(self.named_data_points, self.losses, name)
            @_coconut_mark_as_match
            def _coconut_lambda_0(*_coconut_match_args, **_coconut_match_kwargs):
                _coconut_match_check_0 = False
                _coconut_FunctionMatchError = _coconut_get_function_match_error()
                if (_coconut.len(_coconut_match_args) == 1) and (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 2):
                    val = _coconut_match_args[0][0]
                    loss = _coconut_match_args[0][1]
                    if not _coconut_match_kwargs:
                        _coconut_match_check_0 = True
                if not _coconut_match_check_0:
                    raise _coconut_FunctionMatchError('best_val, min_loss = min(marginals, key=def ((val, loss)) -> loss)', _coconut_match_args)
                return loss
            best_val, min_loss = min(marginals, key=_coconut_lambda_0)
            return best_val

        else:
            marginals = marginalize(self.named_data_points, self.losses, name, ave_func=lambda losses: (mean(losses), len(losses)))
            @_coconut_mark_as_match
            def _coconut_lambda_1(*_coconut_match_args, **_coconut_match_kwargs):
                _coconut_match_check_1 = False
                _coconut_FunctionMatchError = _coconut_get_function_match_error()
                if (_coconut.len(_coconut_match_args) == 2) and ("val" not in _coconut_match_kwargs) and (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 2):
                    _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("val")
                    loss = _coconut_match_args[1][0]
                    N = _coconut_match_args[1][1]
                    if not _coconut_match_kwargs:
                        val = _coconut_match_temp_0
                        _coconut_match_check_1 = True
                if not _coconut_match_check_1:
                    raise _coconut_FunctionMatchError('xs = marginals |> starmap$(def (val, (loss, N)) -> -loss) |> np.asarray', _coconut_match_args)
                return -loss
            xs = (np.asarray)((starmap)(_coconut_lambda_1, marginals))
            zs = self.temp * np.random.gumbel(size=xs.shape)

            if self.bandit_alg == "boltzmann_gumbel":
                @_coconut_mark_as_match
                def _coconut_lambda_2(*_coconut_match_args, **_coconut_match_kwargs):
                    _coconut_match_check_2 = False
                    _coconut_FunctionMatchError = _coconut_get_function_match_error()
                    if (_coconut.len(_coconut_match_args) == 2) and ("val" not in _coconut_match_kwargs) and (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 2):
                        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("val")
                        loss = _coconut_match_args[1][0]
                        N = _coconut_match_args[1][1]
                        if not _coconut_match_kwargs:
                            val = _coconut_match_temp_0
                            _coconut_match_check_2 = True
                    if not _coconut_match_check_2:
                        raise _coconut_FunctionMatchError('ns = marginals |> starmap$(def (val, (loss, N)) -> N) |> np.asarray', _coconut_match_args)
                    return N
                ns = (np.asarray)((starmap)(_coconut_lambda_2, marginals))
                zs /= np.sqrt(ns)
            else:
                assert self.bandit_alg == "boltzmann", "invalid boltzmann bandit algorithm: {_coconut_format_0}".format(_coconut_format_0=(self.bandit_alg))

            best_i = np.argmax(xs + zs)
            return marginals[best_i][0]


# Registered names:

_coconut_call_set_names(BanditBackend)
BanditBackend.register()

BanditBackend.register_alg("epsilon_greedy", bandit_alg="greedy")
BanditBackend.register_alg("boltzmann_exploration", bandit_alg="boltzmann")
BanditBackend.register_alg("boltzmann_gumbel_exploration", bandit_alg="boltzmann_gumbel")
