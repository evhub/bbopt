#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xa38196f

# Compiled with Coconut version 2.0.0-a_dev65 [How Not to Be Seen]

"""
Handles standardizing param calls to use standard library random functions.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os as _coconut_os
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
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



if _coconut_sys.version_info >= (3, 3):  #5 (line num in coconut source)
    from collections.abc import Iterable  #5 (line num in coconut source)
else:  #5 (line num in coconut source)
    from collections import Iterable  #5 (line num in coconut source)
from math import pi  #6 (line num in coconut source)
from math import log as ln  #6 (line num in coconut source)

from bbopt import constants  #8 (line num in coconut source)
from bbopt.util import Num  #9 (line num in coconut source)
from bbopt.util import format_err  #9 (line num in coconut source)
from bbopt.util import all_isinstance  #9 (line num in coconut source)
from bbopt.util import denumpy_all  #9 (line num in coconut source)
from bbopt.util import printerr  #9 (line num in coconut source)


# Handlers:

def handle_randrange(args):  #20 (line num in coconut source)
    if not all_isinstance(args, int):  #21 (line num in coconut source)
        raise format_err(ValueError, "arguments to randrange must be integers, not", args)  #22 (line num in coconut source)
    if len(args) == 1:  #23 (line num in coconut source)
        start, stop, step = 0, args[0], 1  #24 (line num in coconut source)
    elif len(args) == 2:  #25 (line num in coconut source)
        start, stop, step = args[0], args[1], 1  #26 (line num in coconut source)
    elif len(args) == 3:  #27 (line num in coconut source)
        start, stop, step = args  #28 (line num in coconut source)
    else:  #29 (line num in coconut source)
        raise format_err(ValueError, "randrange expects between 1 and 3 arguments, not", args)  #30 (line num in coconut source)
    if start > stop:  #31 (line num in coconut source)
        raise format_err(ValueError, "randrange start must be less than stop")  #32 (line num in coconut source)
    return [start, stop, step]  #33 (line num in coconut source)



def handle_choice(args):  #36 (line num in coconut source)
    if len(args) != 1 or not isinstance(args[0], Iterable):  #37 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to choice", args)  #38 (line num in coconut source)
    choices = list(args[0])  #39 (line num in coconut source)
    if not choices:  #40 (line num in coconut source)
        raise format_err(ValueError, "choice requires at least one choice")  #41 (line num in coconut source)
    return (choices,)  #42 (line num in coconut source)



def handle_uniform(args):  #45 (line num in coconut source)
    if len(args) != 2 or not all_isinstance(args, Num):  #46 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to uniform", args)  #47 (line num in coconut source)



def handle_triangular(args):  #50 (line num in coconut source)
    if len(args) != 3 or not all_isinstance(args, Num):  #51 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to triangular", args)  #52 (line num in coconut source)



def handle_betavariate(args):  #55 (line num in coconut source)
    if len(args) != 2 or not all_isinstance(args, Num):  #56 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to betavariate", args)  #57 (line num in coconut source)



def handle_expovariate(args):  #60 (line num in coconut source)
    if len(args) != 1 or not all_isinstance(args, Num):  #61 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to expovariate", args)  #62 (line num in coconut source)



def handle_gammavariate(args):  #65 (line num in coconut source)
    if len(args) != 2 or not all_isinstance(args, Num):  #66 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to gammavariate", args)  #67 (line num in coconut source)



def handle_normalvariate(args):  #70 (line num in coconut source)
    if len(args) != 2 or not all_isinstance(args, Num):  #71 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to normalvariate", args)  #72 (line num in coconut source)



def handle_vonmisesvariate(args):  #75 (line num in coconut source)
    if len(args) != 2 or not all_isinstance(args, Num):  #76 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to vonmisesvariate", args)  #77 (line num in coconut source)



def handle_paretovariate(args):  #80 (line num in coconut source)
    if len(args) != 1 or not all_isinstance(args, Num):  #81 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to paretovariate", args)  #82 (line num in coconut source)



def handle_weibullvariate(args):  #85 (line num in coconut source)
    if len(args) != 2 or not all_isinstance(args, Num):  #86 (line num in coconut source)
        raise format_err(ValueError, "invalid arguments to weibullvariate", args)  #87 (line num in coconut source)


# Placeholders:


def placeholder_randrange(start, stop, step):  #92 (line num in coconut source)
    rng = range(start, stop, step)  #93 (line num in coconut source)
    return rng[len(rng) // 2]  #94 (line num in coconut source)



def placeholder_choice(choices):  #97 (line num in coconut source)
    return choices[len(choices) // 2]  #98 (line num in coconut source)



def placeholder_uniform(start, stop):  #101 (line num in coconut source)
    return (start + stop) / 2  #102 (line num in coconut source)



def placeholder_triangular(low, high, mode):  #105 (line num in coconut source)
    return mode  #106 (line num in coconut source)



def placeholder_betavariate(alpha, beta):  #109 (line num in coconut source)
    return alpha / (alpha + beta)  #110 (line num in coconut source)



def placeholder_expovariate(lambd):  #113 (line num in coconut source)
    return 1 / lambd  #114 (line num in coconut source)



def placeholder_gammavariate(alpha, beta):  #117 (line num in coconut source)
    return alpha / beta  #118 (line num in coconut source)



def placeholder_normalvariate(mu, sigma):  #121 (line num in coconut source)
    return mu  #122 (line num in coconut source)



def placeholder_vonmisesvariate(mu, kappa):  #125 (line num in coconut source)
    return mu  #126 (line num in coconut source)



def placeholder_paretovariate(alpha):  #129 (line num in coconut source)
    return 1 if alpha <= 1 else alpha / (alpha - 1)  #130 (line num in coconut source)



def placeholder_weibullvariate(alpha, beta):  #133 (line num in coconut source)
    return alpha * ln(2)**(1 / beta)  #134 (line num in coconut source)


# Support checkers:



def support_check_randrange(val, start, stop, step):  #140 (line num in coconut source)
    return val in range(start, stop, step)  #141 (line num in coconut source)



def support_check_choice(val, choices):  #144 (line num in coconut source)
    return val in choices  #145 (line num in coconut source)



def support_check_uniform(val, start, stop):  #148 (line num in coconut source)
    return start <= val <= stop or stop <= val <= start  #149 (line num in coconut source)



def support_check_triangular(val, low, high, mode):  #152 (line num in coconut source)
    return low <= val <= high  #153 (line num in coconut source)



def support_check_betavariate(val, alpha, beta):  #156 (line num in coconut source)
    return 0 <= val <= 1  #157 (line num in coconut source)



def support_check_expovariate(val, lambd):  #160 (line num in coconut source)
    return val >= 0 if lambd >= 0 else val <= 0  #161 (line num in coconut source)



def support_check_gammavariate(val, alpha, beta):  #164 (line num in coconut source)
    return val > 0  #165 (line num in coconut source)



def support_check_normalvariate(val, mu, sigma):  #168 (line num in coconut source)
# just check for comparability with mu
    return val >= mu or val < mu  #170 (line num in coconut source)



def support_check_vonmisesvariate(val, mu, kappa):  #173 (line num in coconut source)
    return 0 <= val <= 2 * pi  #174 (line num in coconut source)



def support_check_paretovariate(val, alpha):  #177 (line num in coconut source)
    return val >= 1  #178 (line num in coconut source)



def support_check_weibullvariate(val, alpha, beta):  #181 (line num in coconut source)
    return val >= 0  #182 (line num in coconut source)


# Processor:


class ParamProcessor(_coconut.object):  #187 (line num in coconut source)
    """Processes param keyword arguments."""  #188 (line num in coconut source)

    def __init__(self):  #190 (line num in coconut source)
        self.handlers = {}  #191 (line num in coconut source)
        self.placeholder_funcs = {}  #192 (line num in coconut source)
        self.support_checkers = {}  #193 (line num in coconut source)


    @property  #195 (line num in coconut source)
    def registered_base_rand_funcs(self):  #196 (line num in coconut source)
        return tuple(self.handlers)  #196 (line num in coconut source)


    def register(self, func, handler, placeholder_generator, support_check_func, replace=False):  #198 (line num in coconut source)
        """Register a new parameter definition function. See bbopt.params for examples."""  #199 (line num in coconut source)
        if not replace and func in self.handlers:  #200 (line num in coconut source)
            raise ValueError("cannot register already existing parameter definition function {_coconut_format_0!r}".format(_coconut_format_0=(func)))  #201 (line num in coconut source)
        self.handlers[func] = handler  #202 (line num in coconut source)
        self.placeholder_funcs[func] = placeholder_generator  #203 (line num in coconut source)
        self.support_checkers[func] = support_check_func  #204 (line num in coconut source)


    def in_support(self, name, val, func, *args, **kwargs):  #206 (line num in coconut source)
        if func not in self.support_checkers:  #207 (line num in coconut source)
            raise ValueError("unknown parameter definition function {_coconut_format_0} (register with bbopt.params.param_processor.register)".format(_coconut_format_0=(func)))  #208 (line num in coconut source)
        try:  #209 (line num in coconut source)
            return self.support_checkers[func](val, *args)  #210 (line num in coconut source)
        except TypeError:  #211 (line num in coconut source)
            return False  #212 (line num in coconut source)


    def verify_support(self, name, val, func, *args, **kwargs):  #214 (line num in coconut source)
        if not self.in_support(name, val, func, *args, **kwargs):  #215 (line num in coconut source)
            printerr("BBopt Warning: {_coconut_format_0} not in support of {_coconut_format_1}(*{_coconut_format_2}) for parameter {_coconut_format_3} (adjust parameter definition to ensure support is always maximally broad)".format(_coconut_format_0=(val), _coconut_format_1=(func), _coconut_format_2=(args), _coconut_format_3=(name)))  #216 (line num in coconut source)
            if constants.use_placeholder_when_outside_support:  #217 (line num in coconut source)
                val = kwargs.get("placeholder_when_missing", self.choose_default_placeholder(name, func, *args, **kwargs))  #218 (line num in coconut source)
        return val  #219 (line num in coconut source)


    def modify_kwargs(self, func, kwargs):  #221 (line num in coconut source)
        """Apply func to all kwargs with values in the random function's domain."""  #222 (line num in coconut source)
        new_kwargs = {}  #223 (line num in coconut source)
        for k, v in kwargs.items():  #224 (line num in coconut source)
            if k in self.handlers:  #225 (line num in coconut source)
                new_kwargs[k] = map(func, v)  #226 (line num in coconut source)
            else:  #227 (line num in coconut source)
                new_kwargs[k] = func(v)  #228 (line num in coconut source)
        return new_kwargs  #229 (line num in coconut source)


    def standardize_args(self, func, args):  #231 (line num in coconut source)
        """Standardize param func and args."""  #232 (line num in coconut source)
# denumpy args
        args = denumpy_all(args)  #234 (line num in coconut source)

# detect invalid funcs
        if func not in self.handlers:  #237 (line num in coconut source)
            raise ValueError("unknown parameter definition function {_coconut_format_0} (register with bbopt.params.param_processor.register)".format(_coconut_format_0=(func)))  #238 (line num in coconut source)

# run handler
        result = self.handlers[func](args)  #241 (line num in coconut source)
        args = result if result is not None else args  #242 (line num in coconut source)

# standardize arguments to a list
        return list(args)  #245 (line num in coconut source)


    def standardize_kwargs(self, kwargs):  #247 (line num in coconut source)
        """Standardizes param keyword args."""  #248 (line num in coconut source)
        @_coconut_mark_as_match  #249 (line num in coconut source)
        def _coconut_lambda_0(*_coconut_match_args, **_coconut_match_kwargs):  #249 (line num in coconut source)
            _coconut_match_check_0 = False  #249 (line num in coconut source)
            _coconut_match_set_name_k = _coconut_sentinel  #249 (line num in coconut source)
            _coconut_match_set_name_v = _coconut_sentinel  #249 (line num in coconut source)
            _coconut_FunctionMatchError = _coconut_get_function_match_error()  #249 (line num in coconut source)
            if _coconut.len(_coconut_match_args) == 1:  #249 (line num in coconut source)
                if (_coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_args[0]) == 2):  #249 (line num in coconut source)
                    _coconut_match_set_name_k = _coconut_match_args[0][0]  #249 (line num in coconut source)
                    _coconut_match_set_name_v = _coconut_match_args[0][1]  #249 (line num in coconut source)
                    if not _coconut_match_kwargs:  #249 (line num in coconut source)
                        _coconut_match_check_0 = True  #249 (line num in coconut source)
            if _coconut_match_check_0:  #249 (line num in coconut source)
                if _coconut_match_set_name_k is not _coconut_sentinel:  #249 (line num in coconut source)
                    k = _coconut_match_set_name_k  #249 (line num in coconut source)
                if _coconut_match_set_name_v is not _coconut_sentinel:  #249 (line num in coconut source)
                    v = _coconut_match_set_name_v  #249 (line num in coconut source)
            if not _coconut_match_check_0:  #249 (line num in coconut source)
                raise _coconut_FunctionMatchError('return kwargs |> fmap$(def ((k, v)) -> denumpy_all((k, v)))', _coconut_match_args)  #249 (line num in coconut source)
            return denumpy_all((k, v))  #249 (line num in coconut source)
        return (fmap)(_coconut_lambda_0, kwargs)  #249 (line num in coconut source)


    def choose_default_placeholder(self, name, func, *args, **kwargs):  #251 (line num in coconut source)
        """Choose a default placeholder_when_missing value for the given parameter."""  #252 (line num in coconut source)
        if func not in self.placeholder_funcs:  #253 (line num in coconut source)
            raise ValueError("unknown parameter definition function {_coconut_format_0} (register with bbopt.params.param_processor.register)".format(_coconut_format_0=(func)))  #254 (line num in coconut source)
        return self.placeholder_funcs[func](*args)  #255 (line num in coconut source)


# Register base random functions:


_coconut_call_set_names(ParamProcessor)  #260 (line num in coconut source)
param_processor = ParamProcessor()  #260 (line num in coconut source)

param_processor.register("randrange", handle_randrange, placeholder_randrange, support_check_randrange)  #262 (line num in coconut source)
param_processor.register("choice", handle_choice, placeholder_choice, support_check_choice)  #263 (line num in coconut source)
param_processor.register("uniform", handle_uniform, placeholder_uniform, support_check_uniform)  #264 (line num in coconut source)
param_processor.register("triangular", handle_triangular, placeholder_triangular, support_check_triangular)  #265 (line num in coconut source)
param_processor.register("betavariate", handle_betavariate, placeholder_betavariate, support_check_betavariate)  #266 (line num in coconut source)
param_processor.register("expovariate", handle_expovariate, placeholder_expovariate, support_check_expovariate)  #267 (line num in coconut source)
param_processor.register("gammavariate", handle_gammavariate, placeholder_gammavariate, support_check_gammavariate)  #268 (line num in coconut source)
param_processor.register("normalvariate", handle_normalvariate, placeholder_normalvariate, support_check_normalvariate)  #269 (line num in coconut source)
param_processor.register("vonmisesvariate", handle_vonmisesvariate, placeholder_vonmisesvariate, support_check_vonmisesvariate)  #270 (line num in coconut source)
param_processor.register("paretovariate", handle_paretovariate, placeholder_paretovariate, support_check_paretovariate)  #271 (line num in coconut source)
param_processor.register("weibullvariate", handle_weibullvariate, placeholder_weibullvariate, support_check_weibullvariate)  #272 (line num in coconut source)
