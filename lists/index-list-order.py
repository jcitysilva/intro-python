def bubble_sort_index(lst):
    """
    Sorts a list using the Bubble Sort algorithm and returns a list of indices.

    Args:
    lst (list): The list to be sorted.

    Returns:
    list: A list of indices representing the sorted order of elements.
    """
    # Initialize variables
    n = len(lst)
    indices = list(range(n))
    no_swap = False

    # Perform bubble sort
    while not no_swap:
        no_swap = True
        for i in range(n - 1):
            if lst[indices[i]] > lst[indices[i + 1]]:
                # Swap indices
                indices[i], indices[i + 1] = indices[i + 1], indices[i]
                no_swap = False

    return indices

# Example usage
unsorted_list = [5, 2, 9, 1, 6]
sorted_indices = bubble_sort_index(unsorted_list)

print("Original list:", unsorted_list)
print("Sorted indices:", sorted_indices)
print("Sorted list:")
for index in sorted_indices:
    print(unsorted_list[index], end=" ")

#O(n^2), where n is the size of the input list
#The space complexity is O(1)
