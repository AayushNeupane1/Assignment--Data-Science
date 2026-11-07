"""NumPy - attributes, indexing, slicing (1D, 2D, 3D).
Consolidated from NumPy/arrayAttributes, arraySlicing, N_DArray/*. Run: python attributes_indexing.py
"""

import numpy as np


def main():
    m = np.array([[1, 2, 3], [4, 5, 6]])
    print("ndim :", m.ndim, "| shape:", m.shape, "| size:", m.size, "| dtype:", m.dtype)

    # 1D slicing
    a = np.array([10, 20, 30, 40, 50])
    print("\na[1:4] :", a[1:4])     # [20 30 40]
    print("a[::2] :", a[::2])       # [10 30 50]

    # 2D indexing
    print("\nm[0,2] :", m[0, 2])    # 3
    print("m[:,0] :", m[:, 0])      # [1 4]

    # a slice is a view
    base = np.array([1, 2, 3, 4])
    view = base[0:2]; view[0] = 99
    print("\nview edits original:", base)   # [99 2 3 4]

    # 3D access
    cube = np.arange(8).reshape(2, 2, 2)
    print("\n3D cube:\n", cube)
    print("cube[1,0,1] :", cube[1, 0, 1])   # 5


if __name__ == "__main__":
    main()
