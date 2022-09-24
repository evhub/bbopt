#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa262fc0e

# Compiled with Coconut version 2.0.0-a_dev63 [How Not to Be Seen]

"""
The bandit backend. Implementations of simple multi-armed bandit algorithms, primarily for run_meta.
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
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import random  #5 (line num in coconut source)
import math  #6 (line num in coconut source)

import numpy as np  #8 (line num in coconut source)

from bbopt import constants  #10 (line num in coconut source)
from bbopt.util import mean  #11 (line num in coconut source)
from bbopt.backends.util import Backend  #12 (line num in coconut source)
from bbopt.backends.util import get_named_data_points_and_losses  #12 (line num in coconut source)
from bbopt.backends.util import marginalize  #12 (line num in coconut source)


# Backend:

class BanditBackend(Backend):  #21 (line num in coconut source)
    """The bandit backend implements simple multi-armed bandit algorithms."""  #22 (line num in coconut source)
    backend_name = "bandit"  #23 (line num in coconut source)

    def __init__(self, *args, **options):  #25 (line num in coconut source)
        self.init_fallback_backend()  #26 (line num in coconut source)
        __class__ = BanditBackend  #27 (line num in coconut source)

        super().__init__(*args, **options)  #27 (line num in coconut source)


    @override  #29 (line num in coconut source)
    def attempt_update(self, examples, params, bandit_alg, eps=None, temp=None):  #30 (line num in coconut source)
        """Update the bandit algorithm with new parameters."""  #31 (line num in coconut source)
        self.bandit_alg = bandit_alg  #32 (line num in coconut source)

        if len(examples) <= 1:  #34 (line num in coconut source)
            self.named_data_points = self.losses = None  #35 (line num in coconut source)
            return True  #36 (line num in coconut source)

        self.named_data_points, self.losses = get_named_data_points_and_losses(examples, params)  #38 (line num in coconut source)

        if bandit_alg == "greedy":  #40 (line num in coconut source)
            if eps is None:  #41 (line num in coconut source)
                eps = constants.eps_greedy_explore_prob  #42 (line num in coconut source)
            assert temp is None, "temp parameter not supported for bandit_alg={_coconut_format_0}".format(_coconut_format_0=(bandit_alg))  #43 (line num in coconut source)

        elif bandit_alg.startswith("boltzmann"):  #45 (line num in coconut source)
            if eps is None:  #46 (line num in coconut source)
# make sure we cover the full space before doing our bandit algorithm
                eps = 1 / math.sqrt(len(self.losses) - 1)  #48 (line num in coconut source)
            if temp is None:  #49 (line num in coconut source)
                temp = (np.std)((np.asarray)(self.losses), ddof=1)  #50 (line num in coconut source)

        else:  #52 (line num in coconut source)
            raise ValueError("invalid multi-armed bandit algorithm: {_coconut_format_0}".format(_coconut_format_0=(bandit_alg)))  #53 (line num in coconut source)

        self.eps = eps  #55 (line num in coconut source)
        self.temp = temp  #56 (line num in coconut source)

        return True  #58 (line num in coconut source)


    @override  #60 (line num in coconut source)
    def param(self, name, *args, **kwargs):  #61 (line num in coconut source)
        """Get a value for the given parameter."""  #62 (line num in coconut source)
        if self.losses is None or random.random() < self.eps:  #63 (line num in coconut source)
            rand_val = self.fallback_backend.param(name, *args, **kwargs)  #64 (line num in coconut source)

# attempt to reroll once if we've already seen the value
            if self.named_data_points is not None:  #67 (line num in coconut source)
                if any((point[name] == rand_val for point in self.named_data_points)):  #68 (line num in coconut source)
                    rand_val = self.fallback_backend.param(name, *args, **kwargs)  #69 (line num in coconut source)

            return rand_val  #71 (line num in coconut source)

        elif self.bandit_alg == "greedy":  #73 (line num in coconut source)
            marginals = marginalize(self.named_data_points, self.losses, name)  #74 (line num in coconut source)
            @_coconut_mark_as_match  #75 (line num in coconut source)
            def _coconut_lambda_0(*_coconut_match_args, **_coconut_match_kwargs):  #75 (line num in coconut source)
                _coconut_match_check_0 = False  #75 (line num in coconut source)
                _coconut_match_set_name_val = _coconut_sentinel  #75 (line num in coconut source)
                _coconut_match_set_name_loss = _coconut_sentinel  #75 (line num in coconut source)
                _coconut_FunctionMatchError = _coconut_get_function_match_error()  #75 (line num in coconut source)
                if _coconut.len(_coconut_match_args) == 1:  #75 (line num in coconut source)
                    if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 2):  #75 (line num in coconut source)
                        _coconut_match_set_name_val = _coconut_match_args[0][0]  #75 (line num in coconut source)
                        _coconut_match_set_name_loss = _coconut_match_args[0][1]  #75 (line num in coconut source)
                        if not _coconut_match_kwargs:  #75 (line num in coconut source)
                            _coconut_match_check_0 = True  #75 (line num in coconut source)
                if _coconut_match_check_0:  #75 (line num in coconut source)
                    if _coconut_match_set_name_val is not _coconut_sentinel:  #75 (line num in coconut source)
                        val = _coconut_match_set_name_val  #75 (line num in coconut source)
                    if _coconut_match_set_name_loss is not _coconut_sentinel:  #75 (line num in coconut source)
                        loss = _coconut_match_set_name_loss  #75 (line num in coconut source)
                if not _coconut_match_check_0:  #75 (line num in coconut source)
                    raise _coconut_FunctionMatchError('best_val, min_loss = min(marginals, key=def ((val, loss)) -> loss)', _coconut_match_args)  #75 (line num in coconut source)
                return loss  #75 (line num in coconut source)
            best_val, min_loss = min(marginals, key=_coconut_lambda_0)  #75 (line num in coconut source)
            return best_val  #76 (line num in coconut source)

        else:  #78 (line num in coconut source)
            marginals = marginalize(self.named_data_points, self.losses, name, ave_func=lambda losses: (mean(losses), len(losses)))  #79 (line num in coconut source)
            @_coconut_mark_as_match  #80 (line num in coconut source)
            def _coconut_lambda_1(*_coconut_match_args, **_coconut_match_kwargs):  #80 (line num in coconut source)
                _coconut_match_check_1 = False  #80 (line num in coconut source)
                _coconut_match_set_name_val = _coconut_sentinel  #80 (line num in coconut source)
                _coconut_match_set_name_loss = _coconut_sentinel  #80 (line num in coconut source)
                _coconut_match_set_name_N = _coconut_sentinel  #80 (line num in coconut source)
                _coconut_FunctionMatchError = _coconut_get_function_match_error()  #80 (line num in coconut source)
                if (_coconut.len(_coconut_match_args) == 2) and ("val" not in _coconut_match_kwargs):  #80 (line num in coconut source)
                    if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 2):  #80 (line num in coconut source)
                        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("val")  #80 (line num in coconut source)
                        _coconut_match_set_name_loss = _coconut_match_args[1][0]  #80 (line num in coconut source)
                        _coconut_match_set_name_N = _coconut_match_args[1][1]  #80 (line num in coconut source)
                        _coconut_match_set_name_val = _coconut_match_temp_0  #80 (line num in coconut source)
                        if not _coconut_match_kwargs:  #80 (line num in coconut source)
                            _coconut_match_check_1 = True  #80 (line num in coconut source)
                if _coconut_match_check_1:  #80 (line num in coconut source)
                    if _coconut_match_set_name_val is not _coconut_sentinel:  #80 (line num in coconut source)
                        val = _coconut_match_set_name_val  #80 (line num in coconut source)
                    if _coconut_match_set_name_loss is not _coconut_sentinel:  #80 (line num in coconut source)
                        loss = _coconut_match_set_name_loss  #80 (line num in coconut source)
                    if _coconut_match_set_name_N is not _coconut_sentinel:  #80 (line num in coconut source)
                        N = _coconut_match_set_name_N  #80 (line num in coconut source)
                if not _coconut_match_check_1:  #80 (line num in coconut source)
                    raise _coconut_FunctionMatchError('xs = marginals |> starmap$(def (val, (loss, N)) -> -loss) |> np.asarray', _coconut_match_args)  #80 (line num in coconut source)
                return -loss  #80 (line num in coconut source)
            xs = (np.asarray)((starmap)(_coconut_lambda_1, marginals))  #80 (line num in coconut source)
            zs = self.temp * np.random.gumbel(size=xs.shape)  #81 (line num in coconut source)

            if self.bandit_alg == "boltzmann_gumbel":  #83 (line num in coconut source)
                @_coconut_mark_as_match  #84 (line num in coconut source)
                def _coconut_lambda_2(*_coconut_match_args, **_coconut_match_kwargs):  #84 (line num in coconut source)
                    _coconut_match_check_2 = False  #84 (line num in coconut source)
                    _coconut_match_set_name_val = _coconut_sentinel  #84 (line num in coconut source)
                    _coconut_match_set_name_loss = _coconut_sentinel  #84 (line num in coconut source)
                    _coconut_match_set_name_N = _coconut_sentinel  #84 (line num in coconut source)
                    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #84 (line num in coconut source)
                    if (_coconut.len(_coconut_match_args) == 2) and ("val" not in _coconut_match_kwargs):  #84 (line num in coconut source)
                        if (_coconut.isinstance(_coconut_match_args[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[1]) == 2):  #84 (line num in coconut source)
                            _coconut_match_temp_1 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("val")  #84 (line num in coconut source)
                            _coconut_match_set_name_loss = _coconut_match_args[1][0]  #84 (line num in coconut source)
                            _coconut_match_set_name_N = _coconut_match_args[1][1]  #84 (line num in coconut source)
                            _coconut_match_set_name_val = _coconut_match_temp_1  #84 (line num in coconut source)
                            if not _coconut_match_kwargs:  #84 (line num in coconut source)
                                _coconut_match_check_2 = True  #84 (line num in coconut source)
                    if _coconut_match_check_2:  #84 (line num in coconut source)
                        if _coconut_match_set_name_val is not _coconut_sentinel:  #84 (line num in coconut source)
                            val = _coconut_match_set_name_val  #84 (line num in coconut source)
                        if _coconut_match_set_name_loss is not _coconut_sentinel:  #84 (line num in coconut source)
                            loss = _coconut_match_set_name_loss  #84 (line num in coconut source)
                        if _coconut_match_set_name_N is not _coconut_sentinel:  #84 (line num in coconut source)
                            N = _coconut_match_set_name_N  #84 (line num in coconut source)
                    if not _coconut_match_check_2:  #84 (line num in coconut source)
                        raise _coconut_FunctionMatchError('ns = marginals |> starmap$(def (val, (loss, N)) -> N) |> np.asarray', _coconut_match_args)  #84 (line num in coconut source)
                    return N  #84 (line num in coconut source)
                ns = (np.asarray)((starmap)(_coconut_lambda_2, marginals))  #84 (line num in coconut source)
                zs /= np.sqrt(ns)  #85 (line num in coconut source)
            else:  #86 (line num in coconut source)
                assert self.bandit_alg == "boltzmann", "invalid bandit algorithm: {_coconut_format_0}".format(_coconut_format_0=(self.bandit_alg))  #87 (line num in coconut source)

            best_i = np.argmax(xs + zs)  #89 (line num in coconut source)
            return marginals[best_i][0]  #90 (line num in coconut source)


# Registered names:


_coconut_call_set_names(BanditBackend)  #95 (line num in coconut source)
BanditBackend.register()  #95 (line num in coconut source)

BanditBackend.register_alg("epsilon_greedy", bandit_alg="greedy")  #97 (line num in coconut source)
BanditBackend.register_alg("boltzmann_exploration", bandit_alg="boltzmann")  #98 (line num in coconut source)
BanditBackend.register_alg("boltzmann_gumbel_exploration", bandit_alg="boltzmann_gumbel")  #99 (line num in coconut source)
