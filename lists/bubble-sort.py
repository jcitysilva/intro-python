def bubble_sort(lst):
    """
    Sorts a list using the bubble sort algorithm.
    
    Args:
    lst (list): The list to be sorted.
    
    Complexity:
    Time: O(n^2) - Quadratic time complexity due to nested loops, the algorithm may need to traverse the entire list to ensure it is in the correct position.
    Space: O(1) - Constant space complexity as the sorting is performed in-place. The number of swaps in bubble sort equals the number of inversion pairs in the given array.
                  It does not use any additional data structures to perform the sorting operation, making it memory efficient for sorting small lists.
    """
    last_index = len(lst) - 1
    no_swap = False  # Ensures the while loop is executed
    while not no_swap:
        no_swap = True
        for i in range(last_index):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                no_swap = False
        last_index -= 1

# Example of using bubble sort
numbers = [64, 34, 25, 12, 22, 11, 90]
print("Original list:", numbers)

bubble_sort(numbers)

print("Sorted list:", numbers)
