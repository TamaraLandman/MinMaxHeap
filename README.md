# Min-Max Heap Implementation

## Overview
This project implements a **Min-Max Heap**, a double-ended priority queue that supports efficient retrieval and removal of both the **minimum** and **maximum** elements.

In addition to the heap implementation, this repository includes a comprehensive suite of tests to verify correctness, edge cases, and performance.

---

## Features
- Insert elements in **O(log n)**
- Get minimum element in **O(1)**
- Get maximum element in **O(1)**
- Delete minimum in **O(log n)**
- Delete maximum in **O(log n)**
- Fully tested with unit tests

---

## What is a Min-Max Heap?
A **Min-Max Heap** is a complete binary tree that alternates between:
- **Min levels** (even depth): nodes are smaller than their descendants
- **Max levels** (odd depth): nodes are larger than their descendants

This structure allows efficient access to both extremes:
- Root → minimum  
- One of the root’s children → maximum  


## API

### `insert(value)`
Adds a new value to the heap.

### `getMin()`
Returns the smallest element without removing it.

### `getMax()`
Returns the largest element without removing it.

### `deleteMin()`
Removes and returns the smallest element.

### `deleteMax()`
Removes and returns the largest element.

### `size()`
Returns the number of elements in the heap.

---

## Testing

This project includes unit tests to ensure correctness.


### Test Coverage Includes:
- Insertion ordering
- Min/max retrieval correctness
- Deletion operations
- Edge cases (empty heap, single element)
- Heap property validation

---

## Implementation Details
- Uses an **array-based binary heap**
- Level determined using index depth:
  - Even depth → min level  
  - Odd depth → max level  
- Uses helper functions for:
  - Push up (min/max variants)
  - Push down (min/max variants)

---

## Time Complexity

| Operation   | Complexity |
|------------|-----------|
| Insert     | O(log n)  |
| Get Min    | O(1)      |
| Get Max    | O(1)      |
| Delete Min | O(log n)  |
| Delete Max | O(log n)  |

---

## AI Usage
- This min-max heap implementation was made fully independant of AI. Unit tests and the Read-Me file were created with the use of AI.

