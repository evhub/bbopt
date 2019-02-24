"""
Simple example using json instead of pickle for enhanced cross-platform compatibility.

To run this example, just run:
    > bbopt ./skopt_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__, protocol="json")
if __name__ == "__main__":
    bb.run()


# Set up log uniform and log normal parameters.
x0 = bb.loguniform("x0", 1, 10, guess=5)
x1 = bb.lognormvariate("x1", 0, 1, guess=1)


# Set the goal to be the sum.
y = x0 + x1
bb.minimize(y)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(y))
