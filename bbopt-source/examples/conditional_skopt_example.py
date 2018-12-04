"""
Example of using BBopt with conditional parameters that only appear
during some runs depending on the value(s) of other parameters. For
this example, we use scikit-optimize for our conditional parameters,
which requires us to pass placeholder_when_missing values.

To run this example, just run:
    > bbopt ./conditional_skopt_example.py
"""

# BBopt boilerplate:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run(backend="scikit-optimize")


# We set the x parameter conditional on the use_high parameter.
use_high = bb.randbool("use high", guess=False)
assert isinstance(use_high, bool)
if use_high:
    x = bb.randrange("x high", 10, 20, placeholder_when_missing=10)
else:
    x = bb.randrange("x low", 10, placeholder_when_missing=0)


# We set x as the thing we want to optimize.
bb.maximize(x)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(x))
