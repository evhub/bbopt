#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x71aff698

# Compiled with Coconut version 1.5.0-post_dev57 [Fish License]

"""
The scikit-optimize backend. Does black box optimization using scikit-optimize.
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



from functools import wraps

from skopt import Optimizer
from skopt.space import Categorical
from skopt.space import Integer
from skopt.space import Real

from bbopt.util import sorted_items
from bbopt.backends.util import StandardBackend
from bbopt.backends.util import split_examples
from bbopt.backends.util import make_values


# attempt to fix skopt errors by patching sklearn
try:
    import sklearn
except ImportError:
    pass
else:

# patch sklearn.utils.optimize._check_optimize_result
    try:
        old_check_optimize_result = sklearn.utils.optimize._check_optimize_result

        @wraps(old_check_optimize_result)
        def new_check_optimize_result(solver, result, *args, **kwargs):
            if not isinstance(result.message, bytes):
                result.message = result.message.encode("latin1")
            return old_check_optimize_result(solver, result, *args, **kwargs)

        sklearn.utils.optimize._check_optimize_result = new_check_optimize_result
        sklearn.gaussian_process._gpr._check_optimize_result = new_check_optimize_result
    except AttributeError:
        pass

# patch sklearn.utils.fixes.sp_version
    try:
        sklearn.utils.fixes.sp_version < (1,)
    except TypeError:
        Version = type(sklearn.utils.fixes.sp_version)
        old_lt = Version.__lt__
        old_le = Version.__le__
        old_gt = Version.__gt__
        old_ge = Version.__ge__
        try:
            try:
                _coconut_name_store_0 = __lt__
            except _coconut.NameError:
                _coconut_name_store_0 = _coconut_sentinel
            def __lt__(self, other):
                try:
                    result = old_lt(self, other)
                except (TypeError, NotImplementedError):
                    result = NotImplemented
                if result is NotImplemented:
                    return self.release < other
                else:
                    return result
            Version.__lt__ = __lt__
            if _coconut_name_store_0 is not _coconut_sentinel:
                __lt__ = _coconut_name_store_0
            try:
                _coconut_name_store_1 = __le__
            except _coconut.NameError:
                _coconut_name_store_1 = _coconut_sentinel
            def __le__(self, other):
                try:
                    result = old_le(self, other)
                except (TypeError, NotImplementedError):
                    result = NotImplemented
                if result is NotImplemented:
                    return self.release <= other
                else:
                    return result
            Version.__le__ = __le__
            if _coconut_name_store_1 is not _coconut_sentinel:
                __le__ = _coconut_name_store_1
            try:
                _coconut_name_store_2 = __gt__
            except _coconut.NameError:
                _coconut_name_store_2 = _coconut_sentinel
            def __gt__(self, other):
                try:
                    result = old_gt(self, other)
                except (TypeError, NotImplementedError):
                    result = NotImplemented
                if result is NotImplemented:
                    return self.release > other
                else:
                    return result
            Version.__gt__ = __gt__
            if _coconut_name_store_2 is not _coconut_sentinel:
                __gt__ = _coconut_name_store_2
            try:
                _coconut_name_store_3 = __ge__
            except _coconut.NameError:
                _coconut_name_store_3 = _coconut_sentinel
            def __ge__(self, other):
                try:
                    result = old_ge(self, other)
                except (TypeError, NotImplementedError):
                    result = NotImplemented
                if result is NotImplemented:
                    return self.release >= other
                else:
                    return result
            Version.__ge__ = __ge__
            if _coconut_name_store_3 is not _coconut_sentinel:
                __ge__ = _coconut_name_store_3
        except TypeError:
            pass


# Utilities:

def guess_n_initial_points(params):
    """Guess a good value for n_initial_points given params."""
    return max(len(params), min(len(params) * 2, 10))


def create_space(name, func, *args):
    """Create a scikit-optimize space for the given parameter."""
    name = py_str(name)
    _coconut_case_match_to_0 = func, args
    _coconut_case_match_check_0 = False
    if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == "choice") and (_coconut.isinstance(_coconut_case_match_to_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0[1]) == 1):
        choices = _coconut_case_match_to_0[1][0]
        _coconut_case_match_check_0 = True
    if _coconut_case_match_check_0:
        return Categorical(choices, name=name)
    if not _coconut_case_match_check_0:
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == "randrange") and (_coconut.isinstance(_coconut_case_match_to_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0[1]) == 3):
            start = _coconut_case_match_to_0[1][0]
            stop = _coconut_case_match_to_0[1][1]
            step = _coconut_case_match_to_0[1][2]
            _coconut_case_match_check_0 = True
        if _coconut_case_match_check_0:
            if step != 1:
                raise ValueError("the scikit-optimize backend only supports a randrange step size of 1")
            stop -= 1  # scikit-optimize ranges are inclusive
            return Integer(start, stop, name=name)
    if not _coconut_case_match_check_0:
        if (_coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0) == 2) and (_coconut_case_match_to_0[0] == "uniform") and (_coconut.isinstance(_coconut_case_match_to_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_case_match_to_0[1]) == 2):
            a = _coconut_case_match_to_0[1][0]
            b = _coconut_case_match_to_0[1][1]
            _coconut_case_match_check_0 = True
        if _coconut_case_match_check_0:
            return Real(a, b, name=name)
    raise TypeError("invalid parameter {_coconut_format_0}".format(_coconut_format_0=(name)))


def create_dimensions(params):
    """Construct the full optimization space for the given parameters."""
    return [create_space(name, func, *args) for name, (func, args, kwargs) in sorted_items(params)]


# Backend:

class SkoptBackend(StandardBackend):
    """The scikit-optimize backend uses scikit-optimize for black box optimization."""
    backend_name = "scikit-optimize"
    implemented_funcs = ("choice", "randrange", "uniform",)

    @override
    def setup_backend(self, params, base_estimator="GP", n_initial_points=None, **options):
        """Special method to initialize the backend from params."""
        self.params = params
        if isinstance(base_estimator, str):
            base_estimator = py_str(base_estimator)
        if n_initial_points is None:
            n_initial_points = guess_n_initial_points(params)
        self.optimizer = Optimizer(create_dimensions(params), base_estimator, n_initial_points=n_initial_points, **options)

    @override
    def tell_examples(self, new_examples):
        """Special method that allows fast updating of the backend with new examples."""
        data_points, losses = split_examples(new_examples, self.params)
        self.result = self.optimizer.tell(data_points, losses)

        current_point = self.optimizer.ask()
        self.current_values = make_values(self.params, current_point)

    @property
    def space(self):
        """The space over which optimization was performed."""
        return self.optimizer.space

    @property
    def model(self):
        """Get the most recently fit model."""
        return self.optimizer.models[-1]


# Registered names:

_coconut_call_set_names(SkoptBackend)
SkoptBackend.register()
SkoptBackend.register_alias("skopt")

SkoptBackend.register_alg("gaussian_process", base_estimator="GP")
SkoptBackend.register_alg("random_forest", base_estimator="RF")
SkoptBackend.register_alg("extra_trees", base_estimator="ET")
SkoptBackend.register_alg("gradient_boosted_regression_trees", base_estimator="GBRT")

SkoptBackend.register_meta_for_all_algs("any_skopt")
