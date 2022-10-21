#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xb5637b07

# Compiled with Coconut version 2.0.0-post_dev23 [How Not to Be Seen]

"""
The scikit-optimize backend. Does black box optimization using scikit-optimize.
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



from functools import wraps  #5 (line in Coconut source)

from skopt import Optimizer  #7 (line in Coconut source)
from skopt.space import Categorical  #8 (line in Coconut source)
from skopt.space import Integer  #8 (line in Coconut source)
from skopt.space import Real  #8 (line in Coconut source)

from bbopt.util import sorted_items  #14 (line in Coconut source)
from bbopt.backends.util import StandardBackend  #15 (line in Coconut source)
from bbopt.backends.util import split_examples  #15 (line in Coconut source)
from bbopt.backends.util import make_values  #15 (line in Coconut source)


# attempt to fix skopt errors by patching sklearn
try:  #23 (line in Coconut source)
    import sklearn  #24 (line in Coconut source)
except ImportError:  #25 (line in Coconut source)
    pass  #26 (line in Coconut source)
else:  #27 (line in Coconut source)

# patch sklearn.utils.optimize._check_optimize_result
    try:  #30 (line in Coconut source)
        old_check_optimize_result = sklearn.utils.optimize._check_optimize_result  #31 (line in Coconut source)

        @wraps(old_check_optimize_result)  #33 (line in Coconut source)
        def new_check_optimize_result(solver, result, *args, **kwargs):  #34 (line in Coconut source)
            if not isinstance(result.message, bytes):  #35 (line in Coconut source)
                result.message = result.message.encode("latin1")  #36 (line in Coconut source)
            return old_check_optimize_result(solver, result, *args, **kwargs)  #37 (line in Coconut source)


        sklearn.utils.optimize._check_optimize_result = new_check_optimize_result  #39 (line in Coconut source)
        sklearn.gaussian_process._gpr._check_optimize_result = new_check_optimize_result  #40 (line in Coconut source)
    except AttributeError:  #41 (line in Coconut source)
        pass  #42 (line in Coconut source)

# patch sklearn.utils.fixes.sp_version
    try:  #45 (line in Coconut source)
        sklearn.utils.fixes.sp_version < (1,)  #46 (line in Coconut source)
    except TypeError:  #47 (line in Coconut source)
        Version = type(sklearn.utils.fixes.sp_version)  #48 (line in Coconut source)
        old_lt = Version.__lt__  #49 (line in Coconut source)
        old_le = Version.__le__  #50 (line in Coconut source)
        old_gt = Version.__gt__  #51 (line in Coconut source)
        old_ge = Version.__ge__  #52 (line in Coconut source)
        try:  #53 (line in Coconut source)
            try:  #54 (line in Coconut source)
                _coconut_name_store_0 = __lt__  #54 (line in Coconut source)
            except _coconut.NameError:  #54 (line in Coconut source)
                _coconut_name_store_0 = _coconut_sentinel  #54 (line in Coconut source)
            def __lt__(self, other):  #54 (line in Coconut source)
                try:  #55 (line in Coconut source)
                    result = old_lt(self, other)  #56 (line in Coconut source)
                except (TypeError, NotImplementedError):  #57 (line in Coconut source)
                    result = NotImplemented  #58 (line in Coconut source)
                if result is NotImplemented:  #59 (line in Coconut source)
                    return self.release < other  #60 (line in Coconut source)
                else:  #61 (line in Coconut source)
                    return result  #62 (line in Coconut source)
            Version.__lt__ = __lt__  #63 (line in Coconut source)
            if _coconut_name_store_0 is not _coconut_sentinel:  #63 (line in Coconut source)
                __lt__ = _coconut_name_store_0  #63 (line in Coconut source)

            try:  #63 (line in Coconut source)
                _coconut_name_store_1 = __le__  #63 (line in Coconut source)
            except _coconut.NameError:  #63 (line in Coconut source)
                _coconut_name_store_1 = _coconut_sentinel  #63 (line in Coconut source)
            def __le__(self, other):  #63 (line in Coconut source)
                try:  #64 (line in Coconut source)
                    result = old_le(self, other)  #65 (line in Coconut source)
                except (TypeError, NotImplementedError):  #66 (line in Coconut source)
                    result = NotImplemented  #67 (line in Coconut source)
                if result is NotImplemented:  #68 (line in Coconut source)
                    return self.release <= other  #69 (line in Coconut source)
                else:  #70 (line in Coconut source)
                    return result  #71 (line in Coconut source)
            Version.__le__ = __le__  #72 (line in Coconut source)
            if _coconut_name_store_1 is not _coconut_sentinel:  #72 (line in Coconut source)
                __le__ = _coconut_name_store_1  #72 (line in Coconut source)

            try:  #72 (line in Coconut source)
                _coconut_name_store_2 = __gt__  #72 (line in Coconut source)
            except _coconut.NameError:  #72 (line in Coconut source)
                _coconut_name_store_2 = _coconut_sentinel  #72 (line in Coconut source)
            def __gt__(self, other):  #72 (line in Coconut source)
                try:  #73 (line in Coconut source)
                    result = old_gt(self, other)  #74 (line in Coconut source)
                except (TypeError, NotImplementedError):  #75 (line in Coconut source)
                    result = NotImplemented  #76 (line in Coconut source)
                if result is NotImplemented:  #77 (line in Coconut source)
                    return self.release > other  #78 (line in Coconut source)
                else:  #79 (line in Coconut source)
                    return result  #80 (line in Coconut source)
            Version.__gt__ = __gt__  #81 (line in Coconut source)
            if _coconut_name_store_2 is not _coconut_sentinel:  #81 (line in Coconut source)
                __gt__ = _coconut_name_store_2  #81 (line in Coconut source)

            try:  #81 (line in Coconut source)
                _coconut_name_store_3 = __ge__  #81 (line in Coconut source)
            except _coconut.NameError:  #81 (line in Coconut source)
                _coconut_name_store_3 = _coconut_sentinel  #81 (line in Coconut source)
            def __ge__(self, other):  #81 (line in Coconut source)
                try:  #82 (line in Coconut source)
                    result = old_ge(self, other)  #83 (line in Coconut source)
                except (TypeError, NotImplementedError):  #84 (line in Coconut source)
                    result = NotImplemented  #85 (line in Coconut source)
                if result is NotImplemented:  #86 (line in Coconut source)
                    return self.release >= other  #87 (line in Coconut source)
                else:  #88 (line in Coconut source)
                    return result  #89 (line in Coconut source)
            Version.__ge__ = __ge__  #90 (line in Coconut source)
            if _coconut_name_store_3 is not _coconut_sentinel:  #90 (line in Coconut source)
                __ge__ = _coconut_name_store_3  #90 (line in Coconut source)

        except TypeError:  #90 (line in Coconut source)
            pass  #91 (line in Coconut source)


# Utilities:

def guess_n_initial_points(params):  #96 (line in Coconut source)
    """Guess a good value for n_initial_points given params."""  #97 (line in Coconut source)
    return max(len(params), min(len(params) * 2, 10))  #98 (line in Coconut source)



def create_space(name, func, *args):  #104 (line in Coconut source)
    """Create a scikit-optimize space for the given parameter."""  #105 (line in Coconut source)
    name = py_str(name)  #106 (line in Coconut source)
    _coconut_case_match_to_0 = func, args  #107 (line in Coconut source)
    _coconut_case_match_check_0 = False  #107 (line in Coconut source)
    _coconut_match_set_name_choices = _coconut_sentinel  #107 (line in Coconut source)
    if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #107 (line in Coconut source)
        _coconut_match_temp_0 = _coconut.tuple(_coconut_case_match_to_0)  #107 (line in Coconut source)
        if (_coconut.len(_coconut_match_temp_0) == 2) and (_coconut_match_temp_0[0] == "choice") and (_coconut.isinstance(_coconut_match_temp_0[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_0[1]) == 1):  #107 (line in Coconut source)
            _coconut_match_set_name_choices = _coconut_match_temp_0[1][0]  #107 (line in Coconut source)
            _coconut_case_match_check_0 = True  #107 (line in Coconut source)
    if _coconut_case_match_check_0:  #107 (line in Coconut source)
        if _coconut_match_set_name_choices is not _coconut_sentinel:  #107 (line in Coconut source)
            choices = _coconut_match_set_name_choices  #107 (line in Coconut source)
    if _coconut_case_match_check_0:  #107 (line in Coconut source)
        return Categorical(choices, name=name)  #109 (line in Coconut source)
    if not _coconut_case_match_check_0:  #110 (line in Coconut source)
        _coconut_match_set_name_start = _coconut_sentinel  #110 (line in Coconut source)
        _coconut_match_set_name_stop = _coconut_sentinel  #110 (line in Coconut source)
        _coconut_match_set_name_step = _coconut_sentinel  #110 (line in Coconut source)
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #110 (line in Coconut source)
            _coconut_match_temp_1 = _coconut.tuple(_coconut_case_match_to_0)  #110 (line in Coconut source)
            if (_coconut.len(_coconut_match_temp_1) == 2) and (_coconut_match_temp_1[0] == "randrange") and (_coconut.isinstance(_coconut_match_temp_1[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_1[1]) == 3):  #110 (line in Coconut source)
                _coconut_match_set_name_start = _coconut_match_temp_1[1][0]  #110 (line in Coconut source)
                _coconut_match_set_name_stop = _coconut_match_temp_1[1][1]  #110 (line in Coconut source)
                _coconut_match_set_name_step = _coconut_match_temp_1[1][2]  #110 (line in Coconut source)
                _coconut_case_match_check_0 = True  #110 (line in Coconut source)
        if _coconut_case_match_check_0:  #110 (line in Coconut source)
            if _coconut_match_set_name_start is not _coconut_sentinel:  #110 (line in Coconut source)
                start = _coconut_match_set_name_start  #110 (line in Coconut source)
            if _coconut_match_set_name_stop is not _coconut_sentinel:  #110 (line in Coconut source)
                stop = _coconut_match_set_name_stop  #110 (line in Coconut source)
            if _coconut_match_set_name_step is not _coconut_sentinel:  #110 (line in Coconut source)
                step = _coconut_match_set_name_step  #110 (line in Coconut source)
        if _coconut_case_match_check_0:  #110 (line in Coconut source)
            if step != 1:  #111 (line in Coconut source)
                raise ValueError("the scikit-optimize backend only supports a randrange step size of 1")  #112 (line in Coconut source)
            stop -= 1  # scikit-optimize ranges are inclusive  #113 (line in Coconut source)
            return Integer(start, stop, name=name)  #114 (line in Coconut source)
    if not _coconut_case_match_check_0:  #115 (line in Coconut source)
        _coconut_match_set_name_a = _coconut_sentinel  #115 (line in Coconut source)
        _coconut_match_set_name_b = _coconut_sentinel  #115 (line in Coconut source)
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Iterable):  #115 (line in Coconut source)
            _coconut_match_temp_2 = _coconut.tuple(_coconut_case_match_to_0)  #115 (line in Coconut source)
            if (_coconut.len(_coconut_match_temp_2) == 2) and (_coconut_match_temp_2[0] == "uniform") and (_coconut.isinstance(_coconut_match_temp_2[1], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_2[1]) == 2):  #115 (line in Coconut source)
                _coconut_match_set_name_a = _coconut_match_temp_2[1][0]  #115 (line in Coconut source)
                _coconut_match_set_name_b = _coconut_match_temp_2[1][1]  #115 (line in Coconut source)
                _coconut_case_match_check_0 = True  #115 (line in Coconut source)
        if _coconut_case_match_check_0:  #115 (line in Coconut source)
            if _coconut_match_set_name_a is not _coconut_sentinel:  #115 (line in Coconut source)
                a = _coconut_match_set_name_a  #115 (line in Coconut source)
            if _coconut_match_set_name_b is not _coconut_sentinel:  #115 (line in Coconut source)
                b = _coconut_match_set_name_b  #115 (line in Coconut source)
        if _coconut_case_match_check_0:  #115 (line in Coconut source)
            return Real(a, b, name=name)  #116 (line in Coconut source)
    raise TypeError("invalid parameter {_coconut_format_0}".format(_coconut_format_0=(name)))  #117 (line in Coconut source)



def create_dimensions(params):  #120 (line in Coconut source)
    """Construct the full optimization space for the given parameters."""  #121 (line in Coconut source)
    return [create_space(name, func, *args) for name, (func, args, kwargs) in sorted_items(params)]  #122 (line in Coconut source)


# Backend:


class SkoptBackend(StandardBackend):  #130 (line in Coconut source)
    """The scikit-optimize backend uses scikit-optimize for black box optimization."""  #131 (line in Coconut source)
    backend_name = "scikit-optimize"  #132 (line in Coconut source)
    implemented_funcs = ("choice", "randrange", "uniform")  #133 (line in Coconut source)

    @override  #140 (line in Coconut source)
    def setup_backend(self, params, base_estimator="GP", n_initial_points=None, **options):  #141 (line in Coconut source)
        """Special method to initialize the backend from params."""  #142 (line in Coconut source)
        self.params = params  #143 (line in Coconut source)
        if isinstance(base_estimator, str):  #144 (line in Coconut source)
            base_estimator = py_str(base_estimator)  #145 (line in Coconut source)
        if n_initial_points is None:  #146 (line in Coconut source)
            n_initial_points = guess_n_initial_points(params)  #147 (line in Coconut source)
        self.optimizer = Optimizer(create_dimensions(params), base_estimator, n_initial_points=n_initial_points, **options)  #148 (line in Coconut source)


    @override  #155 (line in Coconut source)
    def tell_examples(self, new_examples):  #156 (line in Coconut source)
        """Special method that allows fast updating of the backend with new examples."""  #157 (line in Coconut source)
        data_points, losses = split_examples(new_examples, self.params)  #158 (line in Coconut source)
        self.result = self.optimizer.tell(data_points, losses)  #159 (line in Coconut source)

        current_point = self.optimizer.ask()  #161 (line in Coconut source)
        self.current_values = make_values(self.params, current_point)  #162 (line in Coconut source)


    @property  #164 (line in Coconut source)
    def space(self):  #165 (line in Coconut source)
        """The space over which optimization was performed."""  #166 (line in Coconut source)
        return self.optimizer.space  #167 (line in Coconut source)


    @property  #169 (line in Coconut source)
    def model(self):  #170 (line in Coconut source)
        """Get the most recently fit model."""  #171 (line in Coconut source)
        return self.optimizer.models[-1]  #172 (line in Coconut source)


# Registered names:


_coconut_call_set_names(SkoptBackend)  #177 (line in Coconut source)
SkoptBackend.register()  #177 (line in Coconut source)
SkoptBackend.register_alias("skopt")  #178 (line in Coconut source)

SkoptBackend.register_alg("gaussian_process", base_estimator="GP")  #180 (line in Coconut source)
SkoptBackend.register_alg("random_forest", base_estimator="RF")  #181 (line in Coconut source)
SkoptBackend.register_alg("extra_trees", base_estimator="ET")  #182 (line in Coconut source)
SkoptBackend.register_alg("gradient_boosted_regression_trees", base_estimator="GBRT")  #183 (line in Coconut source)

SkoptBackend.register_meta_for_all_algs("any_skopt")  #185 (line in Coconut source)
