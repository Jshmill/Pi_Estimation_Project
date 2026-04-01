import numpy as np

# CUBE SIZE AND NUMBER OF SAMPLES
S = 1000
TIMES = 2_000_000

# RANDOM SPHERE CENTERS
X = np.random.randint(0, S, size=TIMES)
Y = np.random.randint(0, S, size=TIMES)
Z = np.random.randint(0, S, size=TIMES)


def estimate_ratio_fixed(radius):
    r2 = radius**2

    # 1 CUBE: FULLY INSIDE THE CUBE, NOT NEAR ANY BOUNDARY
    inside = (
        (X >= radius)
        & (X <= S - radius)
        & (Y >= radius)
        & (Y <= S - radius)
        & (Z >= radius)
        & (Z <= S - radius)
    )

    # 8 CORNERS: EIGTH-SPHERES AT CUBE VERTICES
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

    # VALID SPHERES: EDGES OR CORNERS, BUT NOT FULLY INSIDE CUBE
    valid = ~(inside | corner)

    return np.mean(valid)


# ITERATE OVER RADIUS
def findMax(low, high):
    best_radius = low
    best_prob = 0.0
    for r in range(low, high + 1):
        p = estimate_ratio_fixed(r)
        if p > best_prob:
            best_prob, best_radius = p, r / S
    return best_prob, best_radius


def output():
    prob, radius = findMax(250, 350)
    pi_estimation = (3 * (4 * radius**2 - 4 * radius + 1)) / (2 * radius**2)
    print(f"""
    Radius: {radius}
    Diameter: {2 * radius}
    Probability: {prob}
    Pi Estimation: {pi_estimation}
    """)


output()
