import numpy as np

# Generate once
squareSize = 1000
TIMES = 2000000
X = np.random.randint(0, squareSize, size=TIMES)
Y = np.random.randint(0, squareSize, size=TIMES)

def estimate_ratio_fixed(radius):
    # 1 square (fully inside)
    inside = (
        (X >= radius) &
        (X <= squareSize - radius) &
        (Y >= radius) &
        (Y <= squareSize - radius)
    )

    # 4 squares (corner cases)
    corner = (
        (X**2 + Y**2 <= radius**2) |
        ((X - squareSize)**2 + Y**2 <= radius**2) |
        (X**2 + (Y - squareSize)**2 <= radius**2) |
        ((X - squareSize)**2 + (Y - squareSize)**2 <= radius**2)
    )

    # valid = touches 2 or 3 squares
    valid = ~(inside | corner)

    return np.mean(valid)


def findMax(low, high):
    best_radius = low
    best_probability = 0.0

    for r in range(low, high + 1):
        p = estimate_ratio_fixed(r)
        if p > best_probability:
            best_probability = p
            best_radius = r

    return best_probability, best_radius



            


"""From previous tests, weve found that the radius is in the 200s"""
best_probability, best_radius = findMax(200, 300)
best_diameter = (2 * best_radius) / 1000

print(best_diameter, best_probability)


print(4 * (1 / best_diameter - 1))