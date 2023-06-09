#https://www.bottomscience.com/lagrange-interpolation-method-python/
import numpy as np

def lagrange(x, y, t):
    """
    Find the Lagrange polynomial through the points (x, y) and return its value at t.
    """
    # Lagrange Interpolation Method  [By Bottom Science]

    # Check that the input arrays have the same length
    if len(x) != len(y):
        raise ValueError("The arrays x and y must have the same length.")

    # Initialize the polynomial
    p = 0

    # Loop over the points
    for i in range(len(x)):
        # Get the current point
        xi, yi = x[i], y[i]

        # Initialize the term
        term = yi

        # Loop over the other points
        for j in range(len(x)):
            # Skip the current point
            if i == j:
                continue

            # Multiply the term by the appropriate factor
            term *= (t - x[j]) / (xi - x[j])

        # Add the term to the polynomial
        p += term

    return p

#YOUR DATA POINTS

x = [0, 1, 2]
y = [0, 1, 4]
t = 0.5
p = lagrange(x, y, t)
print(p)

# OUTPUT - 0.25