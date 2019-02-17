"""
Example of using the hyperopt backend with BBopt.

To run this example, just run:
    > bbopt ./hyperopt_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run(alg="tree_structured_parzen_estimator")


# Let's use some parameters!
x0 = bb.randint("x0", 1, 10, guess=5)
x1 = bb.normalvariate("x1", mu=0, sigma=1)
x2 = bb.choice("x2", [-10, -1, 0, 1, 10])


# And let's set our goal!
y = x0 + x1*x2
bb.minimize(y)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(y))
