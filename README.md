# Blackboard

_The easiest hyperparameter optimization you'll ever do._

Blackboard is a frontend for easily interfacing with any black box optimization framework.

To use blackboard, just add

    # Blackboard boilerplate:
    from blackboard import BlackBoxOptimizer
    bb = BlackBoxOptimizer(file=__file__)
    if __name__ == "__main__":
        bb.run(backend="scikit-optimize")

to the top of your file, then call

    x = bb.param(name="x", uniform=(0, 1))

for each of the tunable parameters in your model, and finally add

    bb.maximize(x)      or      bb.minimize(x)

to set the value being optimized. Then, run

    python <your file here>

to train your model, and just

    import <your module here>

to serve it.
