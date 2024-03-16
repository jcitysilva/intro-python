def shell_sort(lst):
    """
    Sorts a list using the Shell sort algorithm.

    Args:
    lst (list): The list to be sorted.

    Returns:
    None. The list is sorted in-place.
    """
    # Initialize interval to half the length of the list
    interval = len(lst) // 2
    
    # Continue until the interval becomes 0
    while not interval == 0:
        # Initialize flag to track if any swaps were made
        no_swaps = False
        
        # Continue until no swaps are made within the current interval
        while not no_swaps:
            no_swaps = True
            
            # Iterate over the list within the current interval
            for i in range(len(lst) - interval):
                # Compare elements separated by the current interval
                if lst[i] > lst[i + interval]:
                    # Swap elements if they are out of order
                    lst[i], lst[i + interval] = lst[i + interval], lst[i]
                    # Set flag to False to indicate a swap occurred
                    no_swaps = False
        
        # Reduce the interval by half for the next iteration
        interval = interval // 2

# Example of using Shell sort
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)

shell_sort(numbers)

print("Sorted list:", numbers)

# Shellsort is an unstable comparison sort algorithm with variable performance.
# It improves on insertion sort by breaking the original list into smaller sublists,
# which are then sorted using insertion sort. The time complexity of Shellsort depends
# on the chosen sequence of intervals but is generally better than insertion sort,
# with an average/worst-case time complexity of O(n(log(n))^2) and O(n(log(n))) in the best case.
# Despite its better average performance, Shellsort can still have poor performance on certain inputs
# and is less commonly used compared to more efficient sorting algorithms like quicksort and mergesort.
