"""
Example of using BBopt with run_meta.

To run this example, just run:
    > bbopt ./meta_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run_meta(
        algs=(
            "random",
            "tree_structured_parzen_estimator",
            "gaussian_process",
        ),
        meta_alg="epsilon_greedy",
    )


# We set u ~ uniform(0, 1) * sin(uniform(0, 1)).
from math import sin
u = bb.random("x0") * sin(bb.random("x1"))


# Set u as the thing to minimize.
bb.minimize(u)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(u))
