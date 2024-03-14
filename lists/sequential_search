def sequential_search(lst, key):
    """
    Performs a sequential search in a list for a specific key.

    Args:
    lst (list): The list to search through.
    key: The value to search for in the list.

    Returns:
    int: The index of the key in the list if found, otherwise -1.
    """
    for i in range(len(lst)):
        if lst[i] == key:
            return i
    return -1

lst = [2, 3, 1, -4, 12, 9]
print(sequential_search (lst, 1))
print(sequential_search (lst,5))

# The sequential_search function iterates through each element of the list.
# If the current element matches the key, it returns the index of that element.
# If the key is not found in the list, it returns -1.
# Using else return -1 after the for loop in the sequential search algorithm is redundant because if the loop completes without finding the key, it automatically falls through to the return -1 statement.
