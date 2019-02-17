"""
Example of using the scikit-optimize backend and gaussian_process algorithm with BBopt.

To run this example, just run:
    > bbopt ./skopt_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run(alg="gaussian_process")


# Let's use some parameters!
x0 = bb.randrange("x0", 1, 11, guess=5)
x1 = bb.uniform("x1", 0, 1)
x2 = bb.choice("x2", [-10, -1, 0, 1, 10])


# And let's set our goal!
y = x0 + x1*x2
bb.minimize(y)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(y))
