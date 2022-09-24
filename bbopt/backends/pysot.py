#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x2625c327

# Compiled with Coconut version 2.0.0-a_dev65 [How Not to Be Seen]

"""
The pySOT backend. Does black box optimization using pySOT.
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



sys = _coconut_sys  #5 (line num in coconut source)

import numpy as np  #7 (line num in coconut source)

# patch in abc.ABC if it doesn't already exist
import abc  #10 (line num in coconut source)
if not hasattr(abc, "ABC"):  #11 (line num in coconut source)
    class ABC(_coconut.object):  #12 (line num in coconut source)
        __metaclass__ = abc.ABCMeta  #13 (line num in coconut source)
    _coconut_call_set_names(ABC)  #14 (line num in coconut source)
    abc.ABC = ABC  #14 (line num in coconut source)

from pySOT.optimization_problems.optimization_problem import OptimizationProblem  #16 (line num in coconut source)
from pySOT.experimental_design import ExperimentalDesign  #17 (line num in coconut source)
from pySOT.experimental_design import LatinHypercube  #17 (line num in coconut source)
from pySOT.experimental_design import SymmetricLatinHypercube  #17 (line num in coconut source)
from pySOT.experimental_design import TwoFactorial  #17 (line num in coconut source)
from pySOT.surrogate import RBFInterpolant  #23 (line num in coconut source)
from pySOT.surrogate import GPRegressor  #23 (line num in coconut source)
from pySOT.surrogate.kernels import CubicKernel  #27 (line num in coconut source)
from pySOT.surrogate.kernels import LinearKernel  #27 (line num in coconut source)
from pySOT.surrogate.tails import ConstantTail  #31 (line num in coconut source)
from pySOT.surrogate.tails import LinearTail  #31 (line num in coconut source)
from pySOT.strategy import SRBFStrategy  #35 (line num in coconut source)
from pySOT.strategy import EIStrategy  #35 (line num in coconut source)
from pySOT.strategy import DYCORSStrategy  #35 (line num in coconut source)
from pySOT.strategy import LCBStrategy  #35 (line num in coconut source)

from bbopt.util import sorted_items  #42 (line num in coconut source)
from bbopt.backends.util import StandardBackend  #43 (line num in coconut source)


# Utilities:

class EmptyExperimentalDesign(ExperimentalDesign):  #48 (line num in coconut source)
    num_pts = 0  #49 (line num in coconut source)

    def __init__(self, dim):  #51 (line num in coconut source)
        self.dim = dim  #52 (line num in coconut source)


    def generate_points(self, lb=None, ub=None, int_var=None):  #54 (line num in coconut source)
        return np.empty((0, self.dim))  #55 (line num in coconut source)



_coconut_call_set_names(EmptyExperimentalDesign)  #58 (line num in coconut source)
class BBoptOptimizationProblem(OptimizationProblem):  #58 (line num in coconut source)
    def __init__(self, params):  #59 (line num in coconut source)
        self.params = params  #60 (line num in coconut source)
        self.dim = len(params)  #61 (line num in coconut source)
        self.got_values = None  #62 (line num in coconut source)

# lower and upper bounds; len must match self.dim
        self.lb = []  #65 (line num in coconut source)
        self.ub = []  #66 (line num in coconut source)

# lists of indices that are discrete vs. continuous
        self.int_var = []  #69 (line num in coconut source)
        self.cont_var = []  #70 (line num in coconut source)

        self.names = []  #72 (line num in coconut source)
        self.choices = {}  #73 (line num in coconut source)
        for i, (name, (func, args, kwargs)) in enumerate(sorted_items(params)):  #74 (line num in coconut source)
            self.names.append(name)  #75 (line num in coconut source)
            _coconut_case_match_to_0 = func, args  #76 (line num in coconut source)
            _coconut_case_match_check_0 = False  #76 (line num in coconut source)
            _coconut_match_set_name_choices = _coconut_sentinel  #76 (line num in coconut source)
            if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #76 (line num in coconut source)
                _coconut_match_temp_0 = _coconut.tuple(_coconut_case_match_to_0)  #76 (line num in coconut source)
                if (_coconut.len(_coconut_match_temp_0) == 2) and (_coconut_match_temp_0[0] == "choice") and (_coconut.isinstance(_coconut_match_temp_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_0[1]) == 1):  #76 (line num in coconut source)
                    _coconut_match_set_name_choices = _coconut_match_temp_0[1][0]  #76 (line num in coconut source)
                    _coconut_case_match_check_0 = True  #76 (line num in coconut source)
            if _coconut_case_match_check_0:  #76 (line num in coconut source)
                if _coconut_match_set_name_choices is not _coconut_sentinel:  #76 (line num in coconut source)
                    choices = _coconut_match_set_name_choices  #76 (line num in coconut source)
            if _coconut_case_match_check_0:  #76 (line num in coconut source)
                self.lb.append(0)  #78 (line num in coconut source)
                self.ub.append(len(choices) - 1)  #79 (line num in coconut source)
                self.int_var.append(i)  #80 (line num in coconut source)
                self.choices[name] = choices  #81 (line num in coconut source)
            if not _coconut_case_match_check_0:  #82 (line num in coconut source)
                _coconut_match_set_name_start = _coconut_sentinel  #82 (line num in coconut source)
                _coconut_match_set_name_stop = _coconut_sentinel  #82 (line num in coconut source)
                _coconut_match_set_name_step = _coconut_sentinel  #82 (line num in coconut source)
                if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #82 (line num in coconut source)
                    _coconut_match_temp_1 = _coconut.tuple(_coconut_case_match_to_0)  #82 (line num in coconut source)
                    if (_coconut.len(_coconut_match_temp_1) == 2) and (_coconut_match_temp_1[0] == "randrange") and (_coconut.isinstance(_coconut_match_temp_1[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_1[1]) == 3):  #82 (line num in coconut source)
                        _coconut_match_set_name_start = _coconut_match_temp_1[1][0]  #82 (line num in coconut source)
                        _coconut_match_set_name_stop = _coconut_match_temp_1[1][1]  #82 (line num in coconut source)
                        _coconut_match_set_name_step = _coconut_match_temp_1[1][2]  #82 (line num in coconut source)
                        _coconut_case_match_check_0 = True  #82 (line num in coconut source)
                if _coconut_case_match_check_0:  #82 (line num in coconut source)
                    if _coconut_match_set_name_start is not _coconut_sentinel:  #82 (line num in coconut source)
                        start = _coconut_match_set_name_start  #82 (line num in coconut source)
                    if _coconut_match_set_name_stop is not _coconut_sentinel:  #82 (line num in coconut source)
                        stop = _coconut_match_set_name_stop  #82 (line num in coconut source)
                    if _coconut_match_set_name_step is not _coconut_sentinel:  #82 (line num in coconut source)
                        step = _coconut_match_set_name_step  #82 (line num in coconut source)
                if _coconut_case_match_check_0:  #82 (line num in coconut source)
                    rng = range(start, stop, step)  #83 (line num in coconut source)
                    self.lb.append(0)  #84 (line num in coconut source)
                    self.ub.append(len(rng) - 1)  #85 (line num in coconut source)
                    self.int_var.append(i)  #86 (line num in coconut source)
                    self.choices[name] = rng  #87 (line num in coconut source)
            if not _coconut_case_match_check_0:  #88 (line num in coconut source)
                _coconut_match_set_name_start = _coconut_sentinel  #88 (line num in coconut source)
                _coconut_match_set_name_stop = _coconut_sentinel  #88 (line num in coconut source)
                if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #88 (line num in coconut source)
                    _coconut_match_temp_2 = _coconut.tuple(_coconut_case_match_to_0)  #88 (line num in coconut source)
                    if (_coconut.len(_coconut_match_temp_2) == 2) and (_coconut_match_temp_2[0] == "uniform") and (_coconut.isinstance(_coconut_match_temp_2[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_2[1]) == 2):  #88 (line num in coconut source)
                        _coconut_match_set_name_start = _coconut_match_temp_2[1][0]  #88 (line num in coconut source)
                        _coconut_match_set_name_stop = _coconut_match_temp_2[1][1]  #88 (line num in coconut source)
                        _coconut_case_match_check_0 = True  #88 (line num in coconut source)
                if _coconut_case_match_check_0:  #88 (line num in coconut source)
                    if _coconut_match_set_name_start is not _coconut_sentinel:  #88 (line num in coconut source)
                        start = _coconut_match_set_name_start  #88 (line num in coconut source)
                    if _coconut_match_set_name_stop is not _coconut_sentinel:  #88 (line num in coconut source)
                        stop = _coconut_match_set_name_stop  #88 (line num in coconut source)
                if _coconut_case_match_check_0:  #88 (line num in coconut source)
                    self.lb.append(start)  #89 (line num in coconut source)
                    self.ub.append(stop)  #90 (line num in coconut source)
                    self.cont_var.append(i)  #91 (line num in coconut source)
            if not _coconut_case_match_check_0:  #92 (line num in coconut source)
                raise TypeError("insufficiently specified parameter {_coconut_format_0}".format(_coconut_format_0=(name)))  #93 (line num in coconut source)

        self.lb = (np.array)(self.lb)  #95 (line num in coconut source)
        self.ub = (np.array)(self.ub)  #96 (line num in coconut source)
        self.int_var = (np.array)(self.int_var)  #97 (line num in coconut source)
        self.cont_var = (np.array)(self.cont_var)  #98 (line num in coconut source)


    def eval(self, xs):  #100 (line num in coconut source)
        """Set got_values to the given values."""  #101 (line num in coconut source)
        self.__check_input__(xs)  #102 (line num in coconut source)
        self.got_values = {}  #103 (line num in coconut source)
        for i in range(self.dim):  #104 (line num in coconut source)
            name = self.names[i]  #105 (line num in coconut source)
            val = xs[i]  #106 (line num in coconut source)
            _coconut_match_to_0 = self.choices  #107 (line num in coconut source)
            _coconut_match_check_0 = False  #107 (line num in coconut source)
            _coconut_match_set_name_choices = _coconut_sentinel  #107 (line num in coconut source)
            if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #107 (line num in coconut source)
                _coconut_match_temp_3 = _coconut_match_to_0.get(name, _coconut_sentinel)  #107 (line num in coconut source)
                if _coconut_match_temp_3 is not _coconut_sentinel:  #107 (line num in coconut source)
                    _coconut_match_set_name_choices = _coconut_match_temp_3  #107 (line num in coconut source)
                    _coconut_match_check_0 = True  #107 (line num in coconut source)
            if _coconut_match_check_0:  #107 (line num in coconut source)
                if _coconut_match_set_name_choices is not _coconut_sentinel:  #107 (line num in coconut source)
                    choices = _coconut_match_set_name_choices  #107 (line num in coconut source)
            if _coconut_match_check_0:  #107 (line num in coconut source)
                assert val == int(val), val  #108 (line num in coconut source)
                val = choices[int(val)]  #109 (line num in coconut source)
            self.got_values[name] = val  #110 (line num in coconut source)


    def get_points_values(self, new_data, new_losses):  #112 (line num in coconut source)
        """Convert data and losses into pySOT-compatible points and values."""  #113 (line num in coconut source)
        points = []  #114 (line num in coconut source)
        values = []  #115 (line num in coconut source)
        for ex_dict, loss in zip(new_data, new_losses):  #116 (line num in coconut source)
            pt = []  #117 (line num in coconut source)
            for name, val in ex_dict.items():  #118 (line num in coconut source)
                _coconut_match_to_1 = self.choices  #119 (line num in coconut source)
                _coconut_match_check_1 = False  #119 (line num in coconut source)
                _coconut_match_set_name_choices = _coconut_sentinel  #119 (line num in coconut source)
                if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #119 (line num in coconut source)
                    _coconut_match_temp_4 = _coconut_match_to_1.get(name, _coconut_sentinel)  #119 (line num in coconut source)
                    if _coconut_match_temp_4 is not _coconut_sentinel:  #119 (line num in coconut source)
                        _coconut_match_set_name_choices = _coconut_match_temp_4  #119 (line num in coconut source)
                        _coconut_match_check_1 = True  #119 (line num in coconut source)
                if _coconut_match_check_1:  #119 (line num in coconut source)
                    if _coconut_match_set_name_choices is not _coconut_sentinel:  #119 (line num in coconut source)
                        choices = _coconut_match_set_name_choices  #119 (line num in coconut source)
                if _coconut_match_check_1:  #119 (line num in coconut source)
                    chosen_ind = choices.index(val)  #120 (line num in coconut source)
                    pt.append(chosen_ind)  #121 (line num in coconut source)
                else:  #122 (line num in coconut source)
                    pt.append(val)  #123 (line num in coconut source)
            points.append(pt)  #124 (line num in coconut source)
            values.append(loss)  #125 (line num in coconut source)
        return np.array(points), np.array(values)  #126 (line num in coconut source)


# Backend:


_coconut_call_set_names(BBoptOptimizationProblem)  #131 (line num in coconut source)
class PySOTBackend(StandardBackend):  #131 (line num in coconut source)
    """The pySOT backend uses pySOT for black box optimization."""  #132 (line num in coconut source)
    backend_name = "pySOT"  #133 (line num in coconut source)
    implemented_funcs = ("choice", "randrange", "uniform")  #134 (line num in coconut source)

    strategy = None  #140 (line num in coconut source)

    @override  #142 (line num in coconut source)
    def setup_backend(self, params, strategy="SRBF", surrogate="RBF", design=None,):  #143 (line num in coconut source)
        self.opt_problem = BBoptOptimizationProblem(params)  #150 (line num in coconut source)

        design_kwargs = dict(dim=self.opt_problem.dim)  #152 (line num in coconut source)
        _coconut_case_match_to_1 = design  #155 (line num in coconut source)
        _coconut_case_match_check_1 = False  #155 (line num in coconut source)
        if _coconut_case_match_to_1 is None:  #155 (line num in coconut source)
            _coconut_case_match_check_1 = True  #155 (line num in coconut source)
        if _coconut_case_match_check_1:  #155 (line num in coconut source)
            self.exp_design = EmptyExperimentalDesign(**design_kwargs)  #157 (line num in coconut source)
        if not _coconut_case_match_check_1:  #158 (line num in coconut source)
            if _coconut_case_match_to_1 == "latin_hypercube":  #158 (line num in coconut source)
                _coconut_case_match_check_1 = True  #158 (line num in coconut source)
            if _coconut_case_match_check_1:  #158 (line num in coconut source)
                self.exp_design = LatinHypercube(num_pts=2 * (self.opt_problem.dim + 1), **design_kwargs)  #159 (line num in coconut source)
        if not _coconut_case_match_check_1:  #163 (line num in coconut source)
            if _coconut_case_match_to_1 == "symmetric_latin_hypercube":  #163 (line num in coconut source)
                _coconut_case_match_check_1 = True  #163 (line num in coconut source)
            if _coconut_case_match_check_1:  #163 (line num in coconut source)
                self.exp_design = SymmetricLatinHypercube(num_pts=2 * (self.opt_problem.dim + 1), **design_kwargs)  #164 (line num in coconut source)
        if not _coconut_case_match_check_1:  #168 (line num in coconut source)
            if _coconut_case_match_to_1 == "two_factorial":  #168 (line num in coconut source)
                _coconut_case_match_check_1 = True  #168 (line num in coconut source)
            if _coconut_case_match_check_1:  #168 (line num in coconut source)
                self.exp_design = TwoFactorial(**design_kwargs)  #169 (line num in coconut source)
        if not _coconut_case_match_check_1:  #170 (line num in coconut source)
            _coconut_match_set_name_design_cls = _coconut_sentinel  #170 (line num in coconut source)
            _coconut_match_set_name_design_cls = _coconut_case_match_to_1  #170 (line num in coconut source)
            _coconut_case_match_check_1 = True  #170 (line num in coconut source)
            if _coconut_case_match_check_1:  #170 (line num in coconut source)
                if _coconut_match_set_name_design_cls is not _coconut_sentinel:  #170 (line num in coconut source)
                    design_cls = _coconut_match_set_name_design_cls  #170 (line num in coconut source)
            if _coconut_case_match_check_1 and not (callable(design_cls)):  #170 (line num in coconut source)
                _coconut_case_match_check_1 = False  #170 (line num in coconut source)
            if _coconut_case_match_check_1:  #170 (line num in coconut source)
                self.exp_design = design_cls(**design_kwargs)  #171 (line num in coconut source)
        if not _coconut_case_match_check_1:  #172 (line num in coconut source)
            raise TypeError("unknown experimental design {_coconut_format_0!r}".format(_coconut_format_0=(design)))  #173 (line num in coconut source)

        surrogate_kwargs = dict(dim=self.opt_problem.dim, lb=self.opt_problem.lb, ub=self.opt_problem.ub)  #175 (line num in coconut source)
        _coconut_case_match_to_2 = surrogate  #180 (line num in coconut source)
        _coconut_case_match_check_2 = False  #180 (line num in coconut source)
        if _coconut_case_match_to_2 == "RBF":  #180 (line num in coconut source)
            _coconut_case_match_check_2 = True  #180 (line num in coconut source)
        if _coconut_case_match_check_2:  #180 (line num in coconut source)
            self.surrogate = RBFInterpolant(kernel=LinearKernel() if design is None else CubicKernel(), tail=ConstantTail(self.opt_problem.dim) if design is None else LinearTail(self.opt_problem.dim), **surrogate_kwargs)  #182 (line num in coconut source)
        if not _coconut_case_match_check_2:  #187 (line num in coconut source)
            if _coconut_case_match_to_2 == "GP":  #187 (line num in coconut source)
                _coconut_case_match_check_2 = True  #187 (line num in coconut source)
            if _coconut_case_match_check_2:  #187 (line num in coconut source)
                self.surrogate = GPRegressor(**surrogate_kwargs)  #188 (line num in coconut source)
        if not _coconut_case_match_check_2:  #189 (line num in coconut source)
            _coconut_match_set_name_surrogate_cls = _coconut_sentinel  #189 (line num in coconut source)
            _coconut_match_set_name_surrogate_cls = _coconut_case_match_to_2  #189 (line num in coconut source)
            _coconut_case_match_check_2 = True  #189 (line num in coconut source)
            if _coconut_case_match_check_2:  #189 (line num in coconut source)
                if _coconut_match_set_name_surrogate_cls is not _coconut_sentinel:  #189 (line num in coconut source)
                    surrogate_cls = _coconut_match_set_name_surrogate_cls  #189 (line num in coconut source)
            if _coconut_case_match_check_2 and not (callable(surrogate_cls)):  #189 (line num in coconut source)
                _coconut_case_match_check_2 = False  #189 (line num in coconut source)
            if _coconut_case_match_check_2:  #189 (line num in coconut source)
                self.surrogate = surrogate_cls(**surrogate_kwargs)  #190 (line num in coconut source)
        if not _coconut_case_match_check_2:  #191 (line num in coconut source)
            raise TypeError("unknown surrogate {_coconut_format_0!r}".format(_coconut_format_0=(surrogate)))  #192 (line num in coconut source)

        strategy_kwargs = dict(max_evals=sys.maxsize, opt_prob=self.opt_problem, exp_design=self.exp_design, surrogate=self.surrogate, asynchronous=True, batch_size=1)  #194 (line num in coconut source)
        _coconut_case_match_to_3 = strategy  #202 (line num in coconut source)
        _coconut_case_match_check_3 = False  #202 (line num in coconut source)
        if _coconut_case_match_to_3 == "SRBF":  #202 (line num in coconut source)
            _coconut_case_match_check_3 = True  #202 (line num in coconut source)
        if _coconut_case_match_check_3:  #202 (line num in coconut source)
            self.strategy = SRBFStrategy(**strategy_kwargs)  #204 (line num in coconut source)
        if not _coconut_case_match_check_3:  #205 (line num in coconut source)
            if _coconut_case_match_to_3 == "EI":  #205 (line num in coconut source)
                _coconut_case_match_check_3 = True  #205 (line num in coconut source)
            if _coconut_case_match_check_3:  #205 (line num in coconut source)
                self.strategy = EIStrategy(**strategy_kwargs)  #206 (line num in coconut source)
        if not _coconut_case_match_check_3:  #207 (line num in coconut source)
            if _coconut_case_match_to_3 == "DYCORS":  #207 (line num in coconut source)
                _coconut_case_match_check_3 = True  #207 (line num in coconut source)
            if _coconut_case_match_check_3:  #207 (line num in coconut source)
                self.strategy = DYCORSStrategy(**strategy_kwargs)  #208 (line num in coconut source)
        if not _coconut_case_match_check_3:  #209 (line num in coconut source)
            if _coconut_case_match_to_3 == "LCB":  #209 (line num in coconut source)
                _coconut_case_match_check_3 = True  #209 (line num in coconut source)
            if _coconut_case_match_check_3:  #209 (line num in coconut source)
                self.strategy = LCBStrategy(**strategy_kwargs)  #210 (line num in coconut source)
        if not _coconut_case_match_check_3:  #211 (line num in coconut source)
            _coconut_match_set_name_strategy_cls = _coconut_sentinel  #211 (line num in coconut source)
            _coconut_match_set_name_strategy_cls = _coconut_case_match_to_3  #211 (line num in coconut source)
            _coconut_case_match_check_3 = True  #211 (line num in coconut source)
            if _coconut_case_match_check_3:  #211 (line num in coconut source)
                if _coconut_match_set_name_strategy_cls is not _coconut_sentinel:  #211 (line num in coconut source)
                    strategy_cls = _coconut_match_set_name_strategy_cls  #211 (line num in coconut source)
            if _coconut_case_match_check_3 and not (callable(strategy_cls)):  #211 (line num in coconut source)
                _coconut_case_match_check_3 = False  #211 (line num in coconut source)
            if _coconut_case_match_check_3:  #211 (line num in coconut source)
                self.strategy = strategy_cls(**strategy_kwargs)  #212 (line num in coconut source)
        if not _coconut_case_match_check_3:  #213 (line num in coconut source)
            raise TypeError("unknown strategy {_coconut_format_0!r}".format(_coconut_format_0=(strategy)))  #214 (line num in coconut source)


    @override  #216 (line num in coconut source)
    def tell_data(self, new_data, new_losses):  #217 (line num in coconut source)
        """Special method that allows fast updating of the backend with new examples."""  #218 (line num in coconut source)
        points, values = self.opt_problem.get_points_values(new_data, new_losses)  #219 (line num in coconut source)
        for i in range(points.shape[0]):  #220 (line num in coconut source)
            X = np.copy(points[i, :])  #221 (line num in coconut source)
            self.strategy.X = np.vstack((self.strategy.X, X))  #222 (line num in coconut source)
            self.strategy._X = np.vstack((self.strategy._X, X))  #223 (line num in coconut source)
            self.strategy.fX = np.vstack((self.strategy.fX, values[i]))  #224 (line num in coconut source)
            self.strategy._fX = np.vstack((self.strategy._fX, values[i]))  #225 (line num in coconut source)
            assert self.surrogate is self.strategy.surrogate, (self.surrogate, self.strategy.surrogate)  #226 (line num in coconut source)
            self.surrogate.add_points(X, values[i])  #227 (line num in coconut source)


    @override  #229 (line num in coconut source)
    def get_next_values(self):  #230 (line num in coconut source)
        """Special method to get the next set of values to evaluate."""  #231 (line num in coconut source)
        assert self.strategy._X.shape[0] > 0, self.strategy._X  #232 (line num in coconut source)
        assert self.surrogate.num_pts > 0, self.surrogate.num_pts  #233 (line num in coconut source)

        while True:  #235 (line num in coconut source)
            proposal = self.strategy.propose_action()  #236 (line num in coconut source)
            assert proposal, proposal  #237 (line num in coconut source)
            if proposal.action == "terminate":  #238 (line num in coconut source)
                proposal.accept()  #239 (line num in coconut source)
            elif proposal.action == "eval":  #240 (line num in coconut source)
                self.opt_problem.eval(*proposal.args)  #241 (line num in coconut source)
                self.strategy.pending_evals -= 1  #242 (line num in coconut source)
                self.strategy.remove_pending(proposal.args[0])  #243 (line num in coconut source)
                break  #244 (line num in coconut source)
            else:  #245 (line num in coconut source)
                proposal.reject()  #246 (line num in coconut source)

        assert self.opt_problem.got_values is not None, "pySOT optimization produced no values"  #248 (line num in coconut source)
        return self.opt_problem.got_values  #249 (line num in coconut source)


# Registered names:


_coconut_call_set_names(PySOTBackend)  #254 (line num in coconut source)
PySOTBackend.register()  #254 (line num in coconut source)
PySOTBackend.register_alias("pysot")  #255 (line num in coconut source)

# strategy-based, default design algs
PySOTBackend.register_alg("stochastic_radial_basis_function", strategy="SRBF", surrogate="RBF")  #258 (line num in coconut source)
PySOTBackend.register_alg("expected_improvement", strategy="EI", surrogate="GP")  #259 (line num in coconut source)
PySOTBackend.register_alg("DYCORS", strategy="DYCORS", surrogate="RBF")  #260 (line num in coconut source)
PySOTBackend.register_alg("lower_confidence_bound", strategy="LCB", surrogate="GP")  #261 (line num in coconut source)

# design-based, default strategy algs
PySOTBackend.register_alg("latin_hypercube", design="latin_hypercube")  #264 (line num in coconut source)
PySOTBackend.register_alg("symmetric_latin_hypercube", design="symmetric_latin_hypercube")  #265 (line num in coconut source)
PySOTBackend.register_alg("two_factorial", design="two_factorial")  #266 (line num in coconut source)

# register meta alg
PySOTBackend.register_meta_for_all_algs("any_pysot")  #269 (line num in coconut source)
