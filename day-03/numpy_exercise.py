import numpy as np

# a. Null vector of size 10, but the 5th value is 1
Z_a = np.zeros(10)
Z_a[4] = 1

# b. Vector with values ranging from 10 to 49
Z_b = np.arange(10, 50)

# c. Reverse a vector (first element becomes last)
Z_c = Z_b[::-1]

# d. 3x3 matrix with values ranging from 0 to 8
Z_d = np.arange(9).reshape(3, 3)

# e. Find indices of non-zero elements
Z_e = np.nonzero([1, 2, 0, 0, 4, 0])

# f. Random vector of size 30 and find the mean
Z_f = np.random.random(30)
mean_val = Z_f.mean()

# g. 2D array with 1 on the border and 0 inside
Z_g = np.ones((5, 5))
Z_g[1:-1, 1:-1] = 0

# h. 8x8 matrix filled with a checkerboard pattern
Z_h = np.zeros((8, 8), dtype=int)
Z_h[1::2, ::2] = 1
Z_h[::2, 1::2] = 1

# i. Checkerboard 8x8 matrix using the tile function
Z_i = np.tile([[0, 1], [1, 0]], (4, 4))

# j. Negate all elements between 3 and 8 in place
Z_j = np.arange(11)
Z_j[(3 < Z_j) & (Z_j <= 8)] *= -1
print(Z_j)

# k. Create a random vector of size 10 and sort it
Z_k = np.random.random(10)
Z_k.sort()
print(Z_k)

# l. Check if two random arrays A and B are equal
A = np.random.randint(0, 2, 5)
B = np.random.randint(0, 2, 5)
equal = np.array_equal(A, B)
print(equal)

# m. Calculate the square of every number in an array in place
Z_m = np.arange(10, dtype=np.int32)
print(Z_m.dtype)
Z_m **= 2
print(Z_m.dtype)

# n. Get the diagonal of a dot product
A_n = np.arange(9).reshape(3, 3)
B_n = A_n + 1
C_n = np.dot(A_n, B_n)
D_n = np.diag(C_n)
print(D_n)