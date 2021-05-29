"""
Example of using the default "any_fast" algorithm.

To run this example, just run:
    > bbopt ./any_fast_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run()  # alg="any_fast" should be the default


# We set u ~ dist(0, 1) * sin(dist(0, 1)) where dist is uniform or normal.
from math import sin
dist = bb.choice("dist", ["uniform", "normal"])
if dist == "normal":
    u = bb.normalvariate("x0_n", 0, 1) * sin(bb.normalvariate("x1_n", 0, 1))
else:
    u = bb.random("x0_u") * sin(bb.random("x1_u"))


# If we used hyperopt-only parameters, we shouldn't have skopt.
if hasattr(bb.backend, "selected_backend"):
    bb.remember({"backend": bb.backend.selected_backend})
    if dist == "normal":
        assert bb.backend.selected_backend != "scikit-optimize", bb.backend.selected_backend
else:
    bb.remember({"backend": bb.backend.backend_name})


# Set u as the thing to minimize.
bb.minimize(u)


# Print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(u))
