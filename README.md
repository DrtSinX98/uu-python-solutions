# Advanced Scientific Programming with Python: Course Exercises

This repository contains solutions for the daily course exercises.

## Day 1: Basics
* **Jupyter Essentials:** Completed introductory Python exercises using a minimal Jupyter Notebook.

## Day 2: Best Practices - 1

* **Python Packaging (`animals`):** Reorganized a flat collection of Python scripts into a properly structured package with `harmless` and `dangerous` subpackages. Utilized `__all__` in `__init__.py` files to define a clean public API and resolve `ruff` linter warnings.
* **Interactive Debugging (`dicegame`):** Resolved logical and runtime errors in a buggy dice game using `pdb`/`ipdb`. Fixed state reset issues, corrected scoring logic, ensured proper loop behavior for dice re-rolling, and handled invalid user inputs gracefully.
* **Profiling & Optimization (`matmult.py` & `euler72.py`):** Utilized `cProfile` and `line_profiler` (`kernprof`) to identify computational bottlenecks. 
  * Replaced $O(N^3)$ nested `for` loops in matrix multiplication with highly optimized, vectorized NumPy array operations.
  * Optimized Project Euler #72 by replacing iterative, point-by-point integer factorization with an array-based.

## Day 3: High-Performance Computing

* **Object-Oriented Design (`classroom.py`):** Implemented foundational classes (`Person`, `Student`, `Teacher`) demonstrating inheritance and properly utilizing `super()` for constructor overriding.
* **Advanced NumPy Operations:** * Practiced array creation, slicing, masking, and linear algebra (e.g., checkerboard pattern generation, diagonal extraction via fancy indexing).
  * **Broadcasting:** Implemented efficient 3D coordinate normalization without explicit loops.
  * **Memory Layouts:** Utilized `np.lib.stride_tricks.as_strided` to manipulate byte strides, creating a memory-efficient 2D sliding window view over an array (the foundation of convolutional operations).
* **MPI Parallelization (`mpi4py`):** Developed scripts to execute across distributed environments. Demonstrated basic process rank identification (`mpi_ranks.py`) and collective communication using `comm.reduce` to aggregate data across nodes (`mpi_sum.py`).