def swap_value(a, b):
    """
    Swaps the values of two variables (pass by value).
    
    Args:
    a: First variable.
    b: Second variable.
    
    Returns:
    tuple: A tuple containing the swapped values.
    """
    return b, a

def swap_reference(lst):
    """
    Swaps the values of two elements in a list (pass by reference).
    
    Args:
    lst (list): The list containing elements to be swapped.
    """
    temp = lst[0]
    lst[0] = lst[1]
    lst[1] = temp

# Pass by value example
x = 10
y = 20
print("Before swap (pass by value):")
print("x:", x)
print("y:", y)

x,y = swap_value(x, y)

print("\nAfter swap (pass by value):")
print("x:", x)  # No change
print("y:", y)  # No change

# Pass by reference example
numbers = [10, 20]
print("\nBefore swap (pass by reference):")
print("numbers:", numbers)

swap_reference(numbers)

print("\nAfter swap (pass by reference):")
print("numbers:", numbers)  # List has been modified


# In this example, for pass by value swapping, we pass the variables x and y to the swap_value function.
# Despite swapping the values within the function, the original variables x and y remain unchanged.
# For pass by reference swapping, we pass the list numbers to the swap_reference function.
# Within the function, the positions of the elements in the list are swapped.
# After calling the function, the original list numbers is modified, demonstrating that passing a list to functions in Python is by reference.
