"""Even number function"""
# List to contain even numbers
even_lst = []


def is_Even(number=range(int(input()))):
    """Returns even number.

    :param number: int contains the number.
    :param even_lst: contains the even numbers.
    :return: list returns list with even numbers.

    Function that takes the number in int, then we go through 
    the numbers starting with 2 across 1.
    """
    # Enumerate elements with for loop, starting with 2 across 1
    for element in range(2, len(number), 2):
        # Appened even numbers in even_lst
        even_lst.append(element)
    # Return all even numbers
    return even_lst


# Call function with print function
print(is_Even())
