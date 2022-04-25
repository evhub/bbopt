#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x5c9eb0a0

# Compiled with Coconut version 2.0.0-a_dev53 [How Not to Be Seen]

"""
The OpenAI backend. Uses large language models for black box optimization.
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
from __coconut__ import _coconut_call_set_names, _coconut_handle_cls_kwargs, _coconut_handle_cls_stargs, _namedtuple_of, _coconut, _coconut_super, _coconut_MatchError, _coconut_iter_getitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_raise, _coconut_mark_as_match, _coconut_reiterable, _coconut_self_match_types, _coconut_dict_merge, _coconut_exec, _coconut_comma_op, _coconut_multi_dim_arr, _coconut_mk_anon_namedtuple
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import os
from ast import literal_eval

import openai

from bbopt.params import param_processor
from bbopt.backends.util import StandardBackend


# Constants:

DEFAULT_ENGINE = "text-davinci-002"

DEFAULT_TEMP = 1.1
MAX_TEMP = 2

DEFAULT_MAX_RETRIES = 10

MAX_CONTEXT_ERR_PREFIX = "This model's maximum context length is "


# Utilities:

def get_prompt(params, data_points, losses):
    """Get the OpenAI API prompt to use."""
    return '''# black box function to be minimized
def f({func_params}) -> float:
    """
    parameters:
{docstring}

    returns:
        float: the loss
    """
    return black_box_function({names})

# known values (MUST stay within the bounds, SHOULD fully explore the bounds, SHOULD converge to minimum)
# bounds: f({domains})
{values}
assert f('''.format(func_params=", ".join(("{name}: {type}".format(name=name, type=("int" if func == "randrange" else type(args[0][0]).__name__ if func == "choice" and all_equal(map(type, args[0])) else "typing.Any" if func == "choice" else "float")) for name, (func, args, _) in params.items())), docstring="\n".join(("        {name}: in {func}({args})".format(name=name, func=func, args=", ".join((map)(repr, args))) for name, (func, args, _) in params.items())), names=", ".join(params), domains=", ".join(("{func}({args})".format(func=func, args=", ".join((map)(repr, args))) for name, (func, args, _) in params.items())), values="\n".join(("assert f({args}) == {loss}".format(args=", ".join((map)(repr, point.values())), loss=loss) for point, loss in zip(data_points, losses))))



def get_completion_len(data_points):
    """Get the maximum number of characters in a completion."""
    return max((len(", ".join((map)(repr, point.values()))) for point in data_points)) + 1



def to_python(completion, params):
    """Convert a completion to Python code as best as possible."""
    for repl, to in _coconut.itertools.chain.from_iterable(_coconut_reiterable(_coconut_func() for _coconut_func in (lambda: (("\u2212", "-"), ("\u2018", "'"), ("\u2019", "'")), lambda: (("{_coconut_format_0}=".format(_coconut_format_0=(name)), "") for name in params)))):
        completion = completion.replace(repl, to)
    return completion


# Backend:


class OpenAIBackend(StandardBackend):
    """OpenAI large language model BBopt backend."""
    backend_name = "openai"
    implemented_funcs = ("randrange", "uniform", "normalvariate", "choice")

    max_prompt_len = float("inf")

    def setup_backend(self, params, engine=DEFAULT_ENGINE, temperature=DEFAULT_TEMP, max_retries=DEFAULT_MAX_RETRIES, api_key=None, debug=False):
        self.params = params

        self.engine = engine
        self.temp = temperature
        self.max_retries = max_retries
        openai.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.debug = debug

        self.data_points = []
        self.losses = []


    def tell_data(self, new_data, new_losses):
        self.data_points += new_data
        self.losses += new_losses


    def retry_get_values(self, temp=None):
        if not self.max_retries:
            raise RuntimeError("Maximum number of OpenAI API retries exceeded.")
        if self.debug:
            if temp is None:
                print("RETRYING with: self.max_prompt_len={_coconut_format_0}".format(_coconut_format_0=(self.max_prompt_len)))
            else:
                print("RETRYING with new temperature: {_coconut_format_0} -> {_coconut_format_1}".format(_coconut_format_0=(self.temp), _coconut_format_1=(temp)))
        old_retries, self.max_retries = self.max_retries, self.max_retries - 1
        if temp is not None:
            old_temp, self.temp = self.temp, temp
        try:
            return self.get_next_values()
        finally:
            self.max_retries = old_retries
            if temp is not None:
                self.temp = old_temp


    def get_next_values(self):
# generate prompt
        prompt = get_prompt(self.params, self.data_points, self.losses)
        while len(prompt) > self.max_prompt_len:
            self.data_points.pop(0)
            self.losses.pop(0)
        if self.debug:
            print("\n== PROMPT ==\n" + prompt)

# query api
        try:
            response = openai.Completion.create(engine=self.engine, prompt=prompt, temperature=self.temp, max_tokens=get_completion_len(self.data_points))
        except openai.error.InvalidRequestError as api_err:
            if self.debug:
                print("== END ==")
            if not str(api_err).startswith(MAX_CONTEXT_ERR_PREFIX):
                raise
            if self.max_prompt_len == float("inf"):
                self.max_prompt_len = len(prompt.rsplit("\n")[0])
            else:
                self.max_prompt_len -= get_completion_len(self.data_points)
            if self.debug:
                print("ERROR: got max context length error".format())
            return self.retry_get_values()

# parse response
        try:
            completion = response["choices"][0]["text"]
            if self.debug:
                print("== COMPLETION ==\n" + completion)
            valstr = to_python(completion.split(")", 1)[0].strip(), self.params)
            valvec = literal_eval("(" + valstr + ",)")
            assert len(valvec) == len(self.params), "got {_coconut_format_0} values, expected {_coconut_format_1}".format(_coconut_format_0=(len(valvec)), _coconut_format_1=(len(self.params)))
            assert all((param_processor.in_support(name, val, func, *args, **kwargs) for val, (name, (func, args, kwargs)) in zip(valvec, self.params.items()))), "completion value(s) not in support"
        except BaseException as parse_err:
            if self.debug:
                print("== END ==")
            if self.debug:
                print("ERROR: {_coconut_format_0} for API response:\n{_coconut_format_1}".format(_coconut_format_0=(parse_err), _coconut_format_1=(response)))
            return self.retry_get_values(temp=(self.temp + DEFAULT_TEMP) / 2)
        if self.debug:
            print("== END ==")

# return values
        values = dict(((name), (val)) for name, val in zip(self.params, valvec))
        if values in self.data_points:
            if self.debug:
                print("ERROR: OpenAI API generated duplicate value")
            return self.retry_get_values(temp=self.temp + (MAX_TEMP - self.temp) / 2)
        return values


# Registered names:


_coconut_call_set_names(OpenAIBackend)
OpenAIBackend.register()
OpenAIBackend.register_alg("openai")
