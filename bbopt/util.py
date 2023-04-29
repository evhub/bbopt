#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xfb7706c7

# Compiled with Coconut version 3.0.0-a_dev36

"""
Utilities for use across all of bbopt.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys
_coconut_header_info = ('3.0.0-a_dev36', '', True)
import os as _coconut_os
_coconut_cached__coconut__ = _coconut_sys.modules.get(str('__coconut__'))
_coconut_file_dir = _coconut_os.path.dirname(_coconut_os.path.abspath(__file__))
_coconut_pop_path = False
if _coconut_cached__coconut__ is None or getattr(_coconut_cached__coconut__, "_coconut_header_info", None) != _coconut_header_info and _coconut_os.path.dirname(_coconut_cached__coconut__.__file__ or "") != _coconut_file_dir:
    if _coconut_cached__coconut__ is not None:
        _coconut_sys.modules[str('_coconut_cached__coconut__')] = _coconut_cached__coconut__
        del _coconut_sys.modules[str('__coconut__')]
    _coconut_sys.path.insert(0, _coconut_file_dir)
    _coconut_pop_path = True
    _coconut_module_name = _coconut_os.path.splitext(_coconut_os.path.basename(_coconut_file_dir))[0]
    if _coconut_module_name and _coconut_module_name[0].isalpha() and all(c.isalpha() or c.isdigit() for c in _coconut_module_name) and "__init__.py" in _coconut_os.listdir(_coconut_file_dir):
        _coconut_full_module_name = str(_coconut_module_name + ".__coconut__")
        import __coconut__ as _coconut__coconut__
        _coconut__coconut__.__name__ = _coconut_full_module_name
        for _coconut_v in vars(_coconut__coconut__).values():
            if getattr(_coconut_v, "__module__", None) == str('__coconut__'):
                try:
                    _coconut_v.__module__ = _coconut_full_module_name
                except AttributeError:
                    _coconut_v_type = type(_coconut_v)
                    if getattr(_coconut_v_type, "__module__", None) == str('__coconut__'):
                        _coconut_v_type.__module__ = _coconut_full_module_name
        _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_Expected, _coconut_MatchError, _coconut_SupportsAdd, _coconut_SupportsMinus, _coconut_SupportsMul, _coconut_SupportsPow, _coconut_SupportsTruediv, _coconut_SupportsFloordiv, _coconut_SupportsMod, _coconut_SupportsAnd, _coconut_SupportsXor, _coconut_SupportsOr, _coconut_SupportsLshift, _coconut_SupportsRshift, _coconut_SupportsMatmul, _coconut_SupportsInv, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple, _coconut_matmul, _coconut_py_str, _coconut_flatten, _coconut_multiset, _coconut_back_none_pipe, _coconut_back_none_star_pipe, _coconut_back_none_dubstar_pipe, _coconut_forward_none_compose, _coconut_back_none_compose, _coconut_forward_none_star_compose, _coconut_back_none_star_compose, _coconut_forward_none_dubstar_compose, _coconut_back_none_dubstar_compose, _coconut_call_or_coefficient, _coconut_in, _coconut_not_in
if _coconut_pop_path:
    _coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import os  #5 (line in Coconut source)
sys = _coconut_sys  #6 (line in Coconut source)
try:  #7 (line in Coconut source)
    _coconut_sys_0 = sys  # type: ignore  #7 (line in Coconut source)
except _coconut.NameError:  #7 (line in Coconut source)
    _coconut_sys_0 = _coconut_sentinel  #7 (line in Coconut source)
sys = _coconut_sys  #7 (line in Coconut source)
if sys.version_info >= (3, 3):  #7 (line in Coconut source)
    from collections.abc import Mapping  #7 (line in Coconut source)
else:  #7 (line in Coconut source)
    from collections import Mapping  #7 (line in Coconut source)
if _coconut_sys_0 is not _coconut_sentinel:  #7 (line in Coconut source)
    sys = _coconut_sys_0  #7 (line in Coconut source)
try:  #7 (line in Coconut source)
    _coconut_sys_1 = sys  # type: ignore  #7 (line in Coconut source)
except _coconut.NameError:  #7 (line in Coconut source)
    _coconut_sys_1 = _coconut_sentinel  #7 (line in Coconut source)
sys = _coconut_sys  #7 (line in Coconut source)
if sys.version_info >= (3, 3):  #7 (line in Coconut source)
    from collections.abc import Iterable  #7 (line in Coconut source)
else:  #7 (line in Coconut source)
    from collections import Iterable  #7 (line in Coconut source)
if _coconut_sys_1 is not _coconut_sentinel:  #7 (line in Coconut source)
    sys = _coconut_sys_1  #7 (line in Coconut source)
from contextlib import contextmanager  #8 (line in Coconut source)
from functools import wraps  #9 (line in Coconut source)

import numpy as np  #11 (line in Coconut source)
from portalocker import Lock  #12 (line in Coconut source)

from bbopt import constants  #14 (line in Coconut source)


Num = (int, float)  #17 (line in Coconut source)
Str = (str, py_str)  #18 (line in Coconut source)


def norm_path(path):  #21 (line in Coconut source)
    """Normalize the given path."""  #22 (line in Coconut source)
    return ((os.path.normcase)((os.path.realpath)((os.path.abspath)((os.path.expanduser)(path)))))  #23 (line in Coconut source)



def isnumpy(obj):  #30 (line in Coconut source)
    """Determines if obj is a numpy scalar."""  #31 (line in Coconut source)
    return type(obj).__module__ == "numpy" and np.isscalar(obj)  #32 (line in Coconut source)



def denumpy(obj, fallback=None):  #35 (line in Coconut source)
    """Convert numpy data types to their Python equivalents."""  #36 (line in Coconut source)
# the ordering here is extremely important; float must
#  come before int and int must come before bool
    if np.issubdtype(obj, np.complexfloating):  #39 (line in Coconut source)
        return complex(obj)  #40 (line in Coconut source)
    if np.issubdtype(obj, np.floating):  #41 (line in Coconut source)
        return float(obj)  #42 (line in Coconut source)
    if np.issubdtype(obj, np.signedinteger) or np.issubdtype(obj, np.unsignedinteger):  #43 (line in Coconut source)
        return int(obj)  #44 (line in Coconut source)
    if np.issubdtype(obj, np.bool_):  #45 (line in Coconut source)
        return bool(obj)  #46 (line in Coconut source)
    if np.issubdtype(obj, np.str_) or np.issubdtype(obj, np.unicode_):  #47 (line in Coconut source)
        return str(obj)  #48 (line in Coconut source)
    if fallback is not None:  #49 (line in Coconut source)
        fallback()  #50 (line in Coconut source)
    return obj  #51 (line in Coconut source)



def denumpy_all(obj):  #54 (line in Coconut source)
    """Recursively apply denumpy to the given obj."""  #55 (line in Coconut source)
    if isinstance(obj, (list, tuple)):  #56 (line in Coconut source)
        return (fmap)(denumpy_all, obj)  #57 (line in Coconut source)
    elif isinstance(obj, dict):  #58 (line in Coconut source)
        return _coconut.dict(((denumpy_all(k)), (denumpy_all(v))) for k, v in obj.items())  #59 (line in Coconut source)
    elif isnumpy(obj):  #63 (line in Coconut source)
        return denumpy(obj)  #64 (line in Coconut source)
    else:  #65 (line in Coconut source)
        return obj  #66 (line in Coconut source)



def json_serialize(obj):  #69 (line in Coconut source)
    """Serialize obj for encoding in JSON."""  #70 (line in Coconut source)
    if obj is None or isinstance(obj, (int, float, bool, str)):  #71 (line in Coconut source)
        return obj  #72 (line in Coconut source)
    if isinstance(obj, bytes):  #73 (line in Coconut source)
        return str(obj, encoding="utf-8")  #74 (line in Coconut source)
    if isinstance(obj, Mapping):  #75 (line in Coconut source)
        serialized_dict = _coconut.dict()  #76 (line in Coconut source)
        for k, v in obj.items():  #77 (line in Coconut source)
            serialized_k = json_serialize(k)  #78 (line in Coconut source)
            if not isinstance(serialized_k, str):  #79 (line in Coconut source)
                raise TypeError("dict keys must be strings, not {_coconut_format_0}".format(_coconut_format_0=(k)))  #80 (line in Coconut source)
            serialized_dict[k] = json_serialize(v)  #81 (line in Coconut source)
        return serialized_dict  #82 (line in Coconut source)
    if isinstance(obj, Iterable):  #83 (line in Coconut source)
        serialized_list = []  #84 (line in Coconut source)
        for x in obj:  #85 (line in Coconut source)
            serialized_list.append(json_serialize(x))  #86 (line in Coconut source)
        return serialized_list  #87 (line in Coconut source)
    if isnumpy(obj):  #88 (line in Coconut source)
        def _coconut_lambda_0(_=None):  #89 (line in Coconut source)
            raise TypeError("cannot JSON serialize numpy dtype {_coconut_format_0}".format(_coconut_format_0=(obj.dtype)))  #89 (line in Coconut source)

        return denumpy(obj, fallback=(_coconut_lambda_0))  #89 (line in Coconut source)
    raise TypeError("cannot JSON serialize {_coconut_format_0}".format(_coconut_format_0=(obj)))  #90 (line in Coconut source)



def sorted_items(params):  #93 (line in Coconut source)
    """Return an iterator of the dict's items sorted by its keys."""  #94 (line in Coconut source)
    return sorted(params.items())  #95 (line in Coconut source)



def sorted_examples(examples):  #98 (line in Coconut source)
    """Sort examples by their timestamp."""  #99 (line in Coconut source)
    return sorted(examples, key=_coconut.operator.itemgetter(("timestamp")))  #100 (line in Coconut source)



def running_best(examples):  #103 (line in Coconut source)
    """Yield running best examples seen at each point."""  #104 (line in Coconut source)
    best_example = max_gain = min_loss = None  #105 (line in Coconut source)
    for example in examples:  #106 (line in Coconut source)

        _coconut_case_match_to_0 = example  #108 (line in Coconut source)
        _coconut_case_match_check_0 = False  #108 (line in Coconut source)
        _coconut_match_set_name_values = _coconut_sentinel  #108 (line in Coconut source)
        _coconut_match_set_name_gain = _coconut_sentinel  #108 (line in Coconut source)
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):  #108 (line in Coconut source)
            _coconut_match_temp_0 = _coconut_case_match_to_0.get("values", _coconut_sentinel)  #108 (line in Coconut source)
            _coconut_match_temp_1 = _coconut_case_match_to_0.get("gain", _coconut_sentinel)  #108 (line in Coconut source)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):  #108 (line in Coconut source)
                _coconut_match_set_name_values = _coconut_match_temp_0  #108 (line in Coconut source)
                _coconut_match_set_name_gain = _coconut_match_temp_1  #108 (line in Coconut source)
                _coconut_case_match_check_0 = True  #108 (line in Coconut source)
        if _coconut_case_match_check_0:  #108 (line in Coconut source)
            if _coconut_match_set_name_values is not _coconut_sentinel:  #108 (line in Coconut source)
                values = _coconut_match_set_name_values  #108 (line in Coconut source)
            if _coconut_match_set_name_gain is not _coconut_sentinel:  #108 (line in Coconut source)
                gain = _coconut_match_set_name_gain  #108 (line in Coconut source)
        if _coconut_case_match_check_0:  #108 (line in Coconut source)
            if min_loss is not None:  #110 (line in Coconut source)
                raise ValueError("cannot have examples with maximize and examples with minimize")  #111 (line in Coconut source)
            if max_gain is None or gain >= max_gain:  #112 (line in Coconut source)
                best_example = example  #113 (line in Coconut source)
                max_gain = gain  #114 (line in Coconut source)

        if not _coconut_case_match_check_0:  #116 (line in Coconut source)
            _coconut_match_set_name_values = _coconut_sentinel  #116 (line in Coconut source)
            _coconut_match_set_name_loss = _coconut_sentinel  #116 (line in Coconut source)
            if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):  #116 (line in Coconut source)
                _coconut_match_temp_2 = _coconut_case_match_to_0.get("values", _coconut_sentinel)  #116 (line in Coconut source)
                _coconut_match_temp_3 = _coconut_case_match_to_0.get("loss", _coconut_sentinel)  #116 (line in Coconut source)
                if (_coconut_match_temp_2 is not _coconut_sentinel) and (_coconut_match_temp_3 is not _coconut_sentinel):  #116 (line in Coconut source)
                    _coconut_match_set_name_values = _coconut_match_temp_2  #116 (line in Coconut source)
                    _coconut_match_set_name_loss = _coconut_match_temp_3  #116 (line in Coconut source)
                    _coconut_case_match_check_0 = True  #116 (line in Coconut source)
            if _coconut_case_match_check_0:  #116 (line in Coconut source)
                if _coconut_match_set_name_values is not _coconut_sentinel:  #116 (line in Coconut source)
                    values = _coconut_match_set_name_values  #116 (line in Coconut source)
                if _coconut_match_set_name_loss is not _coconut_sentinel:  #116 (line in Coconut source)
                    loss = _coconut_match_set_name_loss  #116 (line in Coconut source)
            if _coconut_case_match_check_0:  #116 (line in Coconut source)
                if max_gain is not None:  #117 (line in Coconut source)
                    raise ValueError("cannot have examples with maximize and examples with minimize")  #118 (line in Coconut source)
                if min_loss is None or loss <= min_loss:  #119 (line in Coconut source)
                    best_example = example  #120 (line in Coconut source)
                    min_loss = loss  #121 (line in Coconut source)

        if not _coconut_case_match_check_0:  #123 (line in Coconut source)
            raise ValueError("invalid example {_coconut_format_0}".format(_coconut_format_0=(example)))  #124 (line in Coconut source)

        yield best_example  #126 (line in Coconut source)



def best_example(examples):  #129 (line in Coconut source)
    """Return the best example seen so far."""  #130 (line in Coconut source)
    best = consume(running_best(examples), keep_last=1)  #131 (line in Coconut source)
    if best:  #132 (line in Coconut source)
        assert len(best) == 1, "{_coconut_format_0} != 1".format(_coconut_format_0=(len(best)))  #133 (line in Coconut source)
        return best[0]  #134 (line in Coconut source)
    else:  #135 (line in Coconut source)
        return _coconut.dict((("values", _coconut.dict()),))  #136 (line in Coconut source)



def all_isinstance(objs, types):  #139 (line in Coconut source)
    """Return whether all the objects have the desired type(s)."""  #140 (line in Coconut source)
    return (all)((map)(_coconut_partial(isinstance, {1: types}, 2, ()), objs))  #141 (line in Coconut source)



def format_err(Error, message, obj):  #144 (line in Coconut source)
    """Creates an error with a formatted error message."""  #145 (line in Coconut source)
    return Error(message + ": " + repr(obj))  #146 (line in Coconut source)



def sync_file(file_handle):  #149 (line in Coconut source)
    """Forcibly flush and sync the given file."""  #150 (line in Coconut source)
    file_handle.flush()  #151 (line in Coconut source)
    os.fsync(file_handle.fileno())  #152 (line in Coconut source)



def ensure_file(fpath):  #155 (line in Coconut source)
    """Ensure that the given file exists."""  #156 (line in Coconut source)
    if sys.version_info >= (3,):  #157 (line in Coconut source)
        try:  #158 (line in Coconut source)
            with open(fpath, "x"):  #159 (line in Coconut source)
                pass  #160 (line in Coconut source)
        except FileExistsError:  #161 (line in Coconut source)
            pass  #162 (line in Coconut source)
    else:  #163 (line in Coconut source)
        with open(fpath, "a"):  #164 (line in Coconut source)
            pass  #165 (line in Coconut source)



def clear_file(file_handle):  #168 (line in Coconut source)
    """Empties the contents of the given file."""  #169 (line in Coconut source)
    file_handle.seek(0)  #170 (line in Coconut source)
    file_handle.truncate()  #171 (line in Coconut source)



def plot(xs, ys, ax=None, yscale=None, title=None, label=None, xlabel=None, ylabel=None, marker=".", markersize=12, linewidth=2, grid=True,):  #174 (line in Coconut source)
    """Construct a matplotlib plot with the given parameters."""  #188 (line in Coconut source)
    if ax is None:  #189 (line in Coconut source)
        from matplotlib import pyplot as plt  #190 (line in Coconut source)
        ax = plt.gca()  #191 (line in Coconut source)
    if title is not None:  #192 (line in Coconut source)
        ax.set_title(title)  #193 (line in Coconut source)
    if xlabel is not None:  #194 (line in Coconut source)
        ax.set_xlabel(xlabel)  #195 (line in Coconut source)
    if ylabel is not None:  #196 (line in Coconut source)
        ax.set_ylabel(ylabel)  #197 (line in Coconut source)
    if grid:  #198 (line in Coconut source)
        ax.grid()  #199 (line in Coconut source)
    if yscale is not None:  #200 (line in Coconut source)
        ax.set_yscale(yscale)  #201 (line in Coconut source)
    ax.plot(xs, ys, label=label, marker=marker, markersize=markersize, linewidth=linewidth)  #202 (line in Coconut source)
    return ax  #203 (line in Coconut source)



@contextmanager  #206 (line in Coconut source)
def open_with_lock(fpath, mode="rb+", timeout=None, **kwargs):  #207 (line in Coconut source)
    """Open file with lock."""  #208 (line in Coconut source)
    if timeout is None:  #209 (line in Coconut source)
        timeout = constants.lock_timeout  #210 (line in Coconut source)
    with Lock(fpath, mode, timeout=timeout, **kwargs) as file_handle:  #211 (line in Coconut source)
        try:  #212 (line in Coconut source)
            yield file_handle  #213 (line in Coconut source)
        finally:  #214 (line in Coconut source)
            file_handle.flush()  #215 (line in Coconut source)
            if "w" in mode or "+" in mode or "a" in mode:  #216 (line in Coconut source)
                try:  #217 (line in Coconut source)
                    os.fsync(file_handle.fileno())  #218 (line in Coconut source)
                except OSError:  #219 (line in Coconut source)
                    pass  #220 (line in Coconut source)



def convert_match_errors(func):  #223 (line in Coconut source)
    """Re-raise MatchErrors as TypeErrors."""  #224 (line in Coconut source)
    @wraps(func)  #225 (line in Coconut source)
    def match_errors_converted_func(*args, **kwargs):  #226 (line in Coconut source)
        try:  #227 (line in Coconut source)
            return func(*args, **kwargs)  #228 (line in Coconut source)
        except MatchError as err:  #229 (line in Coconut source)
            func_name = getattr(func, "__qualname__", func.__name__)  #230 (line in Coconut source)
            _coconut_raise_from_0 = TypeError("arguments did not match call signature for function {_coconut_format_0}".format(_coconut_format_0=(func_name)))  #231 (line in Coconut source)
            _coconut_raise_from_0.__cause__ = err  #231 (line in Coconut source)
            raise _coconut_raise_from_0  #231 (line in Coconut source)

    return match_errors_converted_func  #232 (line in Coconut source)



def printerr(*args):  #235 (line in Coconut source)
    """Print to stderr."""  #236 (line in Coconut source)
    print(*args, file=sys.stderr)  #237 (line in Coconut source)



class ListProxy(_coconut.object):  #240 (line in Coconut source)
    """Behaves like new_list, but appends new elements to old_list."""  #241 (line in Coconut source)

    def __init__(self, old_list, new_list):  #243 (line in Coconut source)
        self.old_list = old_list  #244 (line in Coconut source)
        self.new_list = new_list  #245 (line in Coconut source)


    def __iter__(self):  #247 (line in Coconut source)
        _coconut_yield_from_1 = _coconut.iter(self.new_list)  #248 (line in Coconut source)
        while True:  #248 (line in Coconut source)
            try:  #248 (line in Coconut source)
                yield _coconut.next(_coconut_yield_from_1)  #248 (line in Coconut source)
            except _coconut.StopIteration as _coconut_yield_err_0:  #248 (line in Coconut source)
                _coconut_yield_from_0 = _coconut_yield_err_0.args[0] if _coconut.len(_coconut_yield_err_0.args) > 0 else None  #248 (line in Coconut source)
                break  #248 (line in Coconut source)
        _coconut_yield_from_0  #248 (line in Coconut source)


    def __getitem__(self, index):  #250 (line in Coconut source)
        return self.new_list[index]  #251 (line in Coconut source)


    def append(self, obj):  #253 (line in Coconut source)
        self.new_list.append(obj)  #254 (line in Coconut source)
        if obj not in self.old_list:  #255 (line in Coconut source)
            self.old_list.append(obj)  #256 (line in Coconut source)


    def __setitem__(self, index, obj):  #258 (line in Coconut source)
        self.new_list[index] = obj  #259 (line in Coconut source)
        if obj not in self.old_list:  #260 (line in Coconut source)
            self.old_list.append(obj)  #261 (line in Coconut source)


    def __repr__(self):  #263 (line in Coconut source)
        return "ListProxy(\n\tself.old_list={_coconut_format_0},\n\tself.new_list={_coconut_format_1},\n)".format(_coconut_format_0=(self.old_list), _coconut_format_1=(self.new_list))  #264 (line in Coconut source)



_coconut_call_set_names(ListProxy)  #267 (line in Coconut source)
class DictProxy(_coconut.object):  #267 (line in Coconut source)
    """Behaves like new_dict, but adds new keys to old_dict."""  #268 (line in Coconut source)

    def __init__(self, old_dict, new_dict):  #270 (line in Coconut source)
        self.old_dict = old_dict  #271 (line in Coconut source)
        self.new_dict = new_dict  #272 (line in Coconut source)


    def __iter__(self):  #274 (line in Coconut source)
        _coconut_yield_from_3 = _coconut.iter(self.new_dict)  #275 (line in Coconut source)
        while True:  #275 (line in Coconut source)
            try:  #275 (line in Coconut source)
                yield _coconut.next(_coconut_yield_from_3)  #275 (line in Coconut source)
            except _coconut.StopIteration as _coconut_yield_err_1:  #275 (line in Coconut source)
                _coconut_yield_from_2 = _coconut_yield_err_1.args[0] if _coconut.len(_coconut_yield_err_1.args) > 0 else None  #275 (line in Coconut source)
                break  #275 (line in Coconut source)
        _coconut_yield_from_2  #275 (line in Coconut source)


    def items(self):  #277 (line in Coconut source)
        return self.new_dict.items()  #278 (line in Coconut source)


    def keys(self):  #280 (line in Coconut source)
        return self.new_dict.keys()  #281 (line in Coconut source)


    def values(self):  #283 (line in Coconut source)
        return self.new_dict.values()  #284 (line in Coconut source)


    def __getitem__(self, key):  #286 (line in Coconut source)
        value = self.new_dict[key]  #287 (line in Coconut source)
        if key not in self.old_dict:  #288 (line in Coconut source)
            self.old_dict[key] = value  #289 (line in Coconut source)
        return value  #290 (line in Coconut source)


    def __setitem__(self, key, value):  #292 (line in Coconut source)
        self.new_dict[key] = value  #293 (line in Coconut source)
        if key not in self.old_dict:  #294 (line in Coconut source)
            self.old_dict[key] = value  #295 (line in Coconut source)


    def __repr__(self):  #297 (line in Coconut source)
        return "DictProxy(\n\tself.old_dict={_coconut_format_0},\n\tself.new_dict={_coconut_format_1},\n)".format(_coconut_format_0=(self.old_dict), _coconut_format_1=(self.new_dict))  #298 (line in Coconut source)



_coconut_call_set_names(DictProxy)  #301 (line in Coconut source)
@_coconut_mark_as_match  #301 (line in Coconut source)
def mean(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #301 (line in Coconut source)
    _coconut_match_check_0 = False  #301 (line in Coconut source)
    _coconut_match_set_name_xs = _coconut_sentinel  #301 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #301 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #301 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #301 (line in Coconut source)
    if _coconut.len(_coconut_match_args) == 1:  #301 (line in Coconut source)
        if _coconut.isinstance(_coconut_match_args[0], _coconut.abc.Sequence):  #301 (line in Coconut source)
            _coconut_match_temp_4 = _coconut.list(_coconut_match_args[0])  #301 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_temp_4  #301 (line in Coconut source)
            if not _coconut_match_kwargs:  #301 (line in Coconut source)
                _coconut_match_check_0 = True  #301 (line in Coconut source)
    if _coconut_match_check_0:  #301 (line in Coconut source)
        if _coconut_match_set_name_xs is not _coconut_sentinel:  #301 (line in Coconut source)
            xs = _coconut_match_set_name_xs  #301 (line in Coconut source)
    if not _coconut_match_check_0:  #301 (line in Coconut source)
        raise _coconut_FunctionMatchError('match def mean([] + xs) =', _coconut_match_args)  #301 (line in Coconut source)

    return sum(xs) / len(xs)  #302 (line in Coconut source)


try:  #304 (line in Coconut source)
    _coconut_addpattern_0 = _coconut_addpattern(mean)  # type: ignore  #304 (line in Coconut source)
except _coconut.NameError:  #304 (line in Coconut source)
    _coconut_addpattern_0 = lambda f: f  #304 (line in Coconut source)
@_coconut_addpattern_0  #304 (line in Coconut source)
@_coconut_mark_as_match  #304 (line in Coconut source)
def mean(_coconut_match_first_arg=_coconut_sentinel, *_coconut_match_args, **_coconut_match_kwargs):  #304 (line in Coconut source)
    """Compute the arithmetic mean of the given sequence."""  #305 (line in Coconut source)
    _coconut_match_check_1 = False  #306 (line in Coconut source)
    _coconut_match_set_name_xs = _coconut_sentinel  #306 (line in Coconut source)
    _coconut_FunctionMatchError = _coconut_get_function_match_error()  #306 (line in Coconut source)
    if _coconut_match_first_arg is not _coconut_sentinel:  #306 (line in Coconut source)
        _coconut_match_args = (_coconut_match_first_arg,) + _coconut_match_args  #306 (line in Coconut source)
    if _coconut.len(_coconut_match_args) == 1:  #306 (line in Coconut source)
        if _coconut.isinstance(_coconut_match_args[0], _coconut.abc.Iterable):  #306 (line in Coconut source)
            _coconut_match_set_name_xs = _coconut_match_args[0]  #306 (line in Coconut source)
            if not _coconut_match_kwargs:  #306 (line in Coconut source)
                _coconut_match_check_1 = True  #306 (line in Coconut source)
    if _coconut_match_check_1:  #306 (line in Coconut source)
        if _coconut_match_set_name_xs is not _coconut_sentinel:  #306 (line in Coconut source)
            xs = _coconut_match_set_name_xs  #306 (line in Coconut source)
    if not _coconut_match_check_1:  #306 (line in Coconut source)
        raise _coconut_FunctionMatchError('addpattern def mean(() :: xs) =', _coconut_match_args)  #306 (line in Coconut source)

    return (mean)((tuple)(xs))  #306 (line in Coconut source)



def median(xs):  #309 (line in Coconut source)
    """Compute the median of the given sequence."""  #310 (line in Coconut source)
    sorted_xs = (tuple)((sorted)(xs))  #311 (line in Coconut source)
    return mean((sorted_xs[len(sorted_xs) // 2], sorted_xs[(len(sorted_xs) + 1) // 2]))  #312 (line in Coconut source)



def stdev(xs):  #318 (line in Coconut source)
    """Standard deviation of xs."""  #319 (line in Coconut source)
    mu = mean(xs)  #321 (line in Coconut source)
    xs = tuple(xs)  #322 (line in Coconut source)


    return mean(((x - mu)**2 for x in xs))**0.5  #325 (line in Coconut source)

def mean_abs_dev(xs):  #325 (line in Coconut source)
    """Mean absolute deviation of xs."""  #326 (line in Coconut source)
    mu = mean(xs)  #328 (line in Coconut source)
    xs = tuple(xs)  #329 (line in Coconut source)

    return mean((abs(x - mu) for x in xs))  #331 (line in Coconut source)
