#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xe28c5b02

# Compiled with Coconut version 1.5.0-post_dev7 [Fish License]

"""
The pySOT backend. Does black box optimization using pySOT.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import *
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



sys = _coconut_sys

import numpy as np

from pySOT.optimization_problems.optimization_problem import OptimizationProblem
from pySOT.experimental_design import ExperimentalDesign
from pySOT.experimental_design import LatinHypercube
from pySOT.experimental_design import SymmetricLatinHypercube
from pySOT.experimental_design import TwoFactorial
from pySOT.surrogate import RBFInterpolant
from pySOT.surrogate import GPRegressor
from pySOT.surrogate.kernels import CubicKernel
from pySOT.surrogate.kernels import LinearKernel
from pySOT.surrogate.tails import ConstantTail
from pySOT.surrogate.tails import LinearTail
from pySOT.strategy import SRBFStrategy
from pySOT.strategy import EIStrategy
from pySOT.strategy import DYCORSStrategy
from pySOT.strategy import LCBStrategy

from bbopt.util import sorted_items
from bbopt.backends.util import StandardBackend


# Utilities:

class EmptyExperimentalDesign(ExperimentalDesign):
    num_pts = 0

    def __init__(self, dim):
        self.dim = dim

    def generate_points(self, lb=None, ub=None, int_var=None):
        return np.empty((0, self.dim))

class GotValuesException(Exception): pass

class BBoptOptimizationProblem(OptimizationProblem):
    def __init__(self, params):
        self.params = params
        self.dim = len(params)
        self.got_values = None

# lower and upper bounds; len must match self.dim
        self.lb = []
        self.ub = []

# lists of indices that are discrete vs. continuous
        self.int_var = []
        self.cont_var = []

        self.names = []
        self.choices = {}
        for i, (name, (func, args, kwargs)) in enumerate(sorted_items(params)):
            self.names.append(name)
            _coconut_match_to = func, args
            _coconut_case_check_0 = False
            if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == "choice") and (_coconut.isinstance(_coconut_match_to[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to[1]) == 1):
                choices = _coconut_match_to[1][0]
                _coconut_case_check_0 = True
            if _coconut_case_check_0:
                self.lb.append(0)
                self.ub.append(len(choices) - 1)
                self.int_var.append(i)
                self.choices[name] = choices
            if not _coconut_case_check_0:
                if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == "randrange") and (_coconut.isinstance(_coconut_match_to[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to[1]) == 3):
                    start = _coconut_match_to[1][0]
                    stop = _coconut_match_to[1][1]
                    step = _coconut_match_to[1][2]
                    _coconut_case_check_0 = True
                if _coconut_case_check_0:
                    rng = range(start, stop, step)
                    self.lb.append(0)
                    self.ub.append(len(rng) - 1)
                    self.int_var.append(i)
                    self.choices[name] = rng
            if not _coconut_case_check_0:
                if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to) == 2) and (_coconut_match_to[0] == "uniform") and (_coconut.isinstance(_coconut_match_to[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_to[1]) == 2):
                    start = _coconut_match_to[1][0]
                    stop = _coconut_match_to[1][1]
                    _coconut_case_check_0 = True
                if _coconut_case_check_0:
                    self.lb.append(start)
                    self.ub.append(stop)
                    self.cont_var.append(i)
            if not _coconut_case_check_0:
                raise TypeError("insufficiently specified parameter {_coconut_format_0}".format(_coconut_format_0=(name)))

        self.lb = (np.array)(self.lb)
        self.ub = (np.array)(self.ub)
        self.int_var = (np.array)(self.int_var)
        self.cont_var = (np.array)(self.cont_var)

    def eval(self, xs):
        """Set got_values to the given values."""
        self.__check_input__(xs)
        self.got_values = {}
        for i in range(self.dim):
            name = self.names[i]
            val = xs[i]
            _coconut_match_to = self.choices
            _coconut_match_check = False
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
                if _coconut_match_temp_0 is not _coconut_sentinel:
                    choices = _coconut_match_temp_0
                    _coconut_match_check = True
            if _coconut_match_check:
                assert val == int(val), val
                val = choices[int(val)]
            self.got_values[name] = val

    def get_points_values(self, new_data, new_losses):
        """Convert data and losses into pySOT-compatible points and values."""
        points = []
        values = []
        for ex_dict, loss in zip(new_data, new_losses):
            pt = []
            for name, val in ex_dict.items():
                _coconut_match_to = self.choices
                _coconut_match_check = False
                if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                    _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
                    if _coconut_match_temp_0 is not _coconut_sentinel:
                        choices = _coconut_match_temp_0
                        _coconut_match_check = True
                if _coconut_match_check:
                    chosen_ind = choices.index(val)
                    pt.append(chosen_ind)
                else:
                    pt.append(val)
            points.append(pt)
            values.append(loss)
        return np.array(points), np.array(values)


# Backend:

class PySOTBackend(StandardBackend):
    """The pySOT backend uses pySOT for black box optimization."""
    backend_name = "pySOT"
    implemented_funcs = ("choice", "randrange", "uniform",)

    strategy = None

    def setup_backend(self, params, strategy="SRBF", surrogate="RBF", design="symmetric_latin_hypercube",):
        self.opt_problem = BBoptOptimizationProblem(params)

        design_kwargs = dict(dim=self.opt_problem.dim)
        _coconut_match_to = design
        _coconut_case_check_1 = False
        if _coconut_match_to is None:
            _coconut_case_check_1 = True
        if _coconut_case_check_1:
            self.exp_design = EmptyExperimentalDesign(**design_kwargs)
        if not _coconut_case_check_1:
            if _coconut_match_to == "latin_hypercube":
                _coconut_case_check_1 = True
            if _coconut_case_check_1:
                self.exp_design = LatinHypercube(num_pts=2 * (self.opt_problem.dim + 1), **design_kwargs)
        if not _coconut_case_check_1:
            if _coconut_match_to == "symmetric_latin_hypercube":
                _coconut_case_check_1 = True
            if _coconut_case_check_1:
                self.exp_design = SymmetricLatinHypercube(num_pts=2 * (self.opt_problem.dim + 1), **design_kwargs)
        if not _coconut_case_check_1:
            if _coconut_match_to == "two_factorial":
                _coconut_case_check_1 = True
            if _coconut_case_check_1:
                self.exp_design = TwoFactorial(**design_kwargs)
        if not _coconut_case_check_1:
            design_cls = _coconut_match_to
            _coconut_case_check_1 = True
            if _coconut_case_check_1 and not (callable(design_cls)):
                _coconut_case_check_1 = False
            if _coconut_case_check_1:
                self.exp_design = design_cls(**design_kwargs)
        if not _coconut_case_check_1:
            raise TypeError("unknown experimental design {_coconut_format_0!r}".format(_coconut_format_0=(design)))

        surrogate_kwargs = dict(dim=self.opt_problem.dim, lb=self.opt_problem.lb, ub=self.opt_problem.ub)
        _coconut_match_to = surrogate
        _coconut_case_check_2 = False
        if _coconut_match_to == "RBF":
            _coconut_case_check_2 = True
        if _coconut_case_check_2:
            self.surrogate = RBFInterpolant(kernel=LinearKernel() if design is None else CubicKernel(), tail=ConstantTail(self.opt_problem.dim) if design is None else LinearTail(self.opt_problem.dim), **surrogate_kwargs)
        if not _coconut_case_check_2:
            if _coconut_match_to == "GP":
                _coconut_case_check_2 = True
            if _coconut_case_check_2:
                self.surrogate = GPRegressor(**surrogate_kwargs)
        if not _coconut_case_check_2:
            surrogate_cls = _coconut_match_to
            _coconut_case_check_2 = True
            if _coconut_case_check_2 and not (callable(surrogate_cls)):
                _coconut_case_check_2 = False
            if _coconut_case_check_2:
                self.surrogate = surrogate_cls(**surrogate_kwargs)
        if not _coconut_case_check_2:
            raise TypeError("unknown surrogate {_coconut_format_0!r}".format(_coconut_format_0=(surrogate)))

        strategy_kwargs = dict(max_evals=sys.maxsize, opt_prob=self.opt_problem, exp_design=self.exp_design, surrogate=self.surrogate, asynchronous=True, batch_size=1)
        _coconut_match_to = strategy
        _coconut_case_check_3 = False
        if _coconut_match_to == "SRBF":
            _coconut_case_check_3 = True
        if _coconut_case_check_3:
            self.strategy = SRBFStrategy(**strategy_kwargs)
        if not _coconut_case_check_3:
            if _coconut_match_to == "EI":
                _coconut_case_check_3 = True
            if _coconut_case_check_3:
                self.strategy = EIStrategy(**strategy_kwargs)
        if not _coconut_case_check_3:
            if _coconut_match_to == "DYCORS":
                _coconut_case_check_3 = True
            if _coconut_case_check_3:
                self.strategy = DYCORSStrategy(**strategy_kwargs)
        if not _coconut_case_check_3:
            if _coconut_match_to == "LCB":
                _coconut_case_check_3 = True
            if _coconut_case_check_3:
                self.strategy = LCBStrategy(**strategy_kwargs)
        if not _coconut_case_check_3:
            strategy_cls = _coconut_match_to
            _coconut_case_check_3 = True
            if _coconut_case_check_3 and not (callable(strategy_cls)):
                _coconut_case_check_3 = False
            if _coconut_case_check_3:
                self.strategy = strategy_cls(**strategy_kwargs)
        if not _coconut_case_check_3:
            raise TypeError("unknown strategy {_coconut_format_0!r}".format(_coconut_format_0=(strategy)))

    def tell_data(self, new_data, new_losses):
        """Special method that allows fast updating of the backend with new examples."""
        points, values = self.opt_problem.get_points_values(new_data, new_losses)
        for i in range(points.shape[0]):
            X = np.copy(points[i, :])
            self.strategy.X = np.vstack((self.strategy.X, X))
            self.strategy._X = np.vstack((self.strategy._X, X))
            self.strategy.fX = np.vstack((self.strategy.fX, values[i]))
            self.strategy._fX = np.vstack((self.strategy._fX, values[i]))
            assert self.surrogate is self.strategy.surrogate, (self.surrogate, self.strategy.surrogate)
            self.surrogate.add_points(X, values[i])

    def get_next_values(self):
        """Special method to get the next set of values to evaluate."""
        assert self.strategy._X.shape[0] > 0, self.strategy._X
        assert self.surrogate.num_pts > 0, self.surrogate.num_pts

        while True:
            proposal = self.strategy.propose_action()
            assert proposal, proposal
            if proposal.action == "terminate":
                proposal.accept()
            elif proposal.action == "eval":
                self.opt_problem.eval(*proposal.args)
                self.strategy.pending_evals -= 1
                self.strategy.remove_pending(proposal.args[0])
                break
            else:
                proposal.reject()

        assert self.opt_problem.got_values is not None, "pySOT optimization produced no values"
        return self.opt_problem.got_values


# Registered names:

PySOTBackend.register()
PySOTBackend.register_alias("pysot")
PySOTBackend.register_alg("stochastic_radial_basis_function", strategy="SRBF", surrogate="RBF")
PySOTBackend.register_alg("expected_improvement", strategy="EI", surrogate="GP")
PySOTBackend.register_alg("DYCORS", strategy="DYCORS", surrogate="RBF")
PySOTBackend.register_alg("lower_confidence_bound", strategy="LCB", surrogate="GP")
