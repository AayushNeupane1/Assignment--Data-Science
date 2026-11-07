"""NumPy - creating arrays. Consolidated from NumPy/arrayCreation, first, etc.
Run: python creation.py
"""

import numpy as np


def main():
    print("from list   :", np.array([1, 2, 3, 4]))
    print("zeros (2,3) :\n", np.zeros((2, 3)))
    print("full (2,2,7):\n", np.full((2, 2), 7))
    print("arange      :", np.arange(0, 10, 2))      # [0 2 4 6 8]
    print("linspace    :", np.linspace(0, 1, 5))     # [0. .25 .5 .75 1.]

    rng = np.random.default_rng(seed=42)             # reproducible
    print("random ints :", rng.integers(1, 100, size=5))


if __name__ == "__main__":
    main()
