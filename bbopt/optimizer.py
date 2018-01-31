#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0xdaf7559e

# Compiled with Coconut version 1.3.1-post_dev14 [Dead Parrot]

"""
The interface into BBopt for a file with black-box parameters.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------



# Imports:

import json
import os.path
import math

from bbopt.backends import backend_registry
from bbopt.params import param_processor
from bbopt.util import Str
from bbopt.util import norm_path
from bbopt.util import json_serialize
from bbopt.util import best_example
from bbopt.constants import data_file_ext

# Optimizer:

class BlackBoxOptimizer(_coconut.object):
    _optimizers_by_file = {}  # all Optimizer instances by file

    def __init__(self, file, json_indent=None):
        if not isinstance(file, Str):
            raise TypeError("file must be a string")
        self._file = norm_path(file)
        if self._file in self._optimizers_by_file:
            raise ValueError("BlackBoxOptimizer for file %r already exists" % self.file)
        self._optimizers_by_file[self._file] = self
        self._json_indent = json_indent
        self.reload()

    def reload(self):
        """Completely reload the optimizer."""
        self._old_params = {}
        self._examples = []
        self._load_examples()
        self.run(None)  # use serving backend

    def run(self, backend, **kwargs):
        """Optimize parameters using the given backend."""
        self._backend = backend_registry.init_backend(backend, self._examples, self._old_params, **kwargs)
        self._new_params = {}
        self._current_example = {"values": {}}

    @property
    def _got_reward(self):
        return "loss" in self._current_example or "gain" in self._current_example

    def param(self, name, **kwargs):
        """Create a black box parameter and return its value."""
        if self._got_reward:
            raise ValueError("param calls must come before maximize/minimize")
        if not isinstance(name, Str):
            raise TypeError("name must be a string")
        if name in self._new_params:
            raise ValueError("parameter of name %r already exists" % name)
        kwargs = (param_processor.standardize_kwargs)(kwargs)
        value = (json_serialize)(self._backend.param(name, **kwargs))
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
        if callable(value):
            value = value()
        self._current_example[reward_type] = value
        if not self.is_serving:
            self._save_examples()

    @property
    def _data_file(self):
        return os.path.splitext(self._file)[0] + data_file_ext

    def _load_examples(self):
        """Load example data."""
        if os.path.exists(self._data_file):
            with open(self._data_file, "r") as df:
                contents = df.read()
                if contents:
                    _coconut_match_check = False
                    _coconut_match_to = json.loads(contents)
                    _coconut_sentinel = _coconut.object()
                    if (_coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping)) and (_coconut.len(_coconut_match_to) == 2):
                        _coconut_match_temp_0 = _coconut_match_to.get("params", _coconut_sentinel)
                        _coconut_match_temp_1 = _coconut_match_to.get("examples", _coconut_sentinel)
                        if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                            params = _coconut_match_temp_0
                            examples = _coconut_match_temp_1
                            _coconut_match_check = True
                    if not _coconut_match_check:
                        _coconut_match_err = _coconut_MatchError("pattern-matching failed for " '\'{"params": params, "examples": examples} = json.loads(contents)\'' " in " + _coconut.repr(_coconut.repr(_coconut_match_to)))
                        _coconut_match_err.pattern = '{"params": params, "examples": examples} = json.loads(contents)'
                        _coconut_match_err.value = _coconut_match_to
                        raise _coconut_match_err

                    self._old_params = params
                    self._examples = examples

    def get_data(self):
        self._old_params.update(self._new_params)
        return {"params": self._old_params, "examples": self._examples}

    def _save_examples(self):
        """Save example data."""
        self._load_examples()
        if self._current_example not in self._examples:
            self._examples.append(self._current_example)
        with open(self._data_file, "w+") as df:
            (df.write)((str)(json.dumps(self.get_data(), indent=self._json_indent)))

    def get_current_run(self):
        """Return a dictionary containing the current parameters and reward."""
        try:
            return self._current_example
        except AttributeError:
            raise ValueError("get_current_run calls must come after run")

    def get_optimal_run(self):
        """Return a dictionary containing the optimal parameters and reward computed so far."""
        return best_example(self._examples)

# Base Random Functions:

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

# Derived Random Functions:

    def randint(self, name, a, b, **kwargs):
        """Create a new parameter with the given name modeled by random.randint(a, b)."""
        start, stop = a, b - 1
        return self.param(name, randrange=(start, stop), **kwargs)

    def random(self, name, **kwargs):
        """Create a new parameter with the given name modeled by random.random()."""
        return self.param(name, uniform=(0, 1), **kwargs)

    def getrandbits(self, name, k, **kwargs):
        """Create a new parameter with the given name modeled by random.getrandbits(k)."""
        stop = 2**k
        return self.param(name, randrange=(stop,), **kwargs)

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
