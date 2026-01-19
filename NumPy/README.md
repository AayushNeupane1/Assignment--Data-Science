# NumPy

This folder contains comprehensive examples of NumPy array operations, from basic creation to advanced operations. Includes main NumPy operations and subfolders for N-dimensional arrays and specific operations.

## Main Files Overview

### 1. [first.py](first.py)
**Description:** Basic NumPy array creation and type checking
- Creates a simple 1D array from a list
- Displays array type and contents
- **Key Concepts:** Array creation, type checking, array basics

### 2. [arrayCreation.py](arrayCreation.py)
**Description:** Various methods to create NumPy arrays
- Creates arrays from lists
- Uses `np.zeros()` for zero-filled arrays
- Demonstrates `np.arange()` with step size
- Compares `np.arange()` vs `np.linspace()`
- Creates random arrays with `np.random.rand()` and `np.random.randint()`
- **Key Concepts:** Array creation methods, zeros, range, linspace, random arrays

### 3. [arrayAttributes.py](arrayAttributes.py)
**Description:** Inspecting array properties and attributes
- Demonstrates `ndim` (number of dimensions)
- Shows `shape` (array dimensions)
- Displays `dtype` (data type of elements)
- Shows `size` (total number of elements)
- **Key Concepts:** Array metadata, ndim, shape, dtype, size

### 4. [arrayModify.py](arraymodify.py)
**Description:** Modifying array elements using boolean indexing
- Replaces even numbers with user-specified value
- Replaces odd numbers with user-specified value
- Uses boolean indexing for conditional replacement
- **Key Concepts:** Boolean indexing, conditional modification, masking

### 5. [arraySlicing.py](arraySlicing.py)
**Description:** Extract portions of arrays using slicing
- Slices from index 1 to 4
- Slices from index 2 to end
- Full array slicing
- **Key Concepts:** Array slicing, indexing, range extraction

### 6. [arrayOperation.py](arrayOperation.py)
**Description:** Arithmetic and comparison operations on arrays
- Subtraction operations (- and `np.subtract()`)
- Multiplication operations (* and `np.multiply()`)
- Comparison operations (==, <=, >=, !=)
- Element-wise operations
- **Key Concepts:** Element-wise operations, arithmetic, comparisons

### 7. [booleanIndexing.py](booleanIndexing.py)
**Description:** Boolean indexing and conditional array filtering
- Extracts odd numbers using boolean indexing
- Modifies even numbers to 0 using boolean indexing
- **Key Concepts:** Boolean indexing, filtering, conditional operations

### 8. [comparisonFunctions.py](comparisonFunctions.py)
**Description:** NumPy comparison functions
- Uses `np.less()`, `np.less_equal()`
- Uses `np.greater()`, `np.greater_equal()`
- Uses `np.equal()`, `np.not_equal()`
- Returns boolean arrays
- **Key Concepts:** Comparison functions, boolean arrays, element-wise comparison

### 9. [statisticalFunctions.py](statisticalFunctions.py)
**Description:** Statistical calculations on arrays
- Calculates mean using `np.mean()`
- Calculates median using `np.median()`
- Calculates standard deviation using `np.std()`
- **Key Concepts:** Statistical analysis, mean, median, standard deviation

---

## Subfolder: N_DArray

Advanced operations on multi-dimensional arrays:

### [N_DArray/creation.py](N_DArray/creation.py)
**Description:** Creating 2D and 3D arrays
- Creates 2D arrays with rows and columns
- Creates 3D arrays with blocks, rows, and columns
- Demonstrates arrays with mixed data types
- Creates empty arrays with `np.empty()`
- Creates pre-filled arrays with `np.full()`
- **Key Concepts:** 2D arrays, 3D arrays, array initialization

### [N_DArray/accessing.py](N_DArray/accessing.py)
**Description:** Accessing elements in 3D arrays
- Accesses specific elements using indices [block, row, column]
- **Key Concepts:** 3D indexing, element access

### [N_DArray/slicing.py](N_DArray/slicing.py)
**Description:** Slicing operations on multi-dimensional arrays
- Slices entire 3D array with [:, :, :]
- Extracts specific matrices from 3D array
- Slices specific rows across matrices
- Slices specific columns across matrices
- **Key Concepts:** N-D slicing, matrix extraction, dimensional slicing

---

## Subfolder: operations

Specialized array operations:

### [operations/even_odd.py](operations/even_odd.py)
**Description:** Filtering and replacing even/odd numbers
- Filters even numbers from array
- Replaces odd numbers with 0 using `np.where()`
- **Key Concepts:** Boolean indexing, np.where(), conditional filtering

### [operations/filter.py](operations/filter.py)
**Description:** Filtering negative values from 2D arrays
- Filters negative values from a 2D array
- Replaces negative values with 0 using `np.where()`
- **Key Concepts:** 2D filtering, negative value handling, np.where()

### [operations/matrix.py](operations/matrix.py)
**Description:** Matrix operations and multiplication
- Array multiplication (element-wise)
- Matrix multiplication using `np.matrix` class
- Power operations on arrays and matrices
- **Key Concepts:** Array vs matrix operations, element-wise vs matrix multiplication

### [operations/stack.py](operations/stack.py)
**Description:** Stacking arrays together
- Uses `np.stack()` to combine arrays
- Creates higher dimensional arrays from lower dimensional ones
- **Key Concepts:** Array stacking, combining arrays, dimensionality

### [operations/summean.py](operations/summean.py)
**Description:** Sum and mean operations along axes
- Calculates sum along rows (axis=0)
- Calculates sum along columns (axis=1)
- Calculates mean along rows
- Demonstrates axis-specific operations
- **Key Concepts:** Axis operations, sum, mean, dimensional reduction


## NumPy Topics Covered
- Array creation methods
- Array attributes (ndim, shape, dtype, size)
- Indexing and slicing
- Boolean indexing and masking
- Arithmetic operations
- Comparison operations
- Statistical functions
- 2D and 3D array operations
- Multi-dimensional slicing
- Matrix operations
- Array stacking and combination
- Conditional operations with np.where()
