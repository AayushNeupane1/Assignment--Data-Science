# dataTypes

This folder contains assignments demonstrating various Python data types and their operations.

## Files Overview

### 1. [array.py](array.py)
**Description:** Efficient integer array storage using Python's array module
- Creates an array of 100 integers using the `array` module
- Uses type code 'i' for signed integers (memory efficient)
- Iterates and prints all 100 integers
- **Key Concepts:** Array module, memory efficiency, typed arrays, iteration

### 2. [counter.py](counter.py)
**Description:** Character frequency counter using Collections Counter
- Takes string input from user
- Uses `collections.Counter` to count character frequency
- Displays frequency of each character in the string
- **Key Concepts:** Counter class, frequency analysis, dictionary-like behavior

### 3. [employeeinfo.py](employeeinfo.py)
**Description:** Employee data storage using tuples
- Stores fixed employee information in tuples
- Tuple structure: (Name, Age, Position, Salary)
- Demonstrates tuple immutability and indexing
- Displays employee details in formatted output
- **Key Concepts:** Tuples, immutability, fixed-size data, indexing

### 4. [removeDuplicates.py](removeDuplicates.py)
**Description:** Remove duplicate elements from a list using sets
- Takes a list with duplicate integers
- Converts list to set to remove duplicates
- Converts back to list for display
- Shows original and deduplicated lists
- **Key Concepts:** Sets, list conversion, duplicate removal, set operations

### 5. [sortingList.py](sortingList.py)
**Description:** Sort student names alphabetically
- Stores list of student names
- Uses `.sort()` method to sort names alphabetically
- Displays sorted list
- **Key Concepts:** Lists, sorting, string comparison, list methods

### 6. [studentMarks.py](studentMarks.py)
**Description:** Student marks management using dictionaries
- Creates dictionary with student names as keys and marks as values
- Finds and displays student(s) with highest marks
- Uses dictionary methods (keys, values)
- **Key Concepts:** Dictionaries, key-value pairs, finding maximum values, iteration

---

## How to Run

```bash
# Run array creation example
python array.py

# Run character frequency counter
python counter.py

# Run employee information display
python employeeinfo.py

# Run duplicate removal
python removeDuplicates.py

# Run name sorting
python sortingList.py

# Run student marks lookup
python studentMarks.py
```

## Python Data Types Summary

| Data Type | File | Purpose | Key Feature |
|---|---|---|---|
| Array | array.py | Efficient integer storage | Memory efficient, typed |
| Counter | counter.py | Frequency counting | Counts occurrences |
| Tuple | employeeinfo.py | Fixed data storage | Immutable, ordered |
| Set | removeDuplicates.py | Unique elements | No duplicates |
| List | sortingList.py | Ordered collection | Mutable, sortable |
| Dictionary | studentMarks.py | Key-value mapping | Fast lookup |

## Topics Covered
- Lists and list operations
- Tuples and immutability
- Dictionaries and key-value pairs
- Sets and uniqueness
- Python's collections module
- Array module for type-safe storage
- Sorting and searching
- Data type conversions
