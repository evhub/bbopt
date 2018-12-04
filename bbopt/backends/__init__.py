#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x24d7d518

# Compiled with Coconut version 1.4.0-post_dev3 [Ernest Scribbler]

"""
Backends contains all of bbopt's different backends.
"""

# Coconut Header: -------------------------------------------------------------

from __future__ import print_function, absolute_import, unicode_literals, division
import sys as _coconut_sys, os.path as _coconut_os_path
_coconut_file_path = _coconut_os_path.dirname(_coconut_os_path.abspath(__file__))
_coconut_cached_module = _coconut_sys.modules.get(str("__coconut__"))
if _coconut_cached_module is not None and _coconut_os_path.dirname(_coconut_cached_module.__file__) != _coconut_file_path:
    del _coconut_sys.modules[str("__coconut__")]
_coconut_sys.path.insert(0, _coconut_file_path)
from __coconut__ import _coconut, _coconut_NamedTuple, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_pipe, _coconut_star_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error
from __coconut__ import *
_coconut_sys.path.remove(_coconut_file_path)

# Compiled Coconut: -----------------------------------------------------------




class BackendRegistry(_coconut.object):
    def _coconut_lambda_0(_=None):
        from bbopt.backends.serving import ServingBackend
        return ServingBackend
    def _coconut_lambda_1(_=None):
        from bbopt.backends.random import RandomBackend
        return RandomBackend
    def _coconut_lambda_2(_=None):
        from bbopt.backends.skopt import SkoptBackend
        return SkoptBackend
    def _coconut_lambda_3(_=None):
        from bbopt.backends.hyperopt import HyperoptBackend
        return HyperoptBackend
    backend_generators = {None: (_coconut_lambda_0), "random": (_coconut_lambda_1), "scikit-optimize": (_coconut_lambda_2), "hyperopt": (_coconut_lambda_3)}
    registered_backends = {}

    def __getitem__(self, name):
        _coconut_match_to = self.registered_backends
        _coconut_match_check = False
        _coconut_sentinel = _coconut.object()
        if _coconut.isinstance(_coconut_match_to, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                backend = _coconut_match_temp_0
                _coconut_match_check = True
        if _coconut_match_check:
            return self.registered_backends[name]
        else:
            if name in self.backend_generators:
                backend = self.backend_generators[name]()
                del self.backend_generators[name]
                self.registered_backends[name] = backend
                return backend
            else:
                raise ValueError("unknown backend {}".format(name))

    def __iter__(self):
        _coconut_yield_from = backend_generators
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item

        _coconut_yield_from = registered_backends
        for _coconut_yield_item in _coconut_yield_from:
            yield _coconut_yield_item


    def register_backend(self, name, backend):
        """Register a new backend under the given name."""
        self.registered_backends[name] = backend

    def init_backend(self, name, examples, params, **kwargs):
        """Create a backend object of the given name with the given data."""
        return self[name](examples, params, **kwargs)


backend_registry = BackendRegistry()
