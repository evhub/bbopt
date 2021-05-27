"""
Example of using the mixture backend's remove_erroring_algs feature.

To run this example, just run:
    > bbopt ./remove_erroring_algs_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run_backend(
        "mixture",
        distribution=[
            ("gaussian_process", float("inf")),
            ("tree_structured_parzen_estimator", 1),
        ],
        remove_erroring_algs=True,
    )


# Set some parameters that skopt supports.
x0 = bb.randint("x0", 1, 10, guess=5)
x1 = bb.choice("x1", [-10, -1, 0, 1, 10])


# Set a parameter that only hyperopt supports.
x2 = bb.normalvariate("x2", mu=0, sigma=1)

if not bb.is_serving:
    assert bb.backend.selected_alg == "tree_structured_parzen_estimator", bb.backend.selected_alg


# Set the goal.
y = x0 + x1*x2
bb.minimize(y)


# Print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(y))
