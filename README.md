# BBOpt

BBopt is a frontend for easily interfacing with any black box optimization framework.

BBopt provides a universal interface based on the standard library `random` module (so you don't even have to learn anything new!) that lets you define your tunable parameters.

Once you've defined your parameters, training a black box optimization model on those parameters is as simple as
```
python your_file.py
```
and serving your file with optimized parameters as simple as
```
import your_file
```

## Installation

To get going with BBopt, just install it with
```
pip install bbopt
```

## Usage

To use bbopt, just add
```python
# BBopt boilerplate:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run(backend="scikit-optimize")
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
python <your file here>
```
to train your model, and just
```
import <your module here>
```
to serve it!

## Backends

Currently, BBopt only supports the `scikit-optimize` and `random` backends, but more are in the works! To change backends, just modify `backend="scikit-optimize"` in the boilerplate to whatever backend you want to use. All backends always use the universal interface of
```python
bb.<random function>(<name>, <args to function>)
```
to define parameters.

## Examples

Some examples of BBopt in action (BBopt's examples are written in [Coconut](http://coconut-lang.org/)):

- [`random_example.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/random_example.coco): Extremely basic example using the `random` backend.
- [`skopt_example.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/skopt_example.coco): Slightly more complex example making use of the `scikit-optimize` backend.
- [`conditional_example.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/conditional_example.coco): Example of having black box parameters that are dependent on other black box parameters.
- [`keras_example.coco`](https://github.com/evhub/bbopt/blob/master/bbopt-source/examples/keras_example.coco): Complete example of using BBopt to optimize a neural net in Keras.
