# DataStructuresImplementation

This folder contains implementations of fundamental data structures in Python, including both custom implementations and usage of built-in libraries.

## Files Overview

### 1. [linkedlist.py](linkedlist.py)
**Description:** Custom linked list implementation from scratch
- Defines a `Node` class with data and next pointer
- Creates a `linked_l` (linked list) class with head initialization
- Implements manual node creation and linking
- Traverses and prints the linked list
- **Key Concepts:** Object-oriented programming, node creation, pointers, traversal

### 2. [linkedlistLibrary.py](linkedlistLibrary.py)
**Description:** Linked list implementation using Python's deque
- Uses `collections.deque` for efficient linked list operations
- Demonstrates append (add to right), appendleft (add to left)
- Shows popleft (remove from left) and pop (remove from right) operations
- **Key Concepts:** Python collections, deque, FIFO/LIFO operations

### 3. [queue.py](queue.py)
**Description:** Custom Queue implementation
- Defines a `Queue` class with enqueue and dequeue methods
- Implements FIFO (First In First Out) behavior
- Includes methods: enqueue (add), dequeue (remove), print, empty check
- Demonstrates queue operations with error handling
- **Key Concepts:** Class implementation, FIFO, data structures, error handling

### 4. [queueLibrary.py](queueLibrary.py)
**Description:** Queue implementation using Python's deque library
- Uses `collections.deque` for efficient queue operations
- Demonstrates popleft operation for dequeuing
- Shows efficient removal of elements from queue
- **Key Concepts:** deque library, queue operations, efficiency

### 5. [stack.py](stack.py)
**Description:** Custom Stack implementation
- Defines a `Stack` class with push and pop methods
- Implements LIFO (Last In First Out) behavior
- Includes methods: push (add), pop (remove), print, empty check
- Demonstrates stack operations with multiple stack examples
- **Key Concepts:** Class implementation, LIFO, data structures, error handling

### 6. [stackLibrary.py](stackLibrary.py)
**Description:** Stack implementation using Python's list
- Uses Python list's built-in append and pop methods
- Demonstrates LIFO behavior with simple implementation
- Includes iterative popping with display of removed elements
- **Key Concepts:** List operations, stack operations, simplicity

### 7. [heapLibrary.py](heapLibrary.py)
**Description:** Heap operations using Python's heapq module
- Uses `heapq` module for heap operations
- Demonstrates heappush (insert into heap)
- Shows heappop (remove minimum element)
- Demonstrates heapify (convert list to heap)
- **Key Concepts:** Heap data structure, min-heap, heapq module

### 8. [tree.py](tree.py)
**Description:** Custom binary tree implementation
- Defines a `Node` class with left, right, and data attributes
- Implements a binary tree with show method for traversal
- Demonstrates tree structure with manual node creation
- **Key Concepts:** Binary trees, node structures, tree traversal, recursion

### 9. [treeLibrary.py](treeLibrary.py)
**Description:** Tree implementation using NetworkX library
- Uses `networkx` library for graph and tree operations
- Creates a directed graph (tree) with nodes and edges
- Demonstrates tree structure representation
- **Key Concepts:** NetworkX library, directed graphs, tree representation

### 10. [graphLibrary.py](graphLibrary.py)
**Description:** Graph operations using NetworkX library
- Creates an undirected graph structure
- Adds edges between nodes
- Displays nodes and edges of the graph
- **Key Concepts:** Graph theory, NetworkX, nodes, edges

---

## How to Run

```bash
# Run custom linked list
python linkedlist.py

# Run linked list with deque
python linkedlistLibrary.py

# Run custom queue
python queue.py

# Run queue with deque
python queueLibrary.py

# Run custom stack
python stack.py

# Run stack with list
python stackLibrary.py

# Run heap operations
python heapLibrary.py

# Run binary tree
python tree.py

# Run tree with NetworkX
python treeLibrary.py

# Run graph operations
python graphLibrary.py
```

## Data Structures Summary

| Data Structure | File | Type | Key Feature |
|---|---|---|---|
| Linked List | linkedlist.py | Custom | Manual node management |
| Linked List | linkedlistLibrary.py | Library | Deque-based |
| Queue | queue.py | Custom | FIFO |
| Queue | queueLibrary.py | Library | Deque-based |
| Stack | stack.py | Custom | LIFO |
| Stack | stackLibrary.py | Library | List-based |
| Heap | heapLibrary.py | Library | Min-heap |
| Binary Tree | tree.py | Custom | Recursive traversal |
| Tree | treeLibrary.py | Library | NetworkX-based |
| Graph | graphLibrary.py | Library | NetworkX-based |

## Topics Covered
- Object-oriented design for data structures
- Node and pointer concepts
- FIFO and LIFO operations
- Tree and graph structures
- Using Python libraries (collections, heapq, networkx)
- Traversal and manipulation of complex data structures
