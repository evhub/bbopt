"""
Example of using the default "tpe_or_gp" algorithm.

To run this example, just run:
    > bbopt ./tpe_or_gp_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run()  # alg="tpe_or_gp" should be the default


# We set u ~ normal(0, 1) * sin(normal(0, 1)).
from math import sin
u = bb.normalvariate("x0", 0, 1) * sin(bb.normalvariate("x1", 0, 1))


# Since we used hyperopt-only parameters, we shouldn't have skopt.
if hasattr(bb.backend, "selected_backend"):
    bb.remember({"backend": bb.backend.selected_backend})
    assert bb.backend.selected_backend != "scikit-optimize", bb.backend.selected_backend
else:
    bb.remember({"backend": bb.backend.backend_name})


# Set u as the thing to minimize.
bb.minimize(u)


# Print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(u))
