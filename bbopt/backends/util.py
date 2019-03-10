#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x36af53be

# Compiled with Coconut version 1.4.0-post_dev23 [Ernest Scribbler]

"""
Utilities for use in BBopt backends.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.dirname(_coconut_os_path.abspath(__file__)))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_back_pipe, _coconut_star_pipe, _coconut_back_star_pipe, _coconut_dubstar_pipe, _coconut_back_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
from __coconut__ import *
if _coconut_sys.version_info >= (3,):
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



from bbopt.params import param_processor
from bbopt.util import sorted_items


def negate_objective(objective):
    if isinstance(objective, list):
        return (list)(map(negate_objective, objective))
    else:
        return -objective


def make_features(values, params, fallback_func=param_processor.choose_default_placeholder, converters={}, convert_fallback=True,):
    """Return an iterator of the values for the parameters in sorted order with the given fallback function.
    If passed, converters must map funcs to functions from (value, *args) -> new_value which will be run
    on the resulting value for that func (but only on fallbacks if convert_fallback)."""
    for name, (func, args, kwargs) in sorted_items(params):
# determine feature
        fallback = False
        _coconut_match_to = values
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                feature = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            pass
        else:
            _coconut_match_to = kwargs
            _coconut_match_check = False
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get("placeholder_when_missing", _coconut_sentinel)
                if _coconut_match_temp_0 is not _coconut_sentinel:
                    placeholder_value = _coconut_match_temp_0
                    _coconut_match_check = True
            if _coconut_match_check:
                feature = placeholder_value
            else:
                fallback = True
                feature = fallback_func(name, func, *args, **kwargs)

# run converters
        if not fallback or convert_fallback:
            _coconut_match_to = converters
            _coconut_match_check = False
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get(func, _coconut_sentinel)
                if _coconut_match_temp_0 is not _coconut_sentinel:
                    converter_func = _coconut_match_temp_0
                    _coconut_match_check = True
            if _coconut_match_check:
                feature = converter_func(feature, *args)

        yield feature


def split_examples(examples, params, fallback_func=param_processor.choose_default_placeholder, converters={}, convert_fallback=True,):
    """Split examples into a list of data points and a list of losses with the given fallback function."""
    data_points, losses = [], []
    for example in examples:

# extract values, loss
        _coconut_match_to = example
        _coconut_case_check_0 = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
            _coconut_match_temp_1 = _coconut_match_to.get("gain", _coconut_sentinel)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                values = _coconut_match_temp_0
                gain = _coconut_match_temp_1
                _coconut_case_check_0 = True
        if _coconut_case_check_0:
            loss = negate_objective(gain)
        if not _coconut_case_check_0:
            if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to.get("values", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_match_to.get("loss", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    values = _coconut_match_temp_0
                    loss = _coconut_match_temp_1
                    _coconut_case_check_0 = True
            if _coconut_case_check_0:
                pass
        if not _coconut_case_check_0:
            raise ValueError("invalid example {}".format(example))

# extract features
        features = (list)(make_features(values, params, fallback_func, converters, convert_fallback))

# add to data_points, losses
        (data_points.append)(features)
        (losses.append)(loss)

    return data_points, losses


def make_values(params, point):
    """Return a dictionary with the values replaced by the values in point,
    where point is a list of the values corresponding to the sorted params."""
    values = {}
    for i, k in (enumerate)((sorted)(params)):
        values[k] = point[i]
    return values


def serve_values(name, func, args, kwargs, serving_values, fallback_func, backend_name=None, implemented_funcs=None, supported_kwargs=None,):
    """Determines the parameter value to serve for the given parameter
    name and kwargs. First checks for unsupported funcs or kwargs, then
    uses the following algorithm:
    1. if name in serving_values, use serving_values[name], else
    2. if guess in kwargs, use the guess, else
    3. call fallback_func(name, func, *args, **kwargs)."""
# validate arguments
    if implemented_funcs is not None:
        assert backend_name is not None, "serve_values expects a backend_name argument when doing func validation"
        if func not in implemented_funcs:
            raise ValueError("the {_coconut_format_0} backend does not implement the {_coconut_format_1} function".format(_coconut_format_0=(backend_name), _coconut_format_1=(func)))
    if supported_kwargs is not None:
        assert backend_name is not None, "serve_values expects a backend_name argument when doing kwargs validation"
        unsupported_kwargs = set(kwargs) - set(supported_kwargs)
        if unsupported_kwargs:
            raise ValueError("the {_coconut_format_0} backend does not support {_coconut_format_1} option(s)".format(_coconut_format_0=(backend_name), _coconut_format_1=(unsupported_kwargs)))

# determine value
    _coconut_match_to = serving_values
    _coconut_match_check = False
    if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
        _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
        if _coconut_match_temp_0 is not _coconut_sentinel:
            value = _coconut_match_temp_0
            _coconut_match_check = True
    if _coconut_match_check:
        return value
    else:
        _coconut_match_to = kwargs
        _coconut_match_check = False
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get("guess", _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                guess = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            return guess
        else:
            return fallback_func(name, func, *args, **kwargs)
