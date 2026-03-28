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

## Day 4: Best Practices - 2

* **Unit Testing (`pytest`):** Developed a test suite (`test_simple_math.py`) to systematically verify the mathematical operations and polynomial evaluations within the `simple_math` module.
* **API Documentation (`Sphinx`):** Integrated standard NumPy-style docstrings into the codebase and utilized Sphinx to automatically generate a compiled HTML API reference. Configured system paths and extensions in `conf.py` and `index.rst` to render the module's documentation seamlessly.
* **Data Visualization (`matplotlib`):** Designed customized visualizations using the object-oriented API. Created a contour plot forming a plasma flower using `meshgrid`, the `plasma` colormap, and cleaned axis spines.
* **Data Fitting & Optimization (`scipy`):** Aligned a theoretical model with experimental scattering data. 
  * Solved grid-mismatch issues by mapping the model onto the experimental $x$-coordinates using `scipy.interpolate.interp1d`.
  * Determined the optimal scaling factor by minimizing the Sum of Squared Errors (SSE) using `scipy.optimize.minimize_scalar`.
  * Implemented strict bounds, NaN masking, and array sorting to ensure robust optimizer convergence and prevent mathematical crashes during the fitting routine.

## Day 5: Data Containers

* **Linear Algebra (`scipy.linalg`):** Solved systems of linear equations ($Ax = b$), calculated inverse and determinant matrices, extracted eigenvalues and eigenvectors, and evaluated various matrix norms (Frobenius, L1, L-infinity).
* **Statistical Distributions & Testing (`scipy.stats`):** * Modeled and plotted discrete (Poisson) and continuous (Normal) random variables, comparing their Probability Mass/Density Functions (PMF/PDF) against Cumulative Distribution Functions (CDF) and randomized histograms.
  * Performed hypothesis testing using Welch's t-test (`ttest_ind`) to determine if independent datasets originated from the same distribution.
* **Data Manipulation & Grouping (`pandas`):** * **Inspection & Slicing:** Loaded heterogeneous data, inspected structural metadata, and utilized label-based (`.loc`) and integer-based (`.iloc`) indexing to extract specific rows, columns, and sub-dataframes.
  * **Filtering:** Applied complex boolean masks to filter data based on multi-condition logic.
  * **Aggregation:** Utilized the Split-Apply-Combine workflow via `.groupby()` to calculate descriptive statistics (mean, median, min, max) and isolate top aggregates across distinct categories.