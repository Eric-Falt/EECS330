import math
import random
import time


# -----------------------------------------
# Index helper functions (0-based)
# -----------------------------------------
def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


# -----------------------------------------
# Print the heap as levels
# -----------------------------------------
def print_heap_tree(arr, heap_size, title=None):
    """Print the heap in level order as a tree-like display.

    Shows only arr[0:heap_size] as the current heap, and prints the
    sorted suffix if it exists.
    """
    if title:
        print(title)

    if heap_size <= 0:
        print("Heap: (empty)")
        if len(arr) > 0:
            print(f"Sorted suffix: {arr}")
        print()
        return

    height = math.ceil(math.log2(heap_size + 1))
    index = 0
    level = 0

    while index < heap_size:
        level_count = min(2 ** level, heap_size - index)
        entries = []
        for j in range(level_count):
            idx = index + j
            entries.append(f"[{idx}]={arr[idx]}")
        print(f"Level {level}: " + " ".join(entries))
        index += level_count
        level += 1

    if heap_size < len(arr):
        print(f"Sorted suffix: {arr[heap_size:]}")
    print()


# -----------------------------------------
# Core heap operations
# -----------------------------------------
def max_heapify(arr, i, heap_size):
    """Restore max-heap property at index i within arr[0:heap_size]."""
    while True:
        left_child = left(i)
        right_child = right(i)
        largest = i

        if left_child < heap_size and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < heap_size and arr[right_child] > arr[largest]:
            largest = right_child

        if largest == i:
            break

        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest


def min_heapify(arr, i, heap_size):
    """Restore min-heap property at index i within arr[0:heap_size]."""
    while True:
        left_child = left(i)
        right_child = right(i)
        smallest = i

        if left_child < heap_size and arr[left_child] < arr[smallest]:
            smallest = left_child

        if right_child < heap_size and arr[right_child] < arr[smallest]:
            smallest = right_child

        if smallest == i:
            break

        arr[i], arr[smallest] = arr[smallest], arr[i]
        i = smallest


# These private helpers let heapsort build a heap without printing a
# large tree when sorting a large input array.
def _build_max_heap_in_place(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        max_heapify(arr, i, len(arr))


def _build_min_heap_in_place(arr):
    for i in range(len(arr) // 2 - 1, -1, -1):
        min_heapify(arr, i, len(arr))


# -----------------------------------------
# Build heaps in-place and display the steps
# -----------------------------------------
def build_min_heap(arr):
    n = len(arr)
    print_heap_tree(arr, n, title="Before build_min_heap (not a heap yet):")

    # Leaves at indices n//2 through n-1 are already heaps.
    for i in range(n // 2 - 1, -1, -1):
        min_heapify(arr, i, n)

    print_heap_tree(arr, n, title="After build_min_heap (is a min-heap):")
    print("Done with building MIN HEAP")
    return arr


def build_max_heap(arr):
    n = len(arr)
    print_heap_tree(arr, n, title="Before build_max_heap (not a heap yet):")

    # Leaves at indices n//2 through n-1 are already heaps.
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, i, n)

    print_heap_tree(arr, n, title="After build_max_heap (is a max-heap):")
    print("Done with building MAX HEAP")
    return arr


# -----------------------------------------
# Question 2: Heapsort using both heap types
# Each function takes a list and returns a list.
# -----------------------------------------
def heapSort_max(arr):
    """Return arr sorted ascending using a max-heap."""
    result = arr.copy()
    _build_max_heap_in_place(result)

    for end in range(len(result) - 1, 0, -1):
        result[0], result[end] = result[end], result[0]
        max_heapify(result, 0, end)

    return result


def heapSort_min(arr):
    """Return arr sorted ascending by repeatedly extracting min values."""
    heap = arr.copy()
    _build_min_heap_in_place(heap)
    sorted_values = []

    while heap:
        smallest = heap[0]
        last = heap.pop()

        if heap:
            heap[0] = last
            min_heapify(heap, 0, len(heap))

        sorted_values.append(smallest)

    return sorted_values


# -----------------------------------------
# Correctness and stability checks
# -----------------------------------------
class TaggedValue:
    """Compare only by key so the test can reveal whether equal keys reorder."""
    def __init__(self, key, tag):
        self.key = key
        self.tag = tag

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def __eq__(self, other):
        return isinstance(other, TaggedValue) and self.key == other.key

    def __repr__(self):
        return f"({self.key}, {self.tag})"


def check_stability(sort_function, function_name):
    items = [
        TaggedValue(1, "A"),
        TaggedValue(1, "B"),
        TaggedValue(1, "C"),
    ]
    sorted_items = sort_function(items)
    print(f"{function_name} stability test:")
    print("  Input: ", items)
    print("  Output:", sorted_items)

    stable = True
    for key in {item.key for item in items}:
        original_order = [item.tag for item in items if item.key == key]
        output_order = [item.tag for item in sorted_items if item.key == key]
        if original_order != output_order:
            stable = False

    print("  Stable:", stable, "(heapsort is generally not stable)\n")


# -----------------------------------------
# Question 3: Runtime comparison
# -----------------------------------------
def benchmark():
    try:
        import numpy as np
    except ImportError:
        print("NumPy is not installed; skipping the NumPy benchmark.")
        return

    n = 5000
    random.seed(42)
    arr = [random.randint(0, 10**6) for _ in range(n)]

    start = time.perf_counter()
    heap_output = heapSort_max(arr)
    heap_time = time.perf_counter() - start

    start = time.perf_counter()
    numpy_output = np.sort(arr)
    numpy_time = time.perf_counter() - start

    # Check that both methods returned the same sorted values.
    assert heap_output == numpy_output.tolist()

    print(f"Runtime comparison for {n:,} integers:")
    print(f"Heap Sort time: {heap_time:.6f} sec")
    print(f"NumPy Sort time: {numpy_time:.6f} sec")


# -----------------------------------------
# Demo and test cases
# -----------------------------------------
if __name__ == "__main__":
    data = [3, 9, 2, 1, 4, 5]
    print("Original array:", data, "\n")

    min_heap_data = data.copy()
    build_min_heap(min_heap_data)
    print("After min heapify array:", min_heap_data, "\n")

    max_heap_data = data.copy()
    build_max_heap(max_heap_data)
    print("After max heapify array:", max_heap_data, "\n")

    print("QUESTION 2: HEAPSORT TESTS")
    lecture_example = [70, 40, 60, 10, 20, 30, 50]
    custom_example = [18, 4, 27, 12, 9, 31, 6, 22, 15, 2, 19, 8, 25, 11, 3, 30]
    edge_cases = [
        ([], []),
        ([7, 7, 7, 7], [7, 7, 7, 7]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
    ]

    for label, test_array in [
        ("Lecture example", lecture_example),
        ("Custom array (16 numbers)", custom_example),
    ]:
        print(f"\n{label}: {test_array}")
        max_result = heapSort_max(test_array)
        min_result = heapSort_min(test_array)
        print("Max-heap heapsort:", max_result)
        print("Min-heap heapsort:", min_result)
        assert max_result == sorted(test_array)
        assert min_result == sorted(test_array)

    print("\nEdge cases:")
    for index, (test_array, expected) in enumerate(edge_cases, start=1):
        max_result = heapSort_max(test_array)
        min_result = heapSort_min(test_array)
        print(f"Arr{index}: {test_array}")
        print(f"Expected{index}: {expected}")
        print(f"Max-heap result: {max_result}")
        print(f"Min-heap result: {min_result}")
        assert max_result == expected
        assert min_result == expected

    print("\nAll required test cases passed.")
    check_stability(heapSort_max, "Max-heap heapsort")
    check_stability(heapSort_min, "Min-heap heapsort")

    # Extra randomized correctness checks.
    random.seed(123)
    for _ in range(255):
        test_array = [random.randint(-100, 100) for _ in range(random.randint(0, 30))]
        assert heapSort_max(test_array) == sorted(test_array)
        assert heapSort_min(test_array) == sorted(test_array)
    print("255 additional randomized tests passed for both algorithms.\n")

    benchmark()
