"""Even number function"""


def is_even(number=range(11)):
    """Returns even number.

    :param number: int contains the number.
    :param even_lst: contains the even numbers.
    :return: list returns list with even numbers.

    Function that takes the number in int, then we go through
    the numbers starting with 2 across 1.
    """
    # List to contain even numbers
    even_lst = []
    # Enumerate elements with for loop, starting with 2 across 1
    for num in range(1, len(number)):
        if num % 2 == 0:
            # Appened even numbers in even_lst
            even_lst.append(num)
    # Return all even numbers
    return (even_lst)


# Call function with print function
even_num = is_even()
print(even_num)