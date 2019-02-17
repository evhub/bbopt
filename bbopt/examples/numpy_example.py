"""
Example of using some of the array-based parameter definition methods.

To run this example, just run:
    > bbopt ./skopt_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run()


# Generate 1 x 10 and 10 x 1 random vectors.
x0 = bb.rand("x0", 1, 10)  # entries uniform in [0, 1)
x1 = bb.randn("x1", 10, 1)  # entries standard normal


# Set the loss to be their dot product.
y = float(x0.dot(x1))
bb.minimize(y)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(y))
