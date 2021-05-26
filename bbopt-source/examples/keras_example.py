"""
Example of using BBopt to tune Keras hyperparameters. Uses the full
BBopt API instead of just the boilerplate and implements its own
(very basic) command-line interface instead of using BBopt's. By
implementing our own optimization loop, we are able to avoid the
overhead of running the entire file multiple times, which is what
the BBopt command line does.

To run this example, just run:
    > python ./keras_example.py
"""

# Imports:
import sys
import os
from argparse import ArgumentParser
from pprint import pprint

import numpy as np
from matplotlib import pyplot as plt
from sklearn import datasets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.regularizers import l1_l2


# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)


# Load data into X and y:
iris = datasets.load_iris()

X = iris.data
y = to_categorical(iris.target)


# Split data into training, validation, and testing:
train_split = int(.6*len(X))
validate_split = train_split + int(.2*len(X))

X_train, X_validate, X_test = X[:train_split], X[train_split:validate_split], X[validate_split:]
y_train, y_validate, y_test = y[:train_split], y[train_split:validate_split], y[validate_split:]


def run_trial():
    """Run one trial of hyperparameter optimization."""
    # Start BBopt:
    bb.run()

    # Create model:
    model = Sequential([
        Dense(
            units=bb.randint("hidden neurons", 1, 15, guess=5),
            input_shape=X.shape[1:],
            kernel_regularizer=l1_l2(
                l1=bb.uniform("l1", 0, 0.1, guess=0.005),
                l2=bb.uniform("l2", 0, 0.1, guess=0.05),
            ),
            activation="relu",
        ),
        Dense(
            units=y.shape[1],
            activation="softmax",
        ),
    ])

    # Compile model:
    model.compile(
        loss="categorical_crossentropy",
        optimizer=SGD(
            lr=bb.uniform("learning rate", 0, 0.5, guess=0.15),
            decay=bb.uniform("decay", 0, 0.01, guess=0.0005),
            momentum=bb.uniform("momentum", 0, 1, guess=0.5),
            nesterov=bool(bb.getrandbits("nesterov", 1, guess=1)),
        ),
        metrics=["accuracy"],
    )

    # Train model:
    train_history = model.fit(
        X_train,
        y_train,
        epochs=50,
        batch_size=bb.randint("batch size", 1, 32, guess=16),
        verbose=0,
    )

    train_loss = train_history.history["loss"][-1]
    train_acc = train_history.history["accuracy"][-1]

    validation_loss, validation_acc = model.evaluate(X_validate, y_validate, verbose=0)

    test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)

    # Store BBopt information:
    bb.remember({
        "training loss": train_loss,
        "training accuracy": train_acc,
        "validation loss": validation_loss,
        "validation accuracy": validation_acc,
        "test loss": test_loss,
        "test accuracy": test_acc,
    })

    # End run minimizing validation loss:
    bb.minimize(validation_loss)


# Set up command-line interface:
parser = ArgumentParser()
parser.add_argument(
    "-n", "--num-trials",
    metavar="trials",
    type=int,
    default=20,
    help="number of trials to run (defaults to 20)",
)


if __name__ == "__main__":
    args = parser.parse_args()

    # Main loop:
    for i in range(args.num_trials):
        run_trial()
        print("Summary of run {}/{}:".format(i+1, args.num_trials))
        pprint(bb.get_current_run())
        print()

    print("\nSummary of best run:")
    pprint(bb.get_best_run())

    print("Displaying plots...")

    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(10, 10))
    bb.plot_convergence(ax1)
    bb.plot_history(ax2)
    bb.plot_partial_dependence_1D("hidden neurons", ax3)
    bb.plot_partial_dependence_1D("learning rate", ax4)

    plt.figure(1)
    bb.plot_evaluations()

    plt.figure(2)
    bb.plot_objective()

    plt.figure(3)
    bb.plot_regret()

    plt.show()
