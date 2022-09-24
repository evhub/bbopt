#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xc0ef3eb3

# Compiled with Coconut version 2.0.0-a_dev65 [How Not to Be Seen]

"""
The main BBopt interface.
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



import os  #5 (line num in coconut source)
sys = _coconut_sys  #6 (line num in coconut source)
import json  #7 (line num in coconut source)
if _coconut_sys.version_info >= (3,):  #8 (line num in coconut source)
    import pickle  #8 (line num in coconut source)
else:  #8 (line num in coconut source)
    import cPickle as pickle  #8 (line num in coconut source)
import math  #9 (line num in coconut source)
import itertools  #10 (line num in coconut source)
import time  #11 (line num in coconut source)
from collections import defaultdict  #12 (line num in coconut source)
from pprint import pprint  #13 (line num in coconut source)

import numpy as np  #15 (line num in coconut source)

from bbopt import constants  #17 (line num in coconut source)
from bbopt.registry import alg_registry  #18 (line num in coconut source)
from bbopt.registry import meta_registry  #18 (line num in coconut source)
from bbopt.util import Str  #22 (line num in coconut source)
from bbopt.util import norm_path  #22 (line num in coconut source)
from bbopt.util import json_serialize  #22 (line num in coconut source)
from bbopt.util import best_example  #22 (line num in coconut source)
from bbopt.util import sync_file  #22 (line num in coconut source)
from bbopt.util import ensure_file  #22 (line num in coconut source)
from bbopt.util import clear_file  #22 (line num in coconut source)
from bbopt.util import denumpy_all  #22 (line num in coconut source)
from bbopt.util import sorted_examples  #22 (line num in coconut source)
from bbopt.util import running_best  #22 (line num in coconut source)
from bbopt.util import plot  #22 (line num in coconut source)
from bbopt.util import open_with_lock  #22 (line num in coconut source)
from bbopt.util import printerr  #22 (line num in coconut source)
from bbopt.util import convert_match_errors  #22 (line num in coconut source)
from bbopt.params import param_processor  #38 (line num in coconut source)
from bbopt.backends.util import get_backend  #39 (line num in coconut source)
from bbopt.backends.serving import ServingBackend  #40 (line num in coconut source)


# Utilities:

def array_param(func, name, shape, kwargs):  #45 (line num in coconut source)
    """Create a new array parameter for the given name and shape with entries from func."""  #46 (line num in coconut source)
    if not isinstance(name, Str):  #47 (line num in coconut source)
        raise TypeError("name must be string, not {_coconut_format_0}".format(_coconut_format_0=(name)))  #48 (line num in coconut source)
    arr = np.zeros(shape)  #49 (line num in coconut source)
    for indices in itertools.product(*map(range, shape)):  #50 (line num in coconut source)
        index_str = ",".join(map(str, indices))  #51 (line num in coconut source)
        cell_name = "{_coconut_format_0}[{_coconut_format_1}]".format(_coconut_format_0=(name), _coconut_format_1=(index_str))  #52 (line num in coconut source)
        proc_kwargs = (param_processor.modify_kwargs)(lambda _=None: _[indices], kwargs)  #53 (line num in coconut source)
        arr[indices] = func(cell_name, **proc_kwargs)  #54 (line num in coconut source)
    return arr  #55 (line num in coconut source)


# Optimizer:


class BlackBoxOptimizer(_coconut.object):  #60 (line num in coconut source)
    """Main bbopt optimizer object. See https://github.com/evhub/bbopt for documentation."""  #61 (line num in coconut source)
    backend = None  #62 (line num in coconut source)
    _new_params = None  #63 (line num in coconut source)
    _current_example = None  #64 (line num in coconut source)

    @_coconut_mark_as_match  #66 (line num in coconut source)
    def __init__(*_coconut_match_args, **_coconut_match_kwargs):  #66 (line num in coconut source)
        _coconut_match_check_0 = False  #66 (line num in coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #66 (line num in coconut source)
        _coconut_match_set_name_file = _coconut_sentinel  #66 (line num in coconut source)
        _coconut_match_set_name_tag = _coconut_sentinel  #66 (line num in coconut source)
        _coconut_match_set_name_protocol = _coconut_sentinel  #66 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #66 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 2) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "file" in _coconut_match_kwargs)) == 1):  #66 (line num in coconut source)
            _coconut_match_temp_2 = _coconut_match_kwargs.pop("tag") if "tag" in _coconut_match_kwargs else None  #66 (line num in coconut source)
            _coconut_match_temp_3 = _coconut_match_kwargs.pop("protocol") if "protocol" in _coconut_match_kwargs else None  #66 (line num in coconut source)
            _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #66 (line num in coconut source)
            _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("file")  #66 (line num in coconut source)
            _coconut_match_set_name_tag = _coconut_match_temp_2  #66 (line num in coconut source)
            _coconut_match_set_name_protocol = _coconut_match_temp_3  #66 (line num in coconut source)
            if (isinstance)(_coconut_match_temp_1, Str):  #66 (line num in coconut source)
                _coconut_match_set_name_self = _coconut_match_temp_0  #66 (line num in coconut source)
                _coconut_match_set_name_file = _coconut_match_temp_1  #66 (line num in coconut source)
                if not _coconut_match_kwargs:  #66 (line num in coconut source)
                    _coconut_match_check_0 = True  #66 (line num in coconut source)
        if _coconut_match_check_0:  #66 (line num in coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #66 (line num in coconut source)
                self = _coconut_match_set_name_self  #66 (line num in coconut source)
            if _coconut_match_set_name_file is not _coconut_sentinel:  #66 (line num in coconut source)
                file = _coconut_match_set_name_file  #66 (line num in coconut source)
            if _coconut_match_set_name_tag is not _coconut_sentinel:  #66 (line num in coconut source)
                tag = _coconut_match_set_name_tag  #66 (line num in coconut source)
            if _coconut_match_set_name_protocol is not _coconut_sentinel:  #66 (line num in coconut source)
                protocol = _coconut_match_set_name_protocol  #66 (line num in coconut source)
        if not _coconut_match_check_0:  #66 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def __init__(self, file `isinstance` Str, *, tag=None, protocol=None):', _coconut_match_args)  #66 (line num in coconut source)

        self._backend_creation_counts = defaultdict(int)  #67 (line num in coconut source)

        self._file = norm_path(file)  #69 (line num in coconut source)
        self._tag = (lambda _coconut_x: None if _coconut_x is None else (str)(_coconut_x))(tag)  #70 (line num in coconut source)

        if protocol is None:  #72 (line num in coconut source)
# auto-detect protocol
            self.protocol = "json"  #74 (line num in coconut source)
            if not os.path.exists(self.data_file):  #75 (line num in coconut source)
                self.protocol = constants.default_protocol  #76 (line num in coconut source)
        else:  #77 (line num in coconut source)
            self.protocol = protocol  #78 (line num in coconut source)

        self.reload()  #80 (line num in coconut source)


    @convert_match_errors  #82 (line num in coconut source)
    @_coconut_addpattern(__init__)  #83 (line num in coconut source)
    @_coconut_mark_as_match  #83 (line num in coconut source)
    def __init__(*_coconut_match_args, **_coconut_match_kwargs):  #83 (line num in coconut source)
        """
        Construct a new BlackBoxOptimizer. You must either pass file=__file__ or
        both data_dir="/path/to/some/dir" and data_name="my_project_name".
        """  #87 (line num in coconut source)
        _coconut_match_check_1 = False  #88 (line num in coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #88 (line num in coconut source)
        _coconut_match_set_name_data_dir = _coconut_sentinel  #88 (line num in coconut source)
        _coconut_match_set_name_data_name = _coconut_sentinel  #88 (line num in coconut source)
        _coconut_match_set_name_kwargs = _coconut_sentinel  #88 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #88 (line num in coconut source)
        if (_coconut.len(_coconut_match_args) <= 3) and (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "data_dir" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "data_name" in _coconut_match_kwargs)) == 1):  #88 (line num in coconut source)
            _coconut_match_temp_4 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #88 (line num in coconut source)
            _coconut_match_temp_5 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("data_dir")  #88 (line num in coconut source)
            _coconut_match_temp_6 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("data_name")  #88 (line num in coconut source)
            if ((isinstance)(_coconut_match_temp_5, Str)) and ((isinstance)(_coconut_match_temp_6, Str)):  #88 (line num in coconut source)
                _coconut_match_set_name_self = _coconut_match_temp_4  #88 (line num in coconut source)
                _coconut_match_set_name_data_dir = _coconut_match_temp_5  #88 (line num in coconut source)
                _coconut_match_set_name_data_name = _coconut_match_temp_6  #88 (line num in coconut source)
                _coconut_match_set_name_kwargs = _coconut_match_kwargs  #88 (line num in coconut source)
                _coconut_match_check_1 = True  #88 (line num in coconut source)
        if _coconut_match_check_1:  #88 (line num in coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #88 (line num in coconut source)
                self = _coconut_match_set_name_self  #88 (line num in coconut source)
            if _coconut_match_set_name_data_dir is not _coconut_sentinel:  #88 (line num in coconut source)
                data_dir = _coconut_match_set_name_data_dir  #88 (line num in coconut source)
            if _coconut_match_set_name_data_name is not _coconut_sentinel:  #88 (line num in coconut source)
                data_name = _coconut_match_set_name_data_name  #88 (line num in coconut source)
            if _coconut_match_set_name_kwargs is not _coconut_sentinel:  #88 (line num in coconut source)
                kwargs = _coconut_match_set_name_kwargs  #88 (line num in coconut source)
        if not _coconut_match_check_1:  #88 (line num in coconut source)
            raise _coconut_FunctionMatchError('addpattern def __init__(self, data_dir `isinstance` Str, data_name `isinstance` Str, **kwargs):', _coconut_match_args)  #88 (line num in coconut source)

        self.__init__(os.path.join(data_dir, data_name), **kwargs)  #88 (line num in coconut source)

# Private utilities:


    def _loads(self, raw_contents):  #92 (line num in coconut source)
        """Load data from the given raw data string."""  #93 (line num in coconut source)
        if self.using_json:  #94 (line num in coconut source)
            return json.loads(str(raw_contents, encoding="utf-8"))  #95 (line num in coconut source)
        else:  #96 (line num in coconut source)
            return pickle.loads(raw_contents)  #97 (line num in coconut source)


    def _dumps(self, unserialized_data):  #99 (line num in coconut source)
        """Dump data to a raw data string."""  #100 (line num in coconut source)
        if self.using_json:  #101 (line num in coconut source)
            return json.dumps((json_serialize)(unserialized_data)).encode(encoding="utf-8")  #102 (line num in coconut source)
        else:  #103 (line num in coconut source)
            return pickle.dumps(unserialized_data, protocol=self.protocol)  #104 (line num in coconut source)


    @property  #106 (line num in coconut source)
    def _got_reward(self):  #107 (line num in coconut source)
        """Whether we have seen a maximize/minimize call yet."""  #108 (line num in coconut source)
        return "loss" in self._current_example or "gain" in self._current_example  #109 (line num in coconut source)


    def _set_reward(self, reward_type, value):  #111 (line num in coconut source)
        """Set the gain or loss to the given value."""  #112 (line num in coconut source)
        if self._got_reward:  #113 (line num in coconut source)
            raise ValueError("only one call to maximize or minimize is allowed")  #114 (line num in coconut source)
        if isinstance(value, np.ndarray):  #115 (line num in coconut source)
            if len(value.shape) != 1:  #116 (line num in coconut source)
                raise ValueError("gain/loss must be a scalar or 1-dimensional array, not {_coconut_format_0}".format(_coconut_format_0=(value)))  #117 (line num in coconut source)
            value = tuple(value)  #118 (line num in coconut source)
        self._current_example[reward_type] = denumpy_all(value)  #119 (line num in coconut source)
        if not self.is_serving:  #120 (line num in coconut source)
            self._save_current_data()  #121 (line num in coconut source)
# _save_current_data ensures that _old_params has already been
#  updated with _new_params, so _new_params can safely be cleared
        self._new_params = {}  #124 (line num in coconut source)


    def _add_examples(self, examples):  #126 (line num in coconut source)
        """Load the given examples into memory."""  #127 (line num in coconut source)
        for ex in examples:  #128 (line num in coconut source)
            if ex not in self._examples:  #129 (line num in coconut source)
                for name, val in (list)(ex["values"].items()):  #130 (line num in coconut source)
                    func, args, kwargs = (lambda _coconut_x: self._old_params[name] if _coconut_x is None else _coconut_x)((lambda _coconut_x: None if _coconut_x is None else _coconut_x.get(name))(self._new_params))  #131 (line num in coconut source)
                    ex["values"][name] = param_processor.verify_support(name, val, func, *args, **kwargs)  #132 (line num in coconut source)
                self._examples.append(ex)  #133 (line num in coconut source)


    def _load_from(self, df):  #135 (line num in coconut source)
        """Load data from the given file."""  #136 (line num in coconut source)
        contents = df.read()  #137 (line num in coconut source)
        if contents:  #138 (line num in coconut source)
            _coconut_match_to_0 = self._loads(contents)  #139 (line num in coconut source)
            _coconut_match_check_2 = False  #139 (line num in coconut source)
            _coconut_match_set_name_params = _coconut_sentinel  #139 (line num in coconut source)
            _coconut_match_set_name_examples = _coconut_sentinel  #139 (line num in coconut source)
            if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):  #139 (line num in coconut source)
                _coconut_match_temp_7 = _coconut_match_to_0.get("params", _coconut_sentinel)  #139 (line num in coconut source)
                _coconut_match_temp_8 = _coconut_match_to_0.get("examples", _coconut_sentinel)  #139 (line num in coconut source)
                if (_coconut_match_temp_7 is not _coconut_sentinel) and (_coconut_match_temp_8 is not _coconut_sentinel):  #139 (line num in coconut source)
                    _coconut_match_set_name_params = _coconut_match_temp_7  #139 (line num in coconut source)
                    _coconut_match_set_name_examples = _coconut_match_temp_8  #139 (line num in coconut source)
                    _coconut_match_check_2 = True  #139 (line num in coconut source)
            if _coconut_match_check_2:  #139 (line num in coconut source)
                if _coconut_match_set_name_params is not _coconut_sentinel:  #139 (line num in coconut source)
                    params = _coconut_match_set_name_params  #139 (line num in coconut source)
                if _coconut_match_set_name_examples is not _coconut_sentinel:  #139 (line num in coconut source)
                    examples = _coconut_match_set_name_examples  #139 (line num in coconut source)
            if not _coconut_match_check_2:  #139 (line num in coconut source)
                raise _coconut_MatchError('{"params": params, "examples": examples} = self._loads(contents)', _coconut_match_to_0)  #139 (line num in coconut source)

            self._old_params = params  #140 (line num in coconut source)
            self._add_examples(examples)  #141 (line num in coconut source)


    def _load_data(self):  #143 (line num in coconut source)
        """Load examples from data file."""  #144 (line num in coconut source)
        ensure_file(self.data_file)  #145 (line num in coconut source)
        with open_with_lock(self.data_file) as df:  #146 (line num in coconut source)
            self._load_from(df)  #147 (line num in coconut source)


    def _save_current_data(self):  #149 (line num in coconut source)
        """Save examples to data file."""  #150 (line num in coconut source)
        assert "timestamp" not in self._current_example, "multiple _save_current_data calls on _current_example = {_coconut_format_0}".format(_coconut_format_0=(self._current_example))  #151 (line num in coconut source)
        with open_with_lock(self.data_file) as df:  #152 (line num in coconut source)
# we create the timestamp while we have the lock to ensure its uniqueness
            self._current_example["timestamp"] = time.time()  #154 (line num in coconut source)
            self._add_examples([self._current_example,])  #155 (line num in coconut source)
            self._save_to(df)  #156 (line num in coconut source)


    def _save_to(self, df):  #158 (line num in coconut source)
        """Save to the given open data file."""  #159 (line num in coconut source)
        self._load_from(df)  #160 (line num in coconut source)
        clear_file(df)  #161 (line num in coconut source)
        ((df.write)((self._dumps)(self.get_data())))  #162 (line num in coconut source)
        sync_file(df)  #165 (line num in coconut source)


    @_coconut_mark_as_match  #167 (line num in coconut source)
    def _get_backend(*_coconut_match_args, **_coconut_match_kwargs):  #167 (line num in coconut source)
        """Get the given backend, attempting to load from stored backends."""  #168 (line num in coconut source)
        _coconut_match_check_3 = False  #169 (line num in coconut source)
        _coconut_match_set_name_self = _coconut_sentinel  #169 (line num in coconut source)
        _coconut_match_set_name_backend = _coconut_sentinel  #169 (line num in coconut source)
        _coconut_match_set_name_args = _coconut_sentinel  #169 (line num in coconut source)
        _coconut_match_set_name__in_meta_run = _coconut_sentinel  #169 (line num in coconut source)
        _coconut_match_set_name_options = _coconut_sentinel  #169 (line num in coconut source)
        _coconut_FunctionMatchError = _coconut_get_function_match_error()  #169 (line num in coconut source)
        if (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "self" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "backend" in _coconut_match_kwargs)) == 1):  #169 (line num in coconut source)
            _coconut_match_set_name_args = _coconut_match_args[2:]  #169 (line num in coconut source)
            _coconut_match_temp_11 = _coconut_match_kwargs.pop("_in_meta_run") if "_in_meta_run" in _coconut_match_kwargs else False  #169 (line num in coconut source)
            _coconut_match_temp_9 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("self")  #169 (line num in coconut source)
            _coconut_match_temp_10 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("backend")  #169 (line num in coconut source)
            _coconut_match_set_name__in_meta_run = _coconut_match_temp_11  #169 (line num in coconut source)
            _coconut_match_set_name_self = _coconut_match_temp_9  #169 (line num in coconut source)
            _coconut_match_set_name_backend = _coconut_match_temp_10  #169 (line num in coconut source)
            _coconut_match_set_name_options = _coconut_match_kwargs  #169 (line num in coconut source)
            _coconut_match_check_3 = True  #169 (line num in coconut source)
        if _coconut_match_check_3:  #169 (line num in coconut source)
            if _coconut_match_set_name_self is not _coconut_sentinel:  #169 (line num in coconut source)
                self = _coconut_match_set_name_self  #169 (line num in coconut source)
            if _coconut_match_set_name_backend is not _coconut_sentinel:  #169 (line num in coconut source)
                backend = _coconut_match_set_name_backend  #169 (line num in coconut source)
            if _coconut_match_set_name_args is not _coconut_sentinel:  #169 (line num in coconut source)
                args = _coconut_match_set_name_args  #169 (line num in coconut source)
            if _coconut_match_set_name__in_meta_run is not _coconut_sentinel:  #169 (line num in coconut source)
                _in_meta_run = _coconut_match_set_name__in_meta_run  #169 (line num in coconut source)
            if _coconut_match_set_name_options is not _coconut_sentinel:  #169 (line num in coconut source)
                options = _coconut_match_set_name_options  #169 (line num in coconut source)
        if not _coconut_match_check_3:  #169 (line num in coconut source)
            raise _coconut_FunctionMatchError('match def _get_backend(self, backend, *args, _in_meta_run=False, **options) =', _coconut_match_args)  #169 (line num in coconut source)

        def _coconut_lambda_0(backend):  #169 (line num in coconut source)
            self._backend_creation_counts[type(backend)] += 1  #169 (line num in coconut source)
        return get_backend(self._backend_store, backend, self._examples, self._old_params if not _in_meta_run else dict(((name), (param)) for name, param in self._old_params.items() if name != constants.meta_opt_alg_var), *args, _current_backend=self.backend, _on_new_backend=(_coconut_lambda_0), **options)  #169 (line num in coconut source)


    def _get_skopt_backend(self):  #180 (line num in coconut source)
        """Get a scikit-optimize backend regardless of whether currently using one."""  #181 (line num in coconut source)
        from bbopt.backends.skopt import SkoptBackend  #182 (line num in coconut source)

        if isinstance(self.backend, SkoptBackend):  #184 (line num in coconut source)
            return self.backend  #185 (line num in coconut source)
        else:  #186 (line num in coconut source)
            return self._get_backend(SkoptBackend)  #187 (line num in coconut source)


    @property  #189 (line num in coconut source)
    def _file_name(self):  #190 (line num in coconut source)
        """The base name of the given file."""  #191 (line num in coconut source)
        return os.path.splitext(os.path.basename(self._file))[0] + ("_" + self._tag if self._tag is not None else "")  #192 (line num in coconut source)

# External but undocumented:


    def reload(self):  #196 (line num in coconut source)
        """Completely reload the optimizer."""  #197 (line num in coconut source)
        self._backend_store = defaultdict(list)  #198 (line num in coconut source)
        self._old_params = {}  #199 (line num in coconut source)
        self._examples = []  #200 (line num in coconut source)
        self._load_data()  #201 (line num in coconut source)
        self.run_backend(ServingBackend)  #202 (line num in coconut source)


    def save_data(self):  #204 (line num in coconut source)
        """Forcibly saves data."""  #205 (line num in coconut source)
        with open_with_lock(self.data_file) as df:  #206 (line num in coconut source)
            self._save_to(df)  #207 (line num in coconut source)


    @property  #209 (line num in coconut source)
    def metric(self):  #210 (line num in coconut source)
        """Whether using a gain or a loss."""  #211 (line num in coconut source)
        assert self._examples, "cannot determine metric from empty examples"  #212 (line num in coconut source)
        return "gain" if "gain" in self._examples[0] else "loss"  #213 (line num in coconut source)


    @property  #215 (line num in coconut source)
    def using_json(self):  #216 (line num in coconut source)
        """Whether we are currently saving in json or pickle."""  #217 (line num in coconut source)
        return self.protocol == "json"  #218 (line num in coconut source)


    @property  #220 (line num in coconut source)
    def num_examples(self):  #221 (line num in coconut source)
        """The number of examples seen so far (current example not counted until maximize/minimize call)."""  #222 (line num in coconut source)
        return len(self._examples)  #223 (line num in coconut source)

# Public API:


    def param(self, name, func, *args, **kwargs):  #227 (line num in coconut source)
        """Create a black box parameter and return its value."""  #228 (line num in coconut source)
        if self._got_reward:  #229 (line num in coconut source)
            raise ValueError("all parameter definitions must come before maximize/minimize")  #230 (line num in coconut source)
        if not isinstance(name, Str):  #231 (line num in coconut source)
            raise TypeError("name must be a string, not {_coconut_format_0}".format(_coconut_format_0=(name)))  #232 (line num in coconut source)
        if name in self._new_params:  #233 (line num in coconut source)
            raise ValueError("parameter of name {_coconut_format_0} already exists".format(_coconut_format_0=(name)))  #234 (line num in coconut source)

        args = param_processor.standardize_args(func, args)  #236 (line num in coconut source)
        kwargs = param_processor.standardize_kwargs(kwargs)  #237 (line num in coconut source)

        _coconut_match_to_1 = self._old_params  #239 (line num in coconut source)
        _coconut_match_check_4 = False  #239 (line num in coconut source)
        _coconut_match_set_name_old_func = _coconut_sentinel  #239 (line num in coconut source)
        _coconut_match_set_name_old_args = _coconut_sentinel  #239 (line num in coconut source)
        _coconut_match_set_name_old_kwargs = _coconut_sentinel  #239 (line num in coconut source)
        if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):  #239 (line num in coconut source)
            _coconut_match_temp_12 = _coconut_match_to_1.get(name, _coconut_sentinel)  #239 (line num in coconut source)
            if (_coconut_match_temp_12 is not _coconut_sentinel) and (_coconut.isinstance(_coconut_match_temp_12, _coconut.abc.Sequence)) and (_coconut.len(_coconut_match_temp_12) == 3):  #239 (line num in coconut source)
                _coconut_match_set_name_old_func = _coconut_match_temp_12[0]  #239 (line num in coconut source)
                _coconut_match_set_name_old_args = _coconut_match_temp_12[1]  #239 (line num in coconut source)
                _coconut_match_set_name_old_kwargs = _coconut_match_temp_12[2]  #239 (line num in coconut source)
                _coconut_match_check_4 = True  #239 (line num in coconut source)
        if _coconut_match_check_4:  #239 (line num in coconut source)
            if _coconut_match_set_name_old_func is not _coconut_sentinel:  #239 (line num in coconut source)
                old_func = _coconut_match_set_name_old_func  #239 (line num in coconut source)
            if _coconut_match_set_name_old_args is not _coconut_sentinel:  #239 (line num in coconut source)
                old_args = _coconut_match_set_name_old_args  #239 (line num in coconut source)
            if _coconut_match_set_name_old_kwargs is not _coconut_sentinel:  #239 (line num in coconut source)
                old_kwargs = _coconut_match_set_name_old_kwargs  #239 (line num in coconut source)
        if _coconut_match_check_4:  #239 (line num in coconut source)
            if (func, args) != (old_func, old_args):  #240 (line num in coconut source)
                printerr("BBopt Warning: detected change in parameter {_coconut_format_0} ({_coconut_format_1} != {_coconut_format_2}) (you may need to delete your old BBopt data)".format(_coconut_format_0=(name), _coconut_format_1=((func, args)), _coconut_format_2=((old_func, old_args))))  #241 (line num in coconut source)

        value = self.backend.param(name, func, *args, **kwargs)  #243 (line num in coconut source)
        self._new_params[name] = (func, args, kwargs)  #244 (line num in coconut source)
        self._current_example["values"][name] = value  #245 (line num in coconut source)
        return value  #246 (line num in coconut source)


    def run_backend(self, backend, *args, **options):  #248 (line num in coconut source)
        """Optimize parameters using the given backend."""  #249 (line num in coconut source)
        if self._new_params:  #250 (line num in coconut source)
            raise ValueError("run must come before parameter definitions or after maximize/minimize")  #251 (line num in coconut source)
        self.backend = self._get_backend(backend, *args, **options)  #252 (line num in coconut source)
        self._new_params = {}  #253 (line num in coconut source)
        self._current_example = {"values": {}}  #254 (line num in coconut source)


    @property  #256 (line num in coconut source)
    def algs(self):  #257 (line num in coconut source)
        """All algorithms supported by run."""  #258 (line num in coconut source)
        algs = alg_registry.asdict()  #259 (line num in coconut source)
        algs.update(meta_registry.asdict())  #260 (line num in coconut source)
        return algs  #261 (line num in coconut source)


    def run(self, alg=constants.default_alg_sentinel):  #263 (line num in coconut source)
        """Optimize parameters using the given algorithm
        (use .algs to get the list of valid algorithms)."""  #265 (line num in coconut source)
        if alg is constants.default_alg_sentinel:  #266 (line num in coconut source)
            alg = constants.default_alg  #267 (line num in coconut source)
        if alg in meta_registry:  #268 (line num in coconut source)
            algs, meta_alg = meta_registry[alg]  #269 (line num in coconut source)
            self.run_meta(algs, meta_alg)  #270 (line num in coconut source)
        else:  #271 (line num in coconut source)
            backend, options = alg_registry[alg]  #272 (line num in coconut source)
            self.run_backend(backend, **options)  #273 (line num in coconut source)


    def run_meta(self, algs, meta_alg=constants.default_alg_sentinel):  #275 (line num in coconut source)
        """Dynamically choose the best algorithm from the given set of algorithms."""  #276 (line num in coconut source)
        if meta_alg is constants.default_alg_sentinel:  #277 (line num in coconut source)
            meta_alg = constants.default_meta_alg  #278 (line num in coconut source)
        self.run(meta_alg)  #279 (line num in coconut source)
        alg = self.choice(constants.meta_opt_alg_var, algs)  #280 (line num in coconut source)
        backend, options = alg_registry[alg]  #281 (line num in coconut source)
        self.backend = self._get_backend(backend, _in_meta_run=True, **options)  #282 (line num in coconut source)


    def remember(self, info):  #284 (line num in coconut source)
        """Store a dictionary of information about the current run."""  #285 (line num in coconut source)
        if self._got_reward:  #286 (line num in coconut source)
            raise ValueError("remember calls must come before maximize/minimize")  #287 (line num in coconut source)
        self._current_example.setdefault("memo", {}).update(info)  #288 (line num in coconut source)


    def minimize(self, value):  #290 (line num in coconut source)
        """Set the loss of the current run."""  #291 (line num in coconut source)
        self._set_reward("loss", value)  #292 (line num in coconut source)


    def maximize(self, value):  #294 (line num in coconut source)
        """Set the gain of the current run."""  #295 (line num in coconut source)
        self._set_reward("gain", value)  #296 (line num in coconut source)


    @property  #298 (line num in coconut source)
    def is_serving(self):  #299 (line num in coconut source)
        """Whether we are currently using the serving backend or not."""  #300 (line num in coconut source)
        return isinstance(self.backend, ServingBackend) and not self.backend.allow_missing_data  #301 (line num in coconut source)


    @property  #303 (line num in coconut source)
    def data_file(self):  #304 (line num in coconut source)
        """The path to the file we are saving data to."""  #305 (line num in coconut source)
        return os.path.join(os.path.dirname(self._file), self._file_name) + constants.data_file_ext + (".json" if self.using_json else ".pickle")  #306 (line num in coconut source)


    def get_data(self, print_data=False):  #308 (line num in coconut source)
        """Get all currently-loaded data as a dictionary containing params and examples."""  #309 (line num in coconut source)
        self._old_params.update(self._new_params)  #310 (line num in coconut source)
        data_dict = {"params": self._old_params, "examples": self._examples}  #311 (line num in coconut source)
        if print_data:  #315 (line num in coconut source)
            pprint(data_dict)  #316 (line num in coconut source)
        return data_dict  #317 (line num in coconut source)


    def tell_examples(self, examples):  #319 (line num in coconut source)
        """Adds the given examples to memory and writes the current memory to disk."""  #320 (line num in coconut source)
        self._add_examples(examples)  #321 (line num in coconut source)
        self.save_data()  #322 (line num in coconut source)


    def get_current_run(self):  #324 (line num in coconut source)
        """Return a dictionary containing the current parameters and reward."""  #325 (line num in coconut source)
        if self._current_example is None:  #326 (line num in coconut source)
            raise ValueError("get_current_run calls must come after run")  #327 (line num in coconut source)
        return self._current_example  #328 (line num in coconut source)


    def get_best_run(self):  #330 (line num in coconut source)
        """Return a dictionary containing the best parameters and reward computed so far."""  #331 (line num in coconut source)
        return best_example(self._examples)  #332 (line num in coconut source)


    get_optimal_run = get_best_run  #334 (line num in coconut source)

    @property  #336 (line num in coconut source)
    def run_id(self):  #337 (line num in coconut source)
        """The run ID number if using bbopt CLI."""  #338 (line num in coconut source)
        return (lambda _coconut_x: None if _coconut_x is None else (int)(_coconut_x))(os.getenv(constants.run_id_env_var))  #339 (line num in coconut source)

# Plotting functions:


    def plot_convergence(self, ax=None, yscale=None, label=None):  #343 (line num in coconut source)
        """Plot the best gain/loss over the history of optimization.
        Based on skopt.plots.plot_convergence."""  #345 (line num in coconut source)
        if not self._examples:  #346 (line num in coconut source)
            raise ValueError("no existing data available to be plotted")  #347 (line num in coconut source)

        iterations = range(1, len(self._examples) + 1)  #349 (line num in coconut source)
        best_metrics = ((list)((map)(_coconut.operator.itemgetter((self.metric)), (running_best)((sorted_examples)(self._examples)))))  #350 (line num in coconut source)

        return plot(iterations, best_metrics, ax=ax, yscale=yscale, title="Convergence plot for {_coconut_format_0}".format(_coconut_format_0=(self._file_name)), label=("{_coconut_format_0}".format(_coconut_format_0=(self._file_name)) if label is None else label), xlabel="Number of trials $n$", ylabel="Best {_coconut_format_0} after $n$ trials".format(_coconut_format_0=(self.metric)))  #358 (line num in coconut source)


    def plot_history(self, ax=None, yscale=None, label=None):  #369 (line num in coconut source)
        """Plot the gain/loss of every point in the order in which they were sampled."""  #370 (line num in coconut source)
        if not self._examples:  #371 (line num in coconut source)
            raise ValueError("no existing data available to be plotted")  #372 (line num in coconut source)

        iterations = range(1, len(self._examples) + 1)  #374 (line num in coconut source)
        metrics = ((list)((map)(_coconut.operator.itemgetter((self.metric)), (sorted_examples)(self._examples))))  #375 (line num in coconut source)

        return plot(iterations, metrics, ax=ax, yscale=yscale, title="History plot for {_coconut_format_0}".format(_coconut_format_0=(self._file_name)), label=("{_coconut_format_0}".format(_coconut_format_0=(self._file_name)) if label is None else label), xlabel="Number of trials $n$", ylabel="The {_coconut_format_0} on the $n$th trial".format(_coconut_format_0=(self.metric)))  #382 (line num in coconut source)


    def partial_dependence(self, i_name, j_name=None, *args, **kwargs):  #393 (line num in coconut source)
        """Calls skopt.plots.partial_dependence where i_name and j_name are parameter names."""  #394 (line num in coconut source)
        def _coconut_mock_9(self, i_name, j_name=_coconut_sentinel, *args, **kwargs):  #395 (line num in coconut source)
            if j_name is _coconut_sentinel: j_name = _coconut_recursive_func_27.__defaults__[0]  #395 (line num in coconut source)
            return self, i_name, j_name, args, kwargs  #395 (line num in coconut source)
        while True:  #395 (line num in coconut source)
            from skopt.plots import partial_dependence  #395 (line num in coconut source)
            if not self._examples:  #396 (line num in coconut source)
                raise ValueError("no existing data available to be plotted")  #397 (line num in coconut source)

            skopt_backend = self._get_skopt_backend()  #399 (line num in coconut source)

            sorted_names = list(sorted(self._old_params))  #401 (line num in coconut source)
            i = sorted_names.index(i_name)  #402 (line num in coconut source)
            j = None if j_name is None else sorted_names.index(j_name)  #403 (line num in coconut source)

            try:  #405 (line num in coconut source)
                _coconut_tre_check_0 = partial_dependence is _coconut_recursive_func_27  #405 (line num in coconut source)
            except _coconut.NameError:  #405 (line num in coconut source)
                _coconut_tre_check_0 = False  #405 (line num in coconut source)
            if _coconut_tre_check_0:  #405 (line num in coconut source)
                self, i_name, j_name, args, kwargs = _coconut_mock_9(skopt_backend.space, skopt_backend.model, i, j, *args, **kwargs)  #405 (line num in coconut source)
                continue  #405 (line num in coconut source)
            else:  #405 (line num in coconut source)
                return partial_dependence(skopt_backend.space, skopt_backend.model, i, j, *args, **kwargs)  #413 (line num in coconut source)
            return None  #414 (line num in coconut source)

    _coconut_recursive_func_27 = partial_dependence  #414 (line num in coconut source)

    def plot_partial_dependence_1D(self, i_name, ax=None, yscale=None, label=None, **kwargs):  #414 (line num in coconut source)
        """Constructs a 1D partial dependence plot using self.partial_dependence."""  #415 (line num in coconut source)
        xi, yi = self.partial_dependence(i_name, **kwargs)  #416 (line num in coconut source)
        return plot(xi, yi, ax=ax, yscale=yscale, title="Partial dependence of {_coconut_format_0} in {_coconut_format_1}".format(_coconut_format_0=(i_name), _coconut_format_1=(self._file_name)), label=("{_coconut_format_0}".format(_coconut_format_0=(i_name)) if label is None else label), xlabel="Values of {_coconut_format_0}".format(_coconut_format_0=(i_name)), ylabel="The loss at each point".format())  #417 (line num in coconut source)


    def get_skopt_result(self):  #428 (line num in coconut source)
        """Get a result object usable by skopt.plots functions."""  #429 (line num in coconut source)
        if not self._examples:  #430 (line num in coconut source)
            raise ValueError("no existing data available to be plotted")  #431 (line num in coconut source)
        return self._get_skopt_backend().result  #432 (line num in coconut source)


    def plot_evaluations(self, *args, **kwargs):  #434 (line num in coconut source)
        """Calls skopt.plots.plot_evaluations."""  #435 (line num in coconut source)
        def _coconut_mock_11(self, *args, **kwargs):  #436 (line num in coconut source)
            return self, args, kwargs  #436 (line num in coconut source)
        while True:  #436 (line num in coconut source)
            from skopt.plots import plot_evaluations  #436 (line num in coconut source)
            try:  #437 (line num in coconut source)
                _coconut_tre_check_1 = plot_evaluations is _coconut_recursive_func_30  #437 (line num in coconut source)
            except _coconut.NameError:  #437 (line num in coconut source)
                _coconut_tre_check_1 = False  #437 (line num in coconut source)
            if _coconut_tre_check_1:  #437 (line num in coconut source)
                self, args, kwargs = _coconut_mock_11(self.get_skopt_result(), *args, **kwargs)  #437 (line num in coconut source)
                continue  #437 (line num in coconut source)
            else:  #437 (line num in coconut source)
                return plot_evaluations(self.get_skopt_result(), *args, **kwargs)  #438 (line num in coconut source)
            return None  #439 (line num in coconut source)

    _coconut_recursive_func_30 = plot_evaluations  #439 (line num in coconut source)

    def plot_objective(self, *args, **kwargs):  #439 (line num in coconut source)
        """Calls skopt.plots.plot_objective."""  #440 (line num in coconut source)
        def _coconut_mock_12(self, *args, **kwargs):  #441 (line num in coconut source)
            return self, args, kwargs  #441 (line num in coconut source)
        while True:  #441 (line num in coconut source)
            from skopt.plots import plot_objective  #441 (line num in coconut source)
            try:  #442 (line num in coconut source)
                _coconut_tre_check_2 = plot_objective is _coconut_recursive_func_31  #442 (line num in coconut source)
            except _coconut.NameError:  #442 (line num in coconut source)
                _coconut_tre_check_2 = False  #442 (line num in coconut source)
            if _coconut_tre_check_2:  #442 (line num in coconut source)
                self, args, kwargs = _coconut_mock_12(self.get_skopt_result(), *args, **kwargs)  #442 (line num in coconut source)
                continue  #442 (line num in coconut source)
            else:  #442 (line num in coconut source)
                return plot_objective(self.get_skopt_result(), *args, **kwargs)  #443 (line num in coconut source)
            return None  #444 (line num in coconut source)

    _coconut_recursive_func_31 = plot_objective  #444 (line num in coconut source)

    def plot_regret(self, *args, **kwargs):  #444 (line num in coconut source)
        """Calls skopt.plots.plot_regret."""  #445 (line num in coconut source)
        def _coconut_mock_13(self, *args, **kwargs):  #446 (line num in coconut source)
            return self, args, kwargs  #446 (line num in coconut source)
        while True:  #446 (line num in coconut source)
            from skopt.plots import plot_regret  #446 (line num in coconut source)
            try:  #447 (line num in coconut source)
                _coconut_tre_check_3 = plot_regret is _coconut_recursive_func_32  #447 (line num in coconut source)
            except _coconut.NameError:  #447 (line num in coconut source)
                _coconut_tre_check_3 = False  #447 (line num in coconut source)
            if _coconut_tre_check_3:  #447 (line num in coconut source)
                self, args, kwargs = _coconut_mock_13(self.get_skopt_result(), *args, **kwargs)  #447 (line num in coconut source)
                continue  #447 (line num in coconut source)
            else:  #447 (line num in coconut source)
                return plot_regret(self.get_skopt_result(), *args, **kwargs)  #447 (line num in coconut source)


        return None  #451 (line num in coconut source)

    _coconut_recursive_func_32 = plot_regret  #451 (line num in coconut source)

    def randrange(self, name, *args, **kwargs):  #451 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.randrange(*args)."""  #452 (line num in coconut source)
        return self.param(name, "randrange", *args, **kwargs)  #453 (line num in coconut source)


    def uniform(self, name, a, b, **kwargs):  #455 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.uniform(a, b)."""  #456 (line num in coconut source)
        return self.param(name, "uniform", a, b, **kwargs)  #457 (line num in coconut source)


    def triangular(self, name, low, high, mode, **kwargs):  #459 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.triangular(low, high, mode)."""  #460 (line num in coconut source)
        return self.param(name, "triangular", low, high, mode, **kwargs)  #461 (line num in coconut source)


    def betavariate(self, name, alpha, beta, **kwargs):  #463 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.betavariate(alpha, beta)."""  #464 (line num in coconut source)
        return self.param(name, "betavariate", alpha, beta, **kwargs)  #465 (line num in coconut source)


    def expovariate(self, name, lambd, **kwargs):  #467 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.expovariate(lambd)."""  #468 (line num in coconut source)
        return self.param(name, "expovariate", lambd, **kwargs)  #469 (line num in coconut source)


    def gammavariate(self, name, alpha, beta, **kwargs):  #471 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.gammavariate(alpha, beta)."""  #472 (line num in coconut source)
        return self.param(name, "gammavariate", alpha, beta, **kwargs)  #473 (line num in coconut source)


    def normalvariate(self, name, mu, sigma, **kwargs):  #475 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.gauss(mu, sigma)."""  #476 (line num in coconut source)
        return self.param(name, "normalvariate", mu, sigma, **kwargs)  #477 (line num in coconut source)


    def vonmisesvariate(self, name, kappa, **kwargs):  #479 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.vonmisesvariate(kappa)."""  #480 (line num in coconut source)
        return self.param(name, "vonmisesvariate", kappa, **kwargs)  #481 (line num in coconut source)


    def paretovariate(self, name, alpha, **kwargs):  #483 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.paretovariate(alpha)."""  #484 (line num in coconut source)
        return self.param(name, "paretovariate", alpha, **kwargs)  #485 (line num in coconut source)


    def weibullvariate(self, name, alpha, beta, **kwargs):  #487 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.weibullvariate(alpha, beta)."""  #488 (line num in coconut source)
        return self.param(name, "weibullvariate", alpha, beta, **kwargs)  #489 (line num in coconut source)

# Choice functions:


    def _categorical(self, name, num_categories, **kwargs):  #493 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.choice(range(num_categories))."""  #494 (line num in coconut source)
        return self.param(name, "choice", range(num_categories), **kwargs)  #495 (line num in coconut source)


    def choice(self, name, seq, **kwargs):  #497 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.choice(seq)."""  #498 (line num in coconut source)
        if constants.use_generic_categories_for_categorical_data:  #499 (line num in coconut source)
            (param_processor.modify_kwargs)(seq.index, kwargs)  #500 (line num in coconut source)
            return seq[self._categorical(name, len(seq), **kwargs)]  #501 (line num in coconut source)
        else:  #502 (line num in coconut source)
            return self.param(name, "choice", seq, **kwargs)  #503 (line num in coconut source)

# Derived random functions:


    def randint(self, name, a, b, **kwargs):  #507 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.randint(a, b)."""  #508 (line num in coconut source)
        start, stop = a, b - 1  #509 (line num in coconut source)
        return self.randrange(name, start, stop, **kwargs)  #510 (line num in coconut source)


    def random(self, name, **kwargs):  #512 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.random().
        Equivalent to random.uniform(0, 1) except that 1 is disallowed."""  #514 (line num in coconut source)
        result = self.uniform(name, 0, 1, **kwargs)  #515 (line num in coconut source)
        if result >= 1:  #516 (line num in coconut source)
            result -= sys.float_info.epsilon  #517 (line num in coconut source)
        return result  #518 (line num in coconut source)


    def getrandbits(self, name, k, **kwargs):  #520 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.getrandbits(k)."""  #521 (line num in coconut source)
        stop = 2**k  #522 (line num in coconut source)
        return self.randrange(name, stop, **kwargs)  #523 (line num in coconut source)


    gauss = normalvariate  #525 (line num in coconut source)

    def loguniform(self, name, min_val, max_val, **kwargs):  #527 (line num in coconut source)
        """Create a new parameter with the given name modeled by
        math.exp(random.uniform(math.log(min_val), math.log(max_val)))."""  #529 (line num in coconut source)
        kwargs = (param_processor.modify_kwargs)(math.log, kwargs)  #530 (line num in coconut source)
        log_a, log_b = math.log(min_val), math.log(max_val)  #531 (line num in coconut source)
        return math.exp(self.uniform(name, log_a, log_b, **kwargs))  #532 (line num in coconut source)


    def lognormvariate(self, name, mu, sigma, **kwargs):  #534 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.lognormvariate(mu, sigma)."""  #535 (line num in coconut source)
        kwargs = (param_processor.modify_kwargs)(math.log, kwargs)  #536 (line num in coconut source)
        return math.exp(self.normalvariate(name, mu, sigma, **kwargs))  #537 (line num in coconut source)


    def randbool(self, name, **kwargs):  #539 (line num in coconut source)
        """Create a new boolean parameter with the given name."""  #540 (line num in coconut source)
        return bool(self.choice(name, [False, True], **kwargs))  #541 (line num in coconut source)


    def sample(self, name, population, k, **kwargs):  #543 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.sample(population, k).
        Ordering of elements in the result is random."""  #545 (line num in coconut source)
        if not isinstance(name, Str):  #546 (line num in coconut source)
            raise TypeError("name must be string, not {_coconut_format_0}".format(_coconut_format_0=(name)))  #547 (line num in coconut source)
        sampling_population = [x for x in population]  #548 (line num in coconut source)
        sample = []  #549 (line num in coconut source)
        for i in range(k):  #550 (line num in coconut source)
            if len(sampling_population) <= 1:  #551 (line num in coconut source)
                sample.append(sampling_population[0])  #552 (line num in coconut source)
            else:  #553 (line num in coconut source)
                def _coconut_lambda_1(val):  #554 (line num in coconut source)
                    elem = _coconut_iter_getitem(val, i)  #554 (line num in coconut source)
                    return sampling_population.index(elem) if elem in sampling_population else 0  #554 (line num in coconut source)
                proc_kwargs = (param_processor.modify_kwargs)(_coconut_lambda_1, kwargs)  #554 (line num in coconut source)
                ind = self.randrange("{_coconut_format_0}[{_coconut_format_1}]".format(_coconut_format_0=(name), _coconut_format_1=(i)), len(sampling_population), **proc_kwargs)  #559 (line num in coconut source)
                sample.append(sampling_population.pop(ind))  #560 (line num in coconut source)
        return sample  #561 (line num in coconut source)


    def unshuffled_sample(self, name, population, k, **kwargs):  #563 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.sample(population, k).
        Ordering of elements in the result is the same as in population."""  #565 (line num in coconut source)
        if not isinstance(name, Str):  #566 (line num in coconut source)
            raise TypeError("name must be string, not {_coconut_format_0}".format(_coconut_format_0=(name)))  #567 (line num in coconut source)
        population = tuple(population)  #568 (line num in coconut source)
        sample = []  #569 (line num in coconut source)
        for i, x in enumerate(population):  #570 (line num in coconut source)
            if len(sample) == k:  #571 (line num in coconut source)
                break  #572 (line num in coconut source)
            if len(population) - i == k - len(sample):  #573 (line num in coconut source)
                sample += population[i:]  #574 (line num in coconut source)
                break  #575 (line num in coconut source)
            proc_kwargs = (param_processor.modify_kwargs)(lambda val: 1 if x in val else 0, kwargs)  #576 (line num in coconut source)
            if "placeholder_when_missing" not in proc_kwargs:  #579 (line num in coconut source)
                proc_kwargs["placeholder_when_missing"] = 0  #580 (line num in coconut source)
            if self.uniform("{_coconut_format_0}[{_coconut_format_1}]".format(_coconut_format_0=(name), _coconut_format_1=(i)), 0, 1, **proc_kwargs) >= 1 - (k - len(sample)) / (len(population) - i):  #581 (line num in coconut source)
                sample.append(x)  #587 (line num in coconut source)
        return sample  #588 (line num in coconut source)


    def samples_with_replacement(self, name, population, **kwargs):  #590 (line num in coconut source)
        """An infinite iterator of samples with replacement from population."""  #591 (line num in coconut source)
        if not isinstance(name, Str):  #592 (line num in coconut source)
            raise TypeError("name must be string, not {_coconut_format_0}".format(_coconut_format_0=(name)))  #593 (line num in coconut source)
        population = tuple(population)  #594 (line num in coconut source)
        for i in count():  #595 (line num in coconut source)
            yield self.choice("{_coconut_format_0}[{_coconut_format_1}]".format(_coconut_format_0=(name), _coconut_format_1=(i)), population, **kwargs)  #596 (line num in coconut source)


    def shuffled(self, name, population, **kwargs):  #598 (line num in coconut source)
        """Create a new parameter with the given name modeled by
        random.shuffle(population) except returned instead of modified in place."""  #600 (line num in coconut source)
        return self.sample(name, population, len(population), **kwargs)  #601 (line num in coconut source)


    def shuffle(self, name, population, **kwargs):  #603 (line num in coconut source)
        """Create a new parameter with the given name modeled by random.shuffle(population)."""  #604 (line num in coconut source)
        population[:] = self.shuffled(name, population, **kwargs)  #605 (line num in coconut source)


    def stdnormal(self, name, **kwargs):  #607 (line num in coconut source)
        """Equivalent to bb.normalvariate(name, 0, 1)."""  #608 (line num in coconut source)
        return self.normalvariate(name, 0, 1, **kwargs)  #609 (line num in coconut source)

# Array-based random functions:


    def rand(self, name, *shape, **kwargs):  #613 (line num in coconut source)
        """Create a new array parameter for the given name and shape modeled by np.random.rand."""  #614 (line num in coconut source)
        return array_param(self.random, name, shape, kwargs)  #615 (line num in coconut source)


    def randn(self, name, *shape, **kwargs):  #617 (line num in coconut source)
        """Create a new array parameter for the given name and shape modeled by np.random.randn."""  #618 (line num in coconut source)
        return array_param(self.stdnormal, name, shape, kwargs)  #619 (line num in coconut source)


_coconut_call_set_names(BlackBoxOptimizer)  #621 (line num in coconut source)
