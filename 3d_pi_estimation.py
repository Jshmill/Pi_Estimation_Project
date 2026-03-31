import numpy as np

# Cube size and number of samples
S = 1000
TIMES = 2_000_000

# Random sphere centers
X = np.random.randint(0, S, size=TIMES)
Y = np.random.randint(0, S, size=TIMES)
Z = np.random.randint(0, S, size=TIMES)


def estimate_ratio_fixed(radius):
    r2 = radius**2

    # 1 cube: fully inside the cube, not near any boundary
    inside = (
        (X >= radius)
        & (X <= S - radius)
        & (Y >= radius)
        & (Y <= S - radius)
        & (Z >= radius)
        & (Z <= S - radius)
    )

    # 8 corners: quarter-spheres at cube vertices
    corner = (
        (X**2 + Y**2 + Z**2 <= r2)
        | ((X - S) ** 2 + Y**2 + Z**2 <= r2)
        | (X**2 + (Y - S) ** 2 + Z**2 <= r2)
        | (X**2 + Y**2 + (Z - S) ** 2 <= r2)
        | ((X - S) ** 2 + (Y - S) ** 2 + Z**2 <= r2)
        | ((X - S) ** 2 + Y**2 + (Z - S) ** 2 <= r2)
        | (X**2 + (Y - S) ** 2 + (Z - S) ** 2 <= r2)
        | ((X - S) ** 2 + (Y - S) ** 2 + (Z - S) ** 2 <= r2)
    )

    # Valid spheres: edges or corners, but not fully inside cube
    valid = ~(inside | corner)

    return np.mean(valid)


# Example: iterate over radius
def findMax(low, high):
    best_radius = low
    best_prob = 0.0
    for r in range(low, high + 1):
        p = estimate_ratio_fixed(r)
        if p > best_prob:
            best_prob, best_radius = p, r / S
    return best_prob, best_radius


def output():
    prob, radius_pixels = findMax(250, 350)
    radius = radius_pixels
    pi_estimation = (3 * (4 * radius**2 - 4 * radius + 1)) / (2 * radius**2)
    print(f"""
    Radius: {radius}
    Diameter: {2 * radius}
    Probability: {prob}
    Pi Estimation: {pi_estimation}
    """)


output()


"""
The Formula is as follows:
Pvalid = 1 - [(1 - 2r)^3 +  (4 / 3) * πr^3]
To find the max P, we must find the derivative of P with respect to r and set it to 0.
P' = (4π + 24) * r^2 + (-6π - 24) * r + 6 = 0


SEE Work.jpeg for further details
"""
