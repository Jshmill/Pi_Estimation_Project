# 3d_test
import numpy as np

# Initialize random points in a square of size 1000x1000
squareSize = 1000
TIMES = 2000000
X = np.random.randint(0, squareSize, size=TIMES)
Y = np.random.randint(0, squareSize, size=TIMES)
Z = np.random.randint(0, squareSize, size=TIMES)


# Given a radius, estimate ratio of hits (touching 2
# or 3 cubes) and misses (touching 1 or 4 cubes)
def estimate_ratio_fixed(radius):
    # 1 cube (fully inside)
    inside = (
        (X >= radius)
        & (X <= squareSize - radius)
        & (Y >= radius)
        & (Y <= squareSize - radius)
        & (Z >= radius)
        & (Z <= squareSize - radius)
    )
    # 4 cubes (corner cases)
    corner = (
        (X**2 + Y**2 + Z**2 <= radius**2)
        | ((X - squareSize) ** 2 + Y**2 + Z**2 <= radius**2)
        | (X**2 + (Y - squareSize) ** 2 + Z**2 <= radius**2)
        | (X**2 + Y**2 + (Z - squareSize) ** 2 <= radius**2)
        | ((X - squareSize) ** 2 + (Y - squareSize) ** 2 + Z**2 <= radius**2)
        | (X**2 + (Y - squareSize) ** 2 + (Z - squareSize) ** 2 <= radius**2)
        | ((X - squareSize) ** 2 + Y**2 + (Z - squareSize) ** 2 <= radius**2)
        | (
            (X - squareSize) ** 2 + (Y - squareSize) ** 2 + (Z - squareSize) ** 2
            <= radius**2
        )
    )
    # valid = touches 2 or 3 squares
    valid = ~(inside | corner)
    return np.mean(valid)


# Iterate over a range of radius values
# to determine max probability
def findMax(low, high):
    best_radius = low
    best_probability = 0.0
    for r in range(low, high + 1):
        p = estimate_ratio_fixed(r)
        if p > best_probability:
            best_probability, best_radius = p, r / 1000
    return best_probability, best_radius


# From previous tests, it's been found that
# the radius is in the 200s
def output():
    probability, radius = findMax(200, 300)
    pi_estimation = 4 * (1 / (2 * radius) - 1)
    print(f"""  
    Radius: {radius}
    Diameter: {2 * radius}
    Probability: {probability}
    Pi Estimation: {pi_estimation}
    """)


# Run the program
output()
