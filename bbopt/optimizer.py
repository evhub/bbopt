#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x81c84d40

# Compiled with Coconut version 1.4.0-post_dev7 [Ernest Scribbler]

"""
The main BBopt interface.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_addpattern, _coconut_sentinel
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



import os
import json
if _coconut_sys.version_info < (3,):
    import cPickle as pickle
else:
    import pickle
import math
import itertools

import numpy as np
from portalocker import Lock

from bbopt.backends import backend_registry
from bbopt.backends import init_backend
from bbopt.backends import alg_registry
from bbopt.params import param_processor
from bbopt.util import Str
from bbopt.util import norm_path
from bbopt.util import json_serialize
from bbopt.util import best_example
from bbopt.util import sync_file
from bbopt.util import ensure_file
from bbopt.util import clear_file
from bbopt.constants import data_file_ext
from bbopt.constants import lock_timeout
from bbopt.constants import default_alg


class BlackBoxOptimizer(_coconut.object):
    """Main bbopt optimizer object. See https://github.com/evhub/bbopt for documentation."""

    def __init__(self, file, use_json=None):
        if not isinstance(file, Str):
            raise TypeError("file must be a string")
        self._file = norm_path(file)

        if use_json is None:
# auto-detect use_json, defaulting to False
            self._use_json = True
            if not os.path.exists(self.data_file):
                self._use_json = False
        else:
            self._use_json = use_json

        self.reload()

    def _loads(self, raw_contents):
        if self._use_json:
            return json.loads(raw_contents)
        else:
            return pickle.loads(raw_contents)

    def _dumps(self, unserialized_data):
        if self._use_json:
            return json.dumps((json_serialize)(unserialized_data)).encode(encoding="utf-8")
        else:
            return pickle.dumps(unserialized_data, protocol=pickle.HIGHEST_PROTOCOL)

    def reload(self):
        """Completely reload the optimizer."""
        self._old_params = {}
        self._examples = []
        self._load_data()
        self.run(alg=None)  # backend is set to serving by default

    def run_backend(self, backend, **kwargs):
        """Optimize parameters using the given backend."""
        self._backend = init_backend(backend, self._examples, self._old_params, **kwargs)
        self._new_params = {}
        self._current_example = {"values": {}}

    @property
    def algs(self):
        return dict(((alg), (backend)) for alg, (backend, params) in alg_registry.items())

    def run(self, alg=default_alg):
        """Optimize parameters using the given algorithm
        (use .algs to get the list of valid algorithms)."""
        backend, params = alg_registry[alg]
        self.run_backend(backend, **params)

    @property
    def _got_reward(self):
        return "loss" in self._current_example or "gain" in self._current_example

    def param(self, name, **kwargs):
        """Create a black box parameter and return its value."""
        if self._got_reward:
            raise ValueError("param calls must come before maximize/minimize")
        if not isinstance(name, Str):
            raise TypeError("name must be string, not {}".format(name))
        if name in self._new_params:
            raise ValueError("parameter of name {} already exists".format(name))
        kwargs = (param_processor.standardize_kwargs)(kwargs)
        value = self._backend.param(name, **kwargs)
        self._new_params[name] = kwargs
        self._current_example["values"][name] = value
        return value

    def remember(self, info):
        """Store a dictionary of information about the current run."""
        if self._got_reward:
            raise ValueError("remember calls must come before maximize/minimize")
        self._current_example.setdefault("memo", {}).update(info)

    def minimize(self, value):
        """Set the loss of the current run."""
        self._set_reward("loss", value)

    def maximize(self, value):
        """Set the gain of the current run."""
        self._set_reward("gain", value)

    @property
    def is_serving(self):
        return isinstance(self._backend, backend_registry[None])

    def _set_reward(self, reward_type, value):
        """Set the gain or loss to value."""
        if self._got_reward:
            raise ValueError("only one call to maximize or minimize is allowed")
        if isinstance(value, np.ndarray):
            if len(value.shape) != 1:
                raise ValueError("gain/loss must be a scalar or 1-dimensional array, not {}".format(value))
            value = tuple(value)
        self._current_example[reward_type] = value
        if not self.is_serving:
            self._save_data()

    @property
    def data_file(self):
        return os.path.splitext(self._file)[0] + data_file_ext + (".json" if self._use_json else ".pickle")

    def _tell_examples(self, examples):
        """Load the given examples into memory."""
        for x in examples:
            if x not in self._examples:
                self._examples.append(x)

    def _load_from(self, df):
        """Load data from the given file."""
        contents = df.read()
        if contents:
            _coconut_match_to = self._loads(contents)
            _coconut_match_check = False
            if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
                _coconut_match_temp_0 = _coconut_match_to.get("params", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_match_to.get("examples", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    params = _coconut_match_temp_0
                    examples = _coconut_match_temp_1
                    _coconut_match_check = True
            if not _coconut_match_check:
                _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"params": params, "examples": examples} = self._loads(contents)\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
                _coconut_match_err.pattern = '{"params": params, "examples": examples} = self._loads(contents)'
                _coconut_match_err.value = _coconut_match_to
                raise _coconut_match_err

            self._old_params = params
            self._tell_examples(examples)

    def _load_data(self):
        """Load examples from data file."""
        ensure_file(self.data_file)
        with Lock(self.data_file, "rb", timeout=lock_timeout) as df:
            self._load_from(df)

    def get_data(self):
        self._old_params.update(self._new_params)
        return {"params": self._old_params, "examples": self._examples}

    def _save_data(self):
        """Save examples to data file."""
        self._tell_examples([self._current_example])
        with Lock(self.data_file, "rb+", timeout=lock_timeout) as df:
            self._load_from(df)
            clear_file(df)
            ((df.write)((self._dumps)(self.get_data())))
            sync_file(df)

    def get_current_run(self):
        """Return a dictionary containing the current parameters and reward."""
        try:
            return self._current_example
        except AttributeError:
            raise ValueError("get_current_run calls must come after run")

    def get_optimal_run(self):
        """Return a dictionary containing the optimal parameters and reward computed so far."""
        return best_example(self._examples)

# Base random functions:

    def randrange(self, name, *args, **kwargs):
        """Create a new parameter with the given name modeled by random.randrange(*args)."""
        return self.param(name, randrange=args, **kwargs)

    def choice(self, name, seq, **kwargs):
        """Create a new parameter with the given name modeled by random.choice(seq)."""
        return self.param(name, choice=(seq,), **kwargs)

    def sample(self, name, population, k, **kwargs):
        """Create a new parameter with the given name modeled by random.sample(population, k)."""
        return self.param(name, sample=(population, k), **kwargs)

    def uniform(self, name, a, b, **kwargs):
        """Create a new parameter with the given name modeled by random.uniform(a, b)."""
        return self.param(name, uniform=(a, b), **kwargs)

    def triangular(self, name, low, high, mode, **kwargs):
        """Create a new parameter with the given name modeled by random.triangular(low, high, mode)."""
        return self.param(name, triangular=(low, high, mode), **kwargs)

    def betavariate(self, name, alpha, beta, **kwargs):
        """Create a new parameter with the given name modeled by random.betavariate(alpha, beta)."""
        return self.param(name, betavariate=(alpha, beta), **kwargs)

    def expovariate(self, name, lambd, **kwargs):
        """Create a new parameter with the given name modeled by random.expovariate(lambd)."""
        return self.param(name, expovariate=(lambd,), **kwargs)

    def gammavariate(self, name, alpha, beta, **kwargs):
        """Create a new parameter with the given name modeled by random.gammavariate(alpha, beta)."""
        return self.param(name, gammavariate=(alpha, beta), **kwargs)

    def normalvariate(self, name, mu, sigma, **kwargs):
        """Create a new parameter with the given name modeled by random.gauss(mu, sigma)."""
        return self.param(name, normalvariate=(mu, sigma), **kwargs)

    def lognormvariate(self, name, mu, sigma, **kwargs):
        """Create a new parameter with the given name modeled by random.lognormvariate(mu, sigma)."""
        return self.param(name, lognormvariate=(mu, sigma), **kwargs)

    def vonmisesvariate(self, name, kappa, **kwargs):
        """Create a new parameter with the given name modeled by random.vonmisesvariate(kappa)."""
        return self.param(name, vonmisesvariate=(kappa,), **kwargs)

    def paretovariate(self, name, alpha, **kwargs):
        """Create a new parameter with the given name modeled by random.paretovariate(alpha)."""
        return self.param(name, paretovariate=(alpha,), **kwargs)

    def weibullvariate(self, name, alpha, beta, **kwargs):
        """Create a new parameter with the given name modeled by random.weibullvariate(alpha, beta)."""
        return self.param(name, weibullvariate=(alpha, beta), **kwargs)

# Derived random functions:

    def randint(self, name, a, b, **kwargs):
        """Create a new parameter with the given name modeled by random.randint(a, b)."""
        start, stop = a, b - 1
        return self.randrange(name, start, stop, **kwargs)

    def random(self, name, **kwargs):
        """Create a new parameter with the given name modeled by random.random()."""
        return self.uniform(name, 0, 1, **kwargs)

    def getrandbits(self, name, k, **kwargs):
        """Create a new parameter with the given name modeled by random.getrandbits(k)."""
        stop = 2**k
        return self.randrange(name, stop, **kwargs)

    gauss = normalvariate

    def loguniform(self, name, min_val, max_val, **kwargs):
        """Create a new parameter with the given name modeled by
        math.exp(random.uniform(math.log(min_val), math.log(max_val)))."""
        kwargs = (_coconut.functools.partial(param_processor.modify_kwargs, math.log))(kwargs)
        log_a, log_b = math.log(min_val), math.log(max_val)
        return math.exp(self.uniform(log_a, log_b))

    def randbool(self, name, **kwargs):
        """Create a new boolean parameter with the given name."""
        return self.choice(name, [False, True], **kwargs)

# Array-based random functions:

    def _array_param(self, name, shape, func):
        """Create a new array parameter for the given name and shape with entries from func."""
        if not isinstance(name, Str):
            raise TypeError("name must be string, not {}".format(name))
        arr = np.zeros(shape)
        for indices in itertools.product(*map(range, shape)):
            cell_name = "{}[{}]".format(name, ",".join(map(str, indices)))
            arr[indices] = func(cell_name)
        return arr

    def rand(self, name, *shape, **kwargs):
        """Create a new array parameter for the given name and shape modeled by np.random.rand."""
        return self._array_param(name, shape, lambda cell_name: self.random(cell_name, **kwargs))

    def randn(self, name, *shape, **kwargs):
        """Create a new array parameter for the given name and shape modeled by np.random.randn."""
        return self._array_param(name, shape, lambda cell_name: self.gauss(cell_name, 0, 1, **kwargs))
