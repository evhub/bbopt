"""
Example of using BBopt with conditional parameters and randomness
while leveraging the bayes-skopt backend.

To run this example, just run:
    > bbopt ./bask_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run(alg="bask_gaussian_process")


# We set the x parameter conditional on the use_high parameter and add randomness.
import random
use_high = bb.randbool("use high", guess=False)
assert isinstance(use_high, bool), type(use_high)
if use_high:
    x = bb.randrange("x high", 10, 20) * random.random()
else:
    x = bb.randrange("x low", 10) * random.random()


# We set x as the thing we want to optimize.
bb.maximize(x)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(x))
