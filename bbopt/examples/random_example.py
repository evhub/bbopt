"""
Example of using the random backend with BBopt.

To run this example, just run:
    > bbopt ./random_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__)
if __name__ == "__main__":
    bb.run(alg="random")


# Let's use some parameters!
x = bb.randint("x", 1, 10)


# And let's set our goal!
bb.maximize(x)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(x)
