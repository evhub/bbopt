"""
Example of using the pySOT backend and stochastic_radial_basis_function algorithm with BBopt.

To run this example, just run:
    > bbopt ./skopt_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)


def run_trial(serving=False):
    """Run one trial of black box optimization."""
    if serving:
        bb.run(alg="serving")
    else:
        bb.run(alg="stochastic_radial_basis_function")

    # We'll define some parameters
    x0 = bb.randrange("x0", 1, 11, guess=5)
    x1 = bb.uniform("x1", 0, 1)
    x2 = bb.choice("x2", [-10, -1, 0, 1, 10])

    # And set our goal
    y = x0 + x1*x2
    bb.minimize(y)
    return y


def main(num_trials=10):
    """Run multiple trials of black box optimization."""
    for i in range(num_trials):
        run_trial(serving=False)
    # Return the loss of the best run
    return bb.get_best_run()["loss"]


if __name__ == "__main__":
    print(main())
    # check that we only ever created one backend
    assert all(count <= 2 for count in bb._backend_creation_counts.values()), bb._backend_creation_counts


best_y = run_trial(serving=True)
