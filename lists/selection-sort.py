def selection_sort(lst):
    """
    Sorts a list using the selection sort algorithm.
    
    Args:
    lst (list): The list to be sorted.
    
    Returns:
    list: The sorted list.
    """
    n = len(lst)
    for i in range(n):
        # Assume the current index has the minimum value
        min_index = i
        # Find the index of the minimum element in the unsorted portion of the list
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        # Swap the minimum element with the first element of the unsorted portion
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst

# Time complexity of selection sort: O(n^2) - quadratic time complexity
# Space complexity: O(1) - constant space complexity
# We use only constant extra space such as: 2 variables to enable swapping of elements.

# Example usage:
numbers = [64, 25, 12, 22, 11]
print("Before sorting:", numbers)
sorted_numbers = selection_sort(numbers)
print("After sorting:", sorted_numbers)
