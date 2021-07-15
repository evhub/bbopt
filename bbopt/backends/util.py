#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __coconut_hash__ = 0x779c92c1

# Compiled with Coconut version 1.5.0-post_dev75 [Fish License]

"""
Utilities for use in BBopt backends.
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
                _coconut_v_type = type(_coconut_v)
                if getattr(_coconut_v_type, "__module__", None) == str("__coconut__"):
                    _coconut_v_type.__module__ = _coconut_full_module_name
    _coconut_sys.modules[_coconut_full_module_name] = _coconut__coconut__
from __coconut__ import *
from __coconut__ import _coconut_call_set_names, _coconut, _coconut_MatchError, _coconut_igetitem, _coconut_base_compose, _coconut_forward_compose, _coconut_back_compose, _coconut_forward_star_compose, _coconut_back_star_compose, _coconut_forward_dubstar_compose, _coconut_back_dubstar_compose, _coconut_pipe, _coconut_star_pipe, _coconut_dubstar_pipe, _coconut_back_pipe, _coconut_back_star_pipe, _coconut_back_dubstar_pipe, _coconut_none_pipe, _coconut_none_star_pipe, _coconut_none_dubstar_pipe, _coconut_bool_and, _coconut_bool_or, _coconut_none_coalesce, _coconut_minus, _coconut_map, _coconut_partial, _coconut_get_function_match_error, _coconut_base_pattern_func, _coconut_addpattern, _coconut_sentinel, _coconut_assert, _coconut_mark_as_match, _coconut_reiterable
_coconut_sys.path.pop(0)

# Compiled Coconut: -----------------------------------------------------------



import random

if _coconut_sys.version_info < (3, 3):
    from collections import Iterable
else:
    from collections.abc import Iterable

from bbopt import constants
from bbopt.params import param_processor
from bbopt.util import sorted_items
from bbopt.util import convert_match_errors
from bbopt.util import DictProxy
from bbopt.util import ListProxy
from bbopt.util import mean
from bbopt.registry import backend_registry
from bbopt.registry import alg_registry
from bbopt.registry import meta_registry


# Utilities:

@convert_match_errors
@_coconut_mark_as_match
def _init_backend(*_coconut_match_args, **_coconut_match_kwargs):
    """Create a backend object with the given data (backend can be backend name or class)."""
    _coconut_match_check_0 = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "backend_cls" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "params" in _coconut_match_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("backend_cls")
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("examples")
        _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("params")
        args = _coconut_match_args[3:]
        _coconut_match_temp_3 = _coconut_match_kwargs.pop("_attempt_to_update_backend") if "_attempt_to_update_backend" in _coconut_match_kwargs else None
        _coconut_match_temp_4 = _coconut_match_kwargs.pop("_on_new_backend") if "_on_new_backend" in _coconut_match_kwargs else None
        backend_cls = _coconut_match_temp_0
        examples = _coconut_match_temp_1
        params = _coconut_match_temp_2
        _attempt_to_update_backend = _coconut_match_temp_3
        _on_new_backend = _coconut_match_temp_4
        options = _coconut_match_kwargs
        _coconut_match_check_0 = True
    if not _coconut_match_check_0:
        raise _coconut_FunctionMatchError('match def _init_backend(backend_cls, examples, params, *args, _attempt_to_update_backend=None, _on_new_backend=None, **options):', _coconut_match_args)

    backend_examples = examples[:]
    backend_params = params.copy()

    new_backend = None
    if isinstance(_attempt_to_update_backend, backend_cls):
        updated_backend = _attempt_to_update_backend.attempt_update(backend_examples, backend_params, *args, **options)
        if updated_backend is True:
            new_backend = _attempt_to_update_backend
        elif isinstance(updated_backend, backend_cls):
            new_backend = updated_backend
        else:
            assert updated_backend is False, "invalid {_coconut_format_0}.attempt_update return value: {_coconut_format_1}".format(_coconut_format_0=(backend_cls), _coconut_format_1=(updated_backend))

    if new_backend is None:
        assert not _attempt_to_update_backend or isinstance(_attempt_to_update_backend, Backend), "invalid backend to attempt update on: {_coconut_format_0}".format(_coconut_format_0=(_attempt_to_update_backend))
        new_backend = backend_cls(backend_examples, backend_params, *args, **options)
        if _on_new_backend is not None:
            _on_new_backend(new_backend)

    return new_backend


def _make_safe_backend_store(backend_store, remove_backends):
    """Get a new backend_store without the given remove_backends."""
    safe_backend_store = DictProxy(old_dict=backend_store, new_dict=backend_store.copy())
    for backend_cls in backend_store:
        if any((isinstance(rem_backend, backend_cls) for rem_backend in remove_backends)):
            safe_specific_backends = []
            for stored_args, stored_options, stored_backend in backend_store[backend_cls]:
                if stored_backend not in remove_backends:
                    safe_specific_backends.append((stored_args, stored_options, stored_backend))
            safe_backend_store[backend_cls] = ListProxy(old_list=backend_store[backend_cls], new_list=safe_specific_backends)
    return safe_backend_store


@_coconut_mark_as_match
def get_backend(*_coconut_match_args, **_coconut_match_kwargs):
    """Create a backend object, attempting to update a backend from backend_store."""
    _coconut_match_check_1 = False
    _coconut_FunctionMatchError = _coconut_get_function_match_error()
    if (_coconut.sum((_coconut.len(_coconut_match_args) > 0, "backend_store" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 1, "backend" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 2, "examples" in _coconut_match_kwargs)) == 1) and (_coconut.sum((_coconut.len(_coconut_match_args) > 3, "params" in _coconut_match_kwargs)) == 1):
        _coconut_match_temp_0 = _coconut_match_args[0] if _coconut.len(_coconut_match_args) > 0 else _coconut_match_kwargs.pop("backend_store")
        _coconut_match_temp_1 = _coconut_match_args[1] if _coconut.len(_coconut_match_args) > 1 else _coconut_match_kwargs.pop("backend")
        _coconut_match_temp_2 = _coconut_match_args[2] if _coconut.len(_coconut_match_args) > 2 else _coconut_match_kwargs.pop("examples")
        _coconut_match_temp_3 = _coconut_match_args[3] if _coconut.len(_coconut_match_args) > 3 else _coconut_match_kwargs.pop("params")
        args = _coconut_match_args[4:]
        _coconut_match_temp_4 = _coconut_match_kwargs.pop("_current_backend") if "_current_backend" in _coconut_match_kwargs else None
        _coconut_match_temp_5 = _coconut_match_kwargs.pop("_on_new_backend") if "_on_new_backend" in _coconut_match_kwargs else None
        backend_store = _coconut_match_temp_0
        backend = _coconut_match_temp_1
        examples = _coconut_match_temp_2
        params = _coconut_match_temp_3
        _current_backend = _coconut_match_temp_4
        _on_new_backend = _coconut_match_temp_5
        options = _coconut_match_kwargs
        _coconut_match_check_1 = True
    if not _coconut_match_check_1:
        raise _coconut_FunctionMatchError('match def get_backend(backend_store, backend, examples, params, *args, _current_backend=None, _on_new_backend=None, **options):', _coconut_match_args)

    if isinstance(backend, type) and issubclass(backend, Backend):
        backend_cls = backend
    else:
        backend_cls = backend_registry[backend]
        assert issubclass(backend_cls, Backend), "invalid backend class for {_coconut_format_0}: {_coconut_format_1}".format(_coconut_format_0=(backend), _coconut_format_1=(backend_cls))

    store_ind = None
    attempt_to_update_backend = _current_backend
    for i, (stored_args, stored_options, stored_backend) in enumerate(backend_store[backend_cls]):
        attempt_to_update_backend = stored_backend
        if stored_args == args and stored_options == options:
            store_ind = i
            break

    if backend_cls.request_backend_store:
        init_options = options.copy()
        init_options["_backend_store"] = _make_safe_backend_store(backend_store, (attempt_to_update_backend,))
    else:
        init_options = options

    new_backend = _init_backend(backend_cls, examples, params, *args, _attempt_to_update_backend=attempt_to_update_backend, _on_new_backend=_on_new_backend, **init_options)

    if store_ind is None:
        backend_store[backend_cls].append((args, options, new_backend))
    else:
        backend_store[backend_cls][store_ind] = (args, options, new_backend)

    return new_backend


def negate_objective(objective):
    """Take the negative of the given objective (converts a gain into a loss and vice versa)."""
    if isinstance(objective, Iterable):
        return (list)((map)(negate_objective, objective))
    else:
        return -objective


def get_names_and_features(values, params, fallback_func=param_processor.choose_default_placeholder, converters={}, convert_fallback=True,):
    """Return an iterator of (name, feature) for the parameters in sorted order with the given fallback function.
    If passed, converters must map funcs to functions from (value, *args) -> new_value which will be run
    on the resulting value for that func (but only on fallbacks if convert_fallback)."""
    for name, (func, args, kwargs) in sorted_items(params):
# determine feature
        fallback = False
        _coconut_match_to_1 = values
        _coconut_match_check_3 = False
        if _coconut.isinstance(_coconut_match_to_1, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to_1.get(name, _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                feature = _coconut_match_temp_0
                _coconut_match_check_3 = True
        if _coconut_match_check_3:
            pass
        else:
            _coconut_match_to_0 = kwargs
            _coconut_match_check_2 = False
            if _coconut.isinstance(_coconut_match_to_0, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to_0.get("placeholder_when_missing", _coconut_sentinel)
                if _coconut_match_temp_0 is not _coconut_sentinel:
                    placeholder_value = _coconut_match_temp_0
                    _coconut_match_check_2 = True
            if _coconut_match_check_2:
                feature = placeholder_value
            else:
                fallback = True
                feature = fallback_func(name, func, *args, **kwargs)

# run converters
        if not fallback or convert_fallback:
            _coconut_match_to_2 = converters
            _coconut_match_check_4 = False
            if _coconut.isinstance(_coconut_match_to_2, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_match_to_2.get(func, _coconut_sentinel)
                if _coconut_match_temp_0 is not _coconut_sentinel:
                    converter_func = _coconut_match_temp_0
                    _coconut_match_check_4 = True
            if _coconut_match_check_4:
                feature = converter_func(feature, *args)

        yield name, feature


def make_features(*args, **kwargs):
    """Same as get_names_and_features but just yields the features."""
    _coconut_yield_from_1 = _coconut.iter((starmap)(lambda name, feature: feature, get_names_and_features(*args, **kwargs)))
    while True:
        try:
            yield _coconut.next(_coconut_yield_from_1)
        except _coconut.StopIteration as _coconut_yield_err_0:
            _coconut_yield_from_0 = _coconut_yield_err_0.args[0] if _coconut.len(_coconut_yield_err_0.args) > 0 else None
            break

    _coconut_yield_from_0


def split_examples(examples, params, fallback_func=param_processor.choose_default_placeholder, converters={}, convert_fallback=True,):
    """Split examples into a list of data points and a list of losses with the given fallback function."""
    data_points, losses = [], []
    for example in examples:

# extract values, loss
        _coconut_case_match_to_0 = example
        _coconut_case_match_check_0 = False
        if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_case_match_to_0.get("values", _coconut_sentinel)
            _coconut_match_temp_1 = _coconut_case_match_to_0.get("gain", _coconut_sentinel)
            if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                values = _coconut_match_temp_0
                gain = _coconut_match_temp_1
                _coconut_case_match_check_0 = True
        if _coconut_case_match_check_0:
            loss = negate_objective(gain)
        if not _coconut_case_match_check_0:
            if _coconut.isinstance(_coconut_case_match_to_0, _coconut.abc.Mapping):
                _coconut_match_temp_0 = _coconut_case_match_to_0.get("values", _coconut_sentinel)
                _coconut_match_temp_1 = _coconut_case_match_to_0.get("loss", _coconut_sentinel)
                if (_coconut_match_temp_0 is not _coconut_sentinel) and (_coconut_match_temp_1 is not _coconut_sentinel):
                    values = _coconut_match_temp_0
                    loss = _coconut_match_temp_1
                    _coconut_case_match_check_0 = True
            if _coconut_case_match_check_0:
                pass
        if not _coconut_case_match_check_0:
            raise ValueError("invalid example {_coconut_format_0}".format(_coconut_format_0=(example)))

# extract features
        features = (list)(make_features(values, params, fallback_func, converters, convert_fallback))

# add to data_points, losses
        (data_points.append)(features)
        (losses.append)(loss)

    return data_points, losses


def get_named_data_points_and_losses(examples, params, *args, **kwargs):
    """Same as split_examples but returns named_data_points instead of data_points."""
    data_points, losses = split_examples(examples, params, *args, **kwargs)
    named_data_points = []
    sorted_names = list(sorted(params))
    for point in data_points:
        pt_val = {}
        for name, item in zip(sorted_names, point):
            pt_val[name] = item
        named_data_points.append(pt_val)
    return named_data_points, losses


def marginalize(named_data_points, losses, param_name, ave_func=mean):
    """Get an average loss for each prior value of param_name."""
    losses_for_vals = []  # we can't use a dict since vals might not be hashable
    for point, loss in zip(named_data_points, losses):
        val = point[param_name]
        for check_val, check_losses in losses_for_vals:
            if check_val == val:
                check_losses.append(loss)
                break
        else:  # no break
            losses_for_vals.append((val, [loss]))

    marginals = []
    for val, all_losses in losses_for_vals:
        marginals.append((val, ave_func(all_losses)))
    return marginals


def get_cum_probs_for(distribution):
    """Generate cumulative probabilities from the given distribution."""
    cum_probs = []
    total_weight = sum((weight for elem, weight in distribution))
    prev_cutoff = 0
    for elem, weight in distribution:
        if weight == float("inf"):
            cutoff = 1
        elif weight in (float("-inf"), float("nan")) or total_weight == float("nan"):
            cutoff = prev_cutoff
        else:
            cutoff = prev_cutoff + weight / total_weight
        cum_probs.append((elem, cutoff))
        prev_cutoff = cutoff
    return cum_probs


def random_from_cum_probs(cum_probs):
    """Randomly choose an element using cum_probs."""
    rand_val = random.random()
    for elem, cutoff in cum_probs:
        if rand_val <= cutoff:
            return elem
    return None


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
    _coconut_match_to_4 = serving_values
    _coconut_match_check_6 = False
    if _coconut.isinstance(_coconut_match_to_4, _coconut.abc.Mapping):
        _coconut_match_temp_0 = _coconut_match_to_4.get(name, _coconut_sentinel)
        if _coconut_match_temp_0 is not _coconut_sentinel:
            value = _coconut_match_temp_0
            _coconut_match_check_6 = True
    if _coconut_match_check_6:
        return value
    else:
        _coconut_match_to_3 = kwargs
        _coconut_match_check_5 = False
        if _coconut.isinstance(_coconut_match_to_3, _coconut.abc.Mapping):
            _coconut_match_temp_0 = _coconut_match_to_3.get("guess", _coconut_sentinel)
            if _coconut_match_temp_0 is not _coconut_sentinel:
                guess = _coconut_match_temp_0
                _coconut_match_check_5 = True
        if _coconut_match_check_5:
            return guess
        else:
            return fallback_func(name, func, *args, **kwargs)


# Backend base classes:

class Backend(_coconut.object):
    """Base class for all BBopt backends."""
# derived classes should always set this
    backend_name = None

# derived classes can modify these if they want to further
#  restrict the set of supported funcs and/or kwargs
    implemented_funcs = None
    supported_kwargs = ("guess", "placeholder_when_missing",)

# derived classes must set this on each run if they want to
#  use the default param implementation
    current_values = None

# derived classes must set this if they want to use the
#  default fallback_func implementation
    fallback_backend = None

# derived classes can implement tell_examples(new_examples)
#  to allow fast updating on new data
    tell_examples = None

# derived classes can set this to True to have a _backend_store keyword
#  argument passed to __init__ with an object usable in get_backend
    request_backend_store = False

    def __new__(cls, examples=None, params=None, *args, **kwargs):
        self = super(Backend, cls).__new__(cls)
        if self.tell_examples is not None:
            self._examples = []
            self._params = params
            self._args = args
            self._kwargs = kwargs
        return self

    def __init__(self, examples=None, params=None, *args, **kwargs):
        """Just call attempt_update by default."""
        result = self.attempt_update(examples, params, *args, **kwargs)
        assert result, "Backend.__init__: {_coconut_format_0}.attempt_update(*{_coconut_format_1}, **{_coconut_format_2}) failed with result {_coconut_format_3!r}".format(_coconut_format_0=(self.__class__.__name__), _coconut_format_1=(args), _coconut_format_2=(kwargs), _coconut_format_3=(result))

    def attempt_update(self, examples=None, params=None, *args, **kwargs):
        """Attempt to update this backend with new arguments. False indicates that the
        update failed while True indicates a successful update."""
        if (self.tell_examples is None or not self._params or params != self._params or args != self._args or kwargs != self._kwargs):
            return False
        old_examples, new_examples = examples[:len(self._examples)], examples[len(self._examples):]
        if old_examples != self._examples:
            return False
        if new_examples:
            try:
                self.tell_examples(new_examples)
            except NotImplementedError:
                return False
        self._examples = examples
        return True

    def init_fallback_backend(self):
        """Set fallback_backend to a new random backend instance."""
        self.fallback_backend = backend_registry[constants.default_fallback_backend]()

    def fallback_func(self, name, func, *args, **kwargs):
        """Default fallback_func calls self.fallback_backend.param."""
        assert self.fallback_backend is not None, "Backend subclasses using Backend.fallback_func must set fallback_backend"
        return self.fallback_backend.param(name, func, *args, **kwargs)

    def param(self, name, func, *args, **kwargs):
        """Default param calls serve_values with self.current_values and self.fallback_func."""
        assert self.current_values is not None, "Backend subclasses using Backend.param must set current_values"
        return serve_values(name, func, args, kwargs, serving_values=self.current_values, fallback_func=self.fallback_func, backend_name=self.backend_name, implemented_funcs=self.implemented_funcs, supported_kwargs=self.supported_kwargs)

    registered_algs = None

    @classmethod
    def register(cls):
        """Register this backend to the backend registry."""
        assert cls.backend_name is not None, "Backend subclasses using Backend.register must set backend_name on the class"
        backend_registry.register(cls.backend_name, cls)

# clear out registered_algs when register is called, since that
#  probably indicates a subclass is trying to register new algs
        cls.registered_algs = []

    @classmethod
    def register_alias(cls, alias):
        """Register an alias for this backend."""
        assert cls.backend_name is not None, "Backend subclasses using Backend.register_alias must set backend_name on the class"
        backend_registry.register_alias(cls.backend_name, alias)

    @classmethod
    def register_alg(cls, alg_name, **options):
        """Register an algorithm under the given name that calls this backend with the given options."""
        assert cls.backend_name is not None, "Backend subclasses using Backend.register_alg must set backend_name on the class"
        alg_registry.register(alg_name, (cls.backend_name, options))

        assert cls.registered_algs is not None, "Backend.register_alg must come after Backend.register"
        cls.registered_algs.append(alg_name)

    @classmethod
    def register_meta_for_all_algs(cls, alg_name, meta_alg=None):
        """Register a meta algorithm for all the algs registered on this class."""
        assert cls.registered_algs is not None, "register_meta_for_all_algs requires prior register_alg calls"
        cls.register_meta(alg_name, cls.registered_algs, meta_alg)

    @staticmethod
    def register_meta(alg_name, algs, meta_alg=constants.default_alg_sentinel):
        """Register an algorithm that defers to run_meta."""
        meta_registry.register(alg_name, (algs, meta_alg))

    @staticmethod
    def register_param_func(func_name, handler, placeholder_generator, support_check_func):
        """Register a new parameter definition function. See bbopt.params for examples."""
        param_processor.register(func_name, handler, placeholder_generator, support_check_func)


_coconut_call_set_names(Backend)
class StandardBackend(Backend):
    """Base class for standard BBopt backends."""

    def __init__(self, examples, params, *args, **kwargs):
        """Implement __init__ using setup_backend and tell_examples."""
        self.init_fallback_backend()

        if not params:
            self.current_values = {}
            return

        self.setup_backend(params, *args, **kwargs)

        if examples:
            self.tell_examples(examples)
        else:
            self.current_values = {}

    @override
    def tell_examples(self, new_examples):
        """Implements tell_examples by calling tell_data."""
        new_data, new_losses = get_named_data_points_and_losses(new_examples, self._params)
        self.tell_data(new_data, new_losses)
        self.current_values = self.get_next_values()

    def setup_backend(self, params, *args, **kwargs):
        """Override setup_backend with any setup work that needs to be done."""
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.__init__ must define a setup_backend(params, *args, **kwargs) method")

    def tell_data(self, new_data, new_losses):
        """Override tell_data with any work that needs to be done to add the given data and losses."""
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.tell_examples must define a tell_data(new_data, new_losses) method")

    def get_next_values(self):
        """Override get_next_values to produce the next set of values that should be evaluated."""
        raise NotImplementedError("StandardBackend subclasses using StandardBackend.tell_examples must define a get_next_values() method")

_coconut_call_set_names(StandardBackend)
