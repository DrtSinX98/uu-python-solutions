import numpy as np
import time

N = 250

start_time = time.time()

# Creating matrices directly as numpy arrays is much faster
X = np.random.randint(0, 101, size=(N, N))
Y = np.random.randint(0, 101, size=(N, N+1))

# The @ operator performs highly optimized C-level matrix multiplication
result = X @ Y

end_time = time.time()

print(result)
print(f"Execution time: {end_time - start_time:.6f} seconds")