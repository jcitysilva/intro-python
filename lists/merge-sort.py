def merge_sort(array):
    """
    Sorts an array using the Merge Sort algorithm.
    
    Args:
    array (list): The unsorted array.
    
    Returns:
    list: The sorted array.
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    # Base case: return array if it has only one element
    if len(array) == 1:
        return array
    
    # Divide the array into two halves
    mid_point = len(array) // 2
    left = array[:mid_point]
    right = array[mid_point:]

    # Recursively call merge_sort on each half
    left = merge_sort(left)
    right = merge_sort(right)

    # Merge the sorted halves
    return merge(left, right)

def merge(left, right):
    """
    Merges two sorted arrays into a single sorted array.
    
    Args:
    left (list): The left sorted array.
    right (list): The right sorted array.
    
    Returns:
    list: The merged sorted array.
    """
    merged_arr = []

    # Merge the two halves while both are non-empty
    while left and right:
        if left[0] <= right[0]:
            merged_arr.append(left.pop(0))
        else:
            merged_arr.append(right.pop(0))

    # Add remaining elements from left or right subarray
    merged_arr.extend(left if left else right)

    return merged_arr

# Example usage
arr = [3, 7, 2, 1, 9, 5, 4, 6, 8]
sorted_arr = merge_sort(arr)
print("Sorted Array:", sorted_arr)
