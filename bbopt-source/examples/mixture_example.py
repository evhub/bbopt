"""
Example using a mixture distribution over many different possible algorithms.

To run this example, just run:
    > bbopt ./mixture_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__, use_json=True)
if __name__ == "__main__":
    bb.run_backend("mixture", [
        ("gaussian_process", 1),
        ("random_forest", 1),
        ("extra_trees", 1),
        ("gradient_boosted_regression_trees", 1),
        ("tree_structured_parzen_estimator", 1),
        ("annealing", 1),
    ])


# Set up a uniform random 2 x 2 matrix parameter.
X = bb.rand("X", 2, 2)


# Set the goal to be the absolute determinant.
y = abs(X[0,0] * X[1,1] - X[0,1] * X[1,0])
bb.minimize(y)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(y))
