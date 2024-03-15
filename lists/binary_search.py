def binary_search(lst, key):
    """
    Performs a binary search to find the index of a key in a sorted list.
    
    Args:
    lst (list): The sorted list to search.
    key: The key to search for.
    
    Returns:
    int: The index of the key in the list if found, otherwise -1.
    """
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if key == lst[mid]:
            return mid
        elif key > lst[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Example usage of the search algorithms
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = 23

# Binary search
print("\nBinary Search:")
index_bin = binary_search(numbers, target)
if index_bin != -1:
    print("Target found at index:", index_bin)
else:
    print("Target not found in the list.")

# This function implements the binary search algorithm, which efficiently finds the index of a target element in a sorted list.
# It works by repeatedly dividing the search interval in half until the target element is found or the interval is empty.
# Time complexity: O(log n).
