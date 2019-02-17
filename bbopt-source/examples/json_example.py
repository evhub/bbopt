"""
Simple example using json instead of pickle for enhanced cross-platform compatibility.

To run this example, just run:
    > bbopt ./skopt_example.py
"""

# BBopt setup:
from bbopt import BlackBoxOptimizer
bb = BlackBoxOptimizer(file=__file__, use_json=True)
if __name__ == "__main__":
    bb.run()


# Set up a uniform random 2 x 2 matrix parameter.
X = bb.rand("X", 2, 2)


# Set the goal to be the trace.
y = X[0,0] + X[1,1]
bb.minimize(y)


# Finally, we'll print out the value we used for debugging purposes.
if __name__ == "__main__":
    print(repr(y))
