# BBopt

[![Join the chat at https://gitter.im/evhub/bbopt](https://badges.gitter.im/evhub/bbopt.svg)](https://gitter.im/evhub/bbopt?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![DOI](https://zenodo.org/badge/102327504.svg)](https://zenodo.org/badge/latestdoi/102327504)

BBopt aims to provide the easiest hyperparameter optimization you'll ever do. Think of BBopt like [Keras](https://keras.io/) for black box optimization: one universal interface for working with any black box optimization backend.

BBopt's features include:
- a universal API for defining your tunable parameters based on the standard library [`random`](https://docs.python.org/3.4/library/random.html) module (so you don't even have to learn anything new!),
- tons of state-of-the-art black box optimization algorithms such as Gaussian Processes from [`scikit-optimize`](https://scikit-optimize.github.io/) or Tree Structured Parzen Estimation from [`hyperopt`](http://hyperopt.github.io/hyperopt/) for tuning parameters,
- the ability to switch algorithms (even across different backends!) while retaining all previous trials,
- multiprocessing-safe data saving to enable running multiple trials in parallel,
- lots of data visualization methods, including support for everything in [`skopt.plots`](https://scikit-optimize.github.io/plots.m.html),
- support for optimizing over conditional parameters that only appear during some runs,
- support for all major Python versions (`2.7` or `3.4+`), and
- a straightforward interface for [extending BBopt with your own custom algorithms](#writing-your-own-backend).

Once you've defined your parameters, training a black box optimization model on those parameters is as simple as
```
bbopt your_file.py
```
and serving your file with optimized parameters as easy as
```python
import your_file
```

_Questions? Head over to [BBopt's Gitter](https://gitter.im/evhub/bbopt) if you have any questions/comments/etc. regarding BBopt._

## Installation

To get going with BBopt, simply install it with
```
pip install bbopt
```
or, to also install the extra dependencies necessary for running BBopt's examples, run `pip install bbopt[examples]`.

## Basic Usage

To use bbopt, just add
```python
# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run()
```
to the top of your file, then call
```python
x = bb.uniform("x", 0, 1)
```
for each of the tunable parameters in your model, and finally add
```python
bb.maximize(y)      or      bb.minimize(y)
```
to set the value being optimized. Then, run
```
bbopt <your file here> -n <number of trials> -j <number of processes>
```
to train your model, and just
```
import <your module here>
```
to serve it!

## Examples

Some examples of BBopt in action:

- [`random_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/random_example.py): Extremely basic example using the `random` backend.
- [`skopt_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/skopt_example.py): Slightly more complex example making use of the `gaussian_process` algorithm from the `scikit-optimize` backend.
- [`hyperopt_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/hyperopt_example.py): Example showcasing the `tree_structured_parzen_estimator` algorithm from the `hyperopt` backend.
- [`numpy_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/numpy_example.py): Example which showcases how to have numpy array parameters.
- [`conditional_skopt_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/conditional_skopt_example.py): Example of having black box parameters that are dependent on other black box parameters using the `gaussian_process` algorithm from the `scikit-optimize` backend.
- [`conditional_hyperopt_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/conditional_hyperopt_example.py): Example of doing conditional parameters with the `tree_structured_parzen_estimator` algorithm from the `hyperopt` backend.
- [`keras_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/keras_example.py): Complete example of using BBopt to optimize a neural network built with [Keras](https://keras.io/). Uses the full API to implement its own optimization loop and thus avoid the overhead of running the entire file multiple times.
- [`mixture_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/mixture_example.py): Example of using the `mixture` backend to randomly switch between different algorithms.
- [`json_example.py`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/json_example.py): Example of using `json` instead of `pickle` to save parameters.

## Full API

<!-- MarkdownTOC -->

1. [Command-Line Interface](#command-line-interface)
1. [Black Box Optimization Methods](#black-box-optimization-methods)
    1. [Constructor](#constructor)
    1. [`run`](#run)
    1. [`algs`](#algs)
    1. [`run_backend`](#run_backend)
    1. [`minimize`](#minimize)
    1. [`maximize`](#maximize)
    1. [`remember`](#remember)
    1. [`plot_convergence`](#plot_convergence)
    1. [`plot_history`](#plot_history)
    1. [`partial_dependence`](#partial_dependence)
    1. [`plot_partial_dependence_1D`](#plot_partial_dependence_1d)
    1. [`plot_evaluations`](#plot_evaluations)
    1. [`plot_objective`](#plot_objective)
    1. [`get_current_run`](#get_current_run)
    1. [`get_optimal_run`](#get_optimal_run)
    1. [`get_data`](#get_data)
    1. [`data_file`](#data_file)
    1. [`tell_examples`](#tell_examples)
    1. [`backend`](#backend)
1. [Parameter Definition Methods](#parameter-definition-methods)
    1. [`randrange`](#randrange)
    1. [`randint`](#randint)
    1. [`getrandbits`](#getrandbits)
    1. [`choice`](#choice)
    1. [`randbool`](#randbool)
    1. [`sample`](#sample)
    1. [`shuffled`](#shuffled)
    1. [`random`](#random)
    1. [`uniform`](#uniform)
    1. [`loguniform`](#loguniform)
    1. [`normalvariate`](#normalvariate)
    1. [`lognormvariate`](#lognormvariate)
    1. [`rand`](#rand)
    1. [`randn`](#randn)
1. [Writing Your Own Backend](#writing-your-own-backend)

<!-- /MarkdownTOC -->

### Command-Line Interface

The `bbopt` command is extremely simple in terms of what it actually does. For the command `bbopt <file> -n <trials> -j <processes>`, BBopt simply runs `python <file>` a number of times equal to `<trials>`, split across `<processes>` different processes.

Why does this work? If you're using the basic boilerplate, then running `python <file>` will trigger the `if __name__ == "__main__":` clause, which will run a training episode. But when you go to `import` your file, the `if __name__ == "__main__":` clause won't get triggered, and you'll just get served the best parameters found so far. Since the command-line interface is so simple, advanced users who want to use the full API instead of the boilerplate need not use the `bbopt` command at all. If you want more information on the `bbopt` command, just run `bbopt -h`.

### Black Box Optimization Methods

#### Constructor

**BlackBoxOptimizer**(_file_, _protocol_=`None`)

Create a new `bb` object; this should be done at the beginning of your program as all the other functions are methods of this object.

_file_ is used by BBopt to figure out where to load and save data to, and should usually just be set to `__file__` (BBopt uses `os.path.splitext(file)[0]` as the base path for the data file).

_protocol_ determines how BBopt serializes data. If `None` (the default), BBopt will use pickle protocol 2, which is the highest version that works on both Python 2 and Python 3 (unless a `json` file is present, in which case BBopt will use `json`). To use the newest protocol instead, pass `protocol=-1`. If `protocol="json"`, BBopt will use `json` instead of `pickle`, which is occasionally useful for cross-platform compatibility.

#### `run`

BlackBoxOptimizer.**run**(_alg_=`"tree_structured_parzen_estimator"`)

Start optimizing using the given black box optimization algorithm. Use **algs** to get the valid values for _alg_.

If this method is never called, or called with `alg=None`, BBopt will just serve the best parameters found so far, which is how the basic boilerplate works. Note that, if no saved parameter data is found, and a _guess_ is present, BBopt will use that, which is a good way of distributing your parameter values without including all your saved parameter data.

#### `algs`

BlackBoxOptimizer.**algs**

A dictionary mapping the valid algorithms for use in **run** to the pair `(backend, kwargs)` of the backend and arguments to that backend that the algorithm corresponds to.

Supported algorithms are:
- `"serving"` (or `None`) (`serving` backend),
- `"random"` (`random` backend),
- `"tree_structured_parzen_estimator"` (`hyperopt` backend) (the default),
- `"annealing"` (`hyperopt` backend),
- `"gaussian_process"` (`scikit-optimize` backend),
- `"random_forest"` (`scikit-optimize` backend),
- `"extra_trees"` (`scikit-optimize` backend), and
- `"gradient_boosted_regression_trees"` (`scikit-optimize` backend).

#### `run_backend`

BlackBoxOptimizer.**run_backend**(_backend_, *_args_, **_kwargs_)

The base function behind **run**. Instead of specifying an algorithm, **run_backend** lets you specify the specific backend you want to call and the parameters you want to call it with. Different backends do different things with the remaining arguments:

- `scikit-optimize` passes the arguments to [`skopt.Optimizer`](https://scikit-optimize.github.io/#skopt.Optimizer),
- `hyperopt` passes the arguments to [`fmin`](https://github.com/hyperopt/hyperopt/wiki/FMin), and
- `mixture` expects a `distribution` argument to specify the mixture of different algorithms to use, specifically a list of `(alg, weight)` tuples.

#### `minimize`

BlackBoxOptimizer.**minimize**(_value_)

Finish optimizing and set the loss for this run to _value_. To start another run, call **run** again.

#### `maximize`

BlackBoxOptimizer.**maximize**(_value_)

Same as **minimize** but sets the gain instead of the loss.

#### `remember`

BlackBoxOptimizer.**remember**(_info_)

Update the current run's `"memo"` field with the given _info_ dictionary. Useful for saving information about a run that shouldn't actually impact optimization but that you would like to have access to later (using **get_optimal_run**, for example).

#### `plot_convergence`

BlackBoxOptimizer.**plot_convergence**(_ax_=`None`, _yscale_=`None`)

Plot the running best gain/loss over the course of all previous trials. If passed, `ax` should be the [matplotlib axis](https://matplotlib.org/api/axes_api.html) to plot on and `yscale` should be the scale for the y axis.

Run BBopt's [`keras` example](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/keras_example.py) to generate an example plot.

#### `plot_history`

BlackBoxOptimizer.**plot_history**(_ax_=`None`, _yscale_=`None`)

Plot the gain/loss at each point over the course of all previous trials. If passed, `ax` should be the [matplotlib axis](https://matplotlib.org/api/axes_api.html) to plot on and `yscale` should be the scale for the y axis.

Run BBopt's [`keras` example](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/keras_example.py) to generate an example plot.

#### `partial_dependence`

BlackBoxOptimizer.**partial_dependence**(_i\_name_, _j\_name_=`None`, _sample\_points_=`None`, _n\_samples_=`250`, _n\_points_=`40`)

Calls [`skopt.plots.partial_dependence`](https://scikit-optimize.github.io/plots.m.html) using previous trial data. The parameters _i\_name_ and _j\_name_ should be set to names of the parameters you want for the _i_ and _j_ arguments to `skopt.plots.partial_dependence`.

#### `plot_partial_dependence_1D`

BlackBoxOptimizer.**plot_partial_dependence_1D**(_i\_name_, _ax_=`None`, _yscale_=`Non`, _sample\_points_=`None`, _n\_samples_=`250`, _n\_points_=`40`)

Plot the partial dependence of _i\_name_ on the given [matplotlib axis](https://matplotlib.org/api/axes_api.html) `ax` and with the given y axis scale `yscale`. See **partial_dependence** for the meaning of the other parameters.

Run BBopt's [`keras` example](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/keras_example.py) to generate an example plot.

#### `plot_evaluations`

BlackBoxOptimizer.**plot_evaluations**(_bins_=`20`)

Calls [`skopt.plots.plot_evaluations`](https://scikit-optimize.github.io/plots.m.html) using previous trial data.

Run BBopt's [`keras` example](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/keras_example.py) to generate an example plot.

#### `plot_objective`

BlackBoxOptimizer.**plot_objective**(_levels_=`10`, _n\_points_=`40`, _n\_samples_=`250`, _size_=`2`, _zscale_=`"linear"`)

Calls [`skopt.plots.plot_objective`](https://scikit-optimize.github.io/plots.m.html) using previous trial data.

Run BBopt's [`keras` example](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/keras_example.py) to generate an example plot.

#### `get_current_run`

BlackBoxOptimizer.**get_current_run**()

Get information on the current run, including the values of all parameters encountered so far and the loss/gain of the run if specified yet.

#### `get_optimal_run`

BlackBoxOptimizer.**get_optimal_run**()

Get information on the best run so far. These are the parameters that will be used if **run** is not called.

#### `get_data`

BlackBoxOptimizer.**get_data**()

Dump a dictionary containing `"params"`, the parameters BBopt knows about and what random function and arguments they were initialized with, and `"examples"`, all the previous data BBopt has collected.

#### `data_file`

BlackBoxOptimizer.**data_file**

The path of the file where BBopt is saving data to.

#### `tell_examples`

BlackBoxOptimizer.**tell_examples**(_examples_)

Add the given _examples_ as in **get_data** to memory, writing the new data to **data_file**. Must come before **run** if you want the new data to be included in the model for that run.

#### `backend`

BlackBoxOptimizer.**backend**

The backend object being used by the current BlackBoxOptimizer instance.

### Parameter Definition Methods

Every BBopt parameter definition method has the form
```
bb.<random function>(<name>, <args>, **kwargs)
```
where

- the method itself specifies what distribution is being modeled,
- the first argument is always _name_, a unique string identifying that parameter,
- following _name_ are whatever arguments are needed to specify the distribution's parameters, and
- at the end are keyword arguments, which are the same for all the different methods. The supported _kwargs_ are:
    + _guess_, which specifies the initial value for the parameter, and
    + _placeholder\_when\_missing_, which specifies what placeholder value a conditional parameter should be given if missing.

_Important note: Once you bind a name to a parameter you cannot change that parameter's options. Thus, if the options defining your parameters can vary from run to run, you must use a different name for each possible combination._

#### `randrange`

BlackBoxOptimizer.**randrange**(_name_, _stop_, **_kwargs_)

BlackBoxOptimizer.**randrange**(_name_, _start_, _stop_, _step_=`1`, **_kwargs_)

Create a new parameter modeled by [`random.randrange(start, stop, step)`](https://docs.python.org/3/library/random.html#random.randrange), which is equivalent to `random.choice(range(start, stop, step))`, but can be much more efficient.

_Backends which support **randrange**: `scikit-optimize`, `hyperopt`, `random`._

#### `randint`

BlackBoxOptimizer.**randint**(_name_, _a_, _b_, **_kwargs_)

Create a new parameter modeled by [`random.randint(a, b)`](https://docs.python.org/3/library/random.html#random.randint), which is equivalent to `random.randrange(a, b-1)`.

_Backends which support **randint**: `scikit-optimize`, `hyperopt`, `random`._

#### `getrandbits`

BlackBoxOptimizer.**getrandbits**(_name_, _k_, **_kwargs_)

Create a new parameter modeled by [`random.getrandbits(k)`](https://docs.python.org/3/library/random.html#random.getrandbits), which is equivalent to `random.randrange(0, 2**k)`.

_Backends which support **getrandbits**: `scikit-optimize`, `hyperopt`, `random`._

#### `choice`

BlackBoxOptimizer.**choice**(_name_, _seq_, **_kwargs_)

Create a new parameter modeled by [`random.choice(seq)`](https://docs.python.org/3/library/random.html#random.choice), which chooses an element from _seq_.

_Backends which support **choice**: `scikit-optimize`, `hyperopt`, `random`._

#### `randbool`

BlackBoxOptimizer.**randbool**(_name_, **_kwargs_)

Create a new boolean parameter, modeled by the equivalent of `random.choice([True, False])`.

_Backends which support **randbool**: `scikit-optimize`, `hyperopt`, `random`._

#### `sample`

BlackBoxOptimizer.**sample**(_name_, _population_, _k_, **_kwargs_)

Create a new parameter modeled by [`random.sample(population, k)`](https://docs.python.org/3/library/random.html#random.sample), which chooses _k_ elements from _population_.

_Backends which support **sample**: `scikit-optimize`, `hyperopt`, `random`._

#### `shuffled`

BlackBoxOptimizer.**shuffled**(_name_, _population_, **_kwargs_)

Create a new parameter modeled by [`random.shuffle(population)`](https://docs.python.org/3/library/random.html#random.shuffle) except that it returns the shuffled list instead of shuffling it in place.

_Backends which support **shuffled**: `scikit-optimize`, `hyperopt`, `random`._

#### `random`

BlackBoxOptimizer.**random**(_name_, **_kwargs_)

Create a new parameter modeled by [`random.random()`](https://docs.python.org/3/library/random.html#random.random), which is equivalent to `random.uniform(0, 1)`.

_Backends which support **random**: `scikit-optimize`, `hyperopt`, `random`._

#### `uniform`

BlackBoxOptimizer.**uniform**(_name_, _a_, _b_, **_kwargs_)

Create a new parameter modeled by [`random.uniform(a, b)`](https://docs.python.org/3/library/random.html#random.uniform), which uniformly selects a float between _a_ and _b_.

_Backends which support **uniform**: `scikit-optimize`, `hyperopt`, `random`._

#### `loguniform`

BlackBoxOptimizer.**loguniform**(_name_, _min\_val_, _max\_val_, **_kwargs_)

Create a new parameter modeled by
```python
math.exp(random.uniform(math.log(min_val), math.log(max_val)))
```
which logarithmically selects a float between _min\_val_ and _max\_val_.

_Backends which support **loguniform**: `scikit-optimize`, `hyperopt`, `random`._

#### `normalvariate`

BlackBoxOptimizer.**normalvariate**(_name_, _mu_, _sigma_, **_kwargs_)

Create a new parameter modeled by [`random.normalvariate(mu, sigma)`](https://docs.python.org/3/library/random.html#random.normalvariate).

_Backends which support **normalvariate**: `hyperopt`, `random`._

#### `lognormvariate`

BlackBoxOptimizer.**lognormvariate**(_name_, _mu_, _sigma_, **_kwargs_)

Create a new parameter modeled by [`random.lognormvariate(mu, sigma)`](https://docs.python.org/3/library/random.html#random.lognormvariate) such that the natural log is a normal distribution with mean _mu_ and standard deviation _sigma_.

_Backends which support **lognormvariate**: `hyperopt`, `random`._

#### `rand`

BlackBoxOptimizer.**rand**(_name_, *_shape_, **_kwargs_)

Create a new parameter modeled by [`numpy.random.rand(*shape)`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.rand.html#numpy.random.rand), which creates a `numpy` array of the given shape with entries generated uniformly in `[0, 1)`.

_Backends which support **rand**: `scikit-optimize`, `hyperopt`, `random`._

#### `randn`

BlackBoxOptimizer.**randn**(_name_, *_shape_, **_kwargs_)

Create a new parameter modeled by [`numpy.random.randn(*shape)`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.randn.html#numpy-random-randn), which creates a `numpy` array of the given shape with entries generated according to a standard normal distribution.

_Backends which support **randn**: `hyperopt`, `random`._

### Writing Your Own Backend

BBopt's backend system is built to be extremely extensible, allowing anyone to write and register their own BBopt backends. The basic template for writing a BBopt backend is as follows:
```python
from bbopt.backends.util import Backend

class MyBackend(Backend):
    backend_name = "my-backend"
    implemented_funcs = [
        # list the random functions you support here
        #  (you don't need to include all random functions,
        #  only the base random functions randrange, choice
        #  uniform, and normalvariate)
        ...,
    ]

    def __init__(self, examples, params, **options):
        self.init_fallback_backend()

        # the values you want to use for this run as a dict;
        #  you can use params to get the args for each param
        #  and examples to get all the past data (to see what
        #  examples and params look like, use bb.get_data)
        self.current_values = ...

MyBackend.register()
MyBackend.register_alg("my_alg")
```

Once you've written a BBopt backend as above, you simply need to import it to trigger the `register` calls and enable it to be used in BBopt. For some example BBopt backends, see BBopt's default backends (written in [Coconut](http://coconut-lang.org/)):

- [`serving.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/backends/serving.coco)
- [`random.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/backends/random.coco)
- [`skopt.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/backends/skopt.coco)
- [`hyperopt.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/backends/hyperopt.coco)
- [`mixture.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/backends/mixture.coco)
