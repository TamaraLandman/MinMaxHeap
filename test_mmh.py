import pytest
import random
from min_max_heap import MinMaxHeap



class OracleMinMaxHeap:
    """
    Simplified reference implementation.
    Uses one helper to avoid repeated logic.
    """

    def __init__(self, size):
        self.capacity = size
        self.data = []

    def insert(self, key, value):
        if len(self.data) >= self.capacity:
            return False
        self.data.append((key, value))
        return True

    def _get(self, find_min=True, remove=False):
        """
        Internal helper:
        - find_min: True → min, False → max
        - remove: True → remove element, False → just return it
        """
        if not self.data:
            return False

        func = min if find_min else max
        item = func(self.data, key=lambda x: x[0])

        if remove:
            self.data.remove(item)

        return item

    def findMin(self):
        return self._get(find_min=True, remove=False)

    def findMax(self):
        return self._get(find_min=False, remove=False)

    def removeMin(self):
        return self._get(find_min=True, remove=True)

    def removeMax(self):
        return self._get(find_min=False, remove=True)
    

def test_empty_heap_operations():
    """
    Tests behavior on an empty heap.
    All operations should return None.
    """
    h = MinMaxHeap(5)

    assert h.findMin() == None
    assert h.findMax() == None
    assert h.removeMin() == None
    assert h.removeMax() == None
    
def test_single_element():
    """
    Tests heap with one element.
    Min and max should be the same.
    Removing should return that element and leave heap empty.
    """
    h = MinMaxHeap(5)

    h.insert(10, "a")

    assert h.findMin() == (10, "a")
    assert h.findMax() == (10, "a")

    assert h.removeMin() == (10, "a")
    assert h.findMin() == None  # now empty  
    
def test_basic_insert_find():
    """
    Tests that min and max are correctly tracked after inserts.
    """
    h = MinMaxHeap(5)

    h.insert(5, "a")
    h.insert(1, "b")
    h.insert(10, "c")

    assert h.findMin() == (1, "b")
    assert h.findMax() == (10, "c")
    
def test_remove_min():
    """
    Tests that removeMin returns correct value
    and updates the heap correctly.
    """
    h = MinMaxHeap(5)

    h.insert(5, "a")
    h.insert(1, "b")
    h.insert(10, "c")

    assert h.removeMin() == (1, "b")
    assert h.findMin() == (5, "a")
    
def test_remove_max():
    """
    Tests that removeMax returns correct value
    and updates the heap correctly.
    """
    h = MinMaxHeap(5)

    h.insert(5, "a")
    h.insert(1, "b")
    h.insert(10, "c")

    assert h.removeMax() == (10, "c")
    assert h.findMax() == (5, "a")

def test_capacity_limit():
    """
    Tests that insert fails when capacity is reached.
    """
    h = MinMaxHeap(2)

    assert h.insert(1, "a") == True
    assert h.insert(2, "b") == True
    assert h.insert(3, "c") == False  # exceeds capacity
    
def test_duplicate_keys():
    """
    Tests behavior when multiple elements have the same key.
    Ensures correct tuple is returned and no crashes occur.
    """
    h = MinMaxHeap(5)

    h.insert(5, "a")
    h.insert(5, "b")

    result = h.findMin()
    assert result[0] == 5  # key must be 5

    removed = h.removeMin()
    assert removed[0] == 5

    # One element should still remain
    assert h.findMin() != False

def test_interleaved_operations():
    """
    Tests alternating inserts and removals.
    This catches structural bugs in heap maintenance.
    """
    h = MinMaxHeap(5)

    h.insert(5, "a")
    h.insert(2, "b")
    assert h.removeMin() == (2, "b")

    h.insert(1, "c")
    assert h.findMin() == (1, "c")

    h.insert(10, "d")
    assert h.removeMax() == (10, "d")
    
def test_remove_until_empty():
    """
    Tests repeatedly removing elements until heap is empty.
    Ensures correct ordering and termination behavior.
    """
    h = MinMaxHeap(5)

    h.insert(3, "a")
    h.insert(1, "b")
    h.insert(2, "c")

    assert h.removeMin() == (1, "b")
    assert h.removeMin() == (2, "c")
    assert h.removeMin() == (3, "a")
    assert h.removeMin() == None # now empty

def test_find_does_not_remove():
    """
    Ensures that findMin and findMax do NOT modify the heap.
    """
    h = MinMaxHeap(5)

    h.insert(1, "a")
    h.insert(10, "b")

    assert h.findMin() == (1, "a")
    assert h.findMin() == (1, "a")  # should still be there

    assert h.findMax() == (10, "b")
    assert h.findMax() == (10, "b")  # should still be there
    
    
def test_string_keys_basic_ordering():
    """
    Tests that string keys are ordered lexicographically.
    """
    h = MinMaxHeap(5)

    h.insert("banana", "a")
    h.insert("apple", "b")
    h.insert("cherry", "c")

    assert h.findMin() == ("apple", "b")
    assert h.findMax() == ("cherry", "c")
    
def test_string_keys_remove_min():
    """
    Tests removeMin with string keys.
    Ensures correct lexicographic minimum is removed.
    """
    h = MinMaxHeap(5)

    h.insert("dog", "x")
    h.insert("cat", "y")
    h.insert("elephant", "z")

    assert h.removeMin() == ("cat", "y")
    assert h.findMin() == ("dog", "x")

def test_string_keys_remove_max():
    """
    Tests removeMax with string keys.
    Ensures correct lexicographic maximum is removed.
    """
    h = MinMaxHeap(5)

    h.insert("dog", "x")
    h.insert("cat", "y")
    h.insert("elephant", "z")

    assert h.removeMax() == ("elephant", "z")
    assert h.findMax() == ("dog", "x")
    
def test_string_duplicate_keys():
    """
    Tests behavior when duplicate string keys exist.
    Ensures correct handling without crashing.
    """
    h = MinMaxHeap(5)

    h.insert("apple", "a")
    h.insert("apple", "b")

    result = h.findMin()
    assert result[0] == "apple"

    removed = h.removeMin()
    assert removed[0] == "apple"

    assert h.findMin() != False  # one still remains
    
def test_string_case_sensitivity():
    """
    Tests that ordering respects ASCII/lexicographic rules.
    Uppercase letters come before lowercase.
    """
    h = MinMaxHeap(5)

    h.insert("apple", "a")
    h.insert("Banana", "b")  # uppercase B

    assert h.findMin() == ("Banana", "b")  # 'B' < 'a'
    assert h.findMax() == ("apple", "a")
    
def test_empty_string_key():
    """
    Tests behavior when empty string is used as a key.
    """
    h = MinMaxHeap(5)

    h.insert("", "empty")
    h.insert("a", "letter")

    assert h.findMin() == ("", "empty")
    assert h.removeMin() == ("", "empty")
    
    
def test_string_length_ordering():
    """
    Tests lexicographic ordering with different string lengths.
    """
    h = MinMaxHeap(5)

    h.insert("a", "short")
    h.insert("aa", "longer")
    h.insert("b", "next")

    assert h.findMin() == ("a", "short")
    assert h.findMax() == ("b", "next")
    
def test_float_keys_all_operations():
    """
    Tests all heap operations using floating-point keys.

    Validates:
    - Correct ordering with decimals
    - Handling of negative and positive floats
    - Proper updates after removals
    """
    h = MinMaxHeap(6)

    # Insert float keys
    assert h.insert(2.5, "a") == True
    assert h.insert(-1.2, "b") == True
    assert h.insert(3.7, "c") == True
    assert h.insert(0.0, "d") == True

    # Check min and max
    assert h.findMin() == (-1.2, "b")
    assert h.findMax() == (3.7, "c")

    # Remove min and verify update
    assert h.removeMin() == (-1.2, "b")
    assert h.findMin() == (0.0, "d")

    # Remove max and verify update
    assert h.removeMax() == (3.7, "c")
    assert h.findMax() == (2.5, "a")

    # Final removals
    assert h.removeMin() == (0.0, "d")
    assert h.removeMax() == (2.5, "a")

    # Heap should now be empty
    assert h.findMin() == None
    assert h.removeMax() == None
    
def test_negative_keys_all_operations():
    """
    Tests all heap operations using negative integer keys.

    Validates:
    - Correct ordering with all-negative values
    - Ensures min is most negative and max is closest to zero
    - Proper behavior after multiple removals
    """
    h = MinMaxHeap(6)

    # Insert negative keys
    assert h.insert(-10, "a") == True
    assert h.insert(-3, "b") == True
    assert h.insert(-20, "c") == True
    assert h.insert(-1, "d") == True

    # Check min and max
    assert h.findMin() == (-20, "c")   # most negative
    assert h.findMax() == (-1, "d")    # closest to zero

    # Remove min and verify update
    assert h.removeMin() == (-20, "c")
    assert h.findMin() == (-10, "a")

    # Remove max and verify update
    assert h.removeMax() == (-1, "d")
    assert h.findMax() == (-3, "b")

    # Continue removing
    assert h.removeMax() == (-3, "b")
    assert h.removeMin() == (-10, "a")

    # Heap should now be empty
    assert h.findMax() == None
    assert h.removeMin() == None
    
    
    
pytest.main(["-v", "-s", "test_mmh.py"])