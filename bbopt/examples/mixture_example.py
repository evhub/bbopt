"""
Example using a mixture distribution over many different possible algorithms.

To run this example, just run:
    > bbopt ./mixture_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run_backend("mixture", [
        ("tree_structured_parzen_estimator", 1),
        ("annealing", 1),
        ("gaussian_process", 1),
        ("random_forest", 1),
        ("extra_trees", 1),
        ("gradient_boosted_regression_trees", 1),
    ])


# If we're not serving, store which algorithm the
#  mixture backend has selected.
if not bb.is_serving:
    bb.remember({
        "alg": bb.backend.selected_alg,
    })


# Set up a parameter from a choice and a random sample.
xs = bb.sample("xs", range(10), 5, guess=[3,4,5,6,7])
y = bb.choice("y", [1, 10, 100], guess=10)


# Set the goal to be the absolute difference of sum(xs) and y.
loss = abs(sum(xs) - y)
bb.minimize(loss)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(loss))
