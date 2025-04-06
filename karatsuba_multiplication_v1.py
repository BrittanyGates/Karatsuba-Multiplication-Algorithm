#!/usr/bin/python3
"""Karatsuba Multiplication
My implementation of the multiplication algorithm. However, it doesn't work correctly if the parameters aren't the
same size.
"""


def karatsuba(digit_1: int, digit_2: int) -> int:
    """Divides the n-digits and multiplies them.
    :param digit_1: The first digit.
    :param digit_2: The second digit.
    :return: The product of the two digits.
    """

    def split_list(digit_list: list) -> tuple[list[int], list[int]]:
        """Determine the midpoints of the list containing the digits and slicing it at the midpoint.
        :param digit_list: The list containing the n-digits.
        :return: A tuple of lists containing at least one integer.
        """
        digit_list_len: int = len(digit_list)
        digit_list_midpoint: int = digit_list_len // 2
        first_half_of_digit_list: list[int] = digit_list[:digit_list_midpoint]
        second_half_of_digit_list: list[int] = digit_list[digit_list_midpoint:]

        return first_half_of_digit_list, second_half_of_digit_list

    def get_numbers(digit_list: list) -> int:
        """Remove the digits from each list and puts it into a variable.
        :param digit_list: The list containing the n-digits.
        :return: The results of all integers in the list.
        """
        result: str = ""

        if not digit_list:
            return 0
        else:
            for number in digit_list:
                number = str(number)
                result += number

            result: int = int(result)

            return result

    # Base cases
    if digit_1 == 0 or digit_2 == 0:
        return 0
    elif digit_1 < 10 or digit_2 < 10:
        return digit_1 * digit_2
    # End of base cases
    else:
        digit_1_list: list = []
        digit_2_list: list = []

        # Pops off the last digit from the input.
        while digit_1 and digit_2 > 0:
            digit_1_digit = digit_1 % 10
            digit_2_digit = digit_2 % 10
            digit_1_list.insert(0, digit_1_digit)
            digit_2_list.insert(0, digit_2_digit)
            digit_1 //= 10
            digit_2 //= 10

        # Split the lists and get the numbers from each to perform math operations.
        digit_1_list_a, digit_1_list_b = split_list(digit_1_list)
        digit_1_list_a_numbers, digit_1_list_b_numbers = get_numbers(digit_1_list_a), get_numbers(digit_1_list_b)

        digit_2_list_c, digit_2_list_d = split_list(digit_2_list)
        digit_2_list_c_numbers, digit_2_list_d_numbers = get_numbers(digit_2_list_c), get_numbers(digit_2_list_d)

        # Add the numbers together before performing the multiplication operation.
        digit_1_list_sum: int = digit_1_list_a_numbers + digit_1_list_b_numbers
        digit_2_list_sum: int = digit_2_list_c_numbers + digit_2_list_d_numbers

        # Perform the recursive calls to multiply the numbers.
        product_of_first_half: int = karatsuba(digit_1_list_a_numbers, digit_2_list_c_numbers)
        product_of_second_half: int = karatsuba(digit_1_list_b_numbers, digit_2_list_d_numbers)
        product_of_the_sum_of_both_lists: int = karatsuba(digit_1_list_sum, digit_2_list_sum)

        # Per the algorithm's design I need to subtract all the products
        subtraction_total: int = product_of_the_sum_of_both_lists - product_of_first_half - product_of_second_half

        # Now to add trailing zeroes to the product in the first half
        shift_amount: int = len(digit_1_list_b)

        # Then add trailing zeroes to the subtraction total
        shift_midpoint: int = 2 * shift_amount

        final_result: int = (product_of_first_half * 10 ** shift_midpoint) + (
                subtraction_total * 10 ** shift_amount) + product_of_second_half

        return final_result


print(karatsuba(7894, 12))  # This case doesn't provide the right answer
print(karatsuba(78, 128))  # This case doesn't provide the right answer
print(karatsuba(456, 918))  # Answer: 418608
print(karatsuba(8965, 7412))  # Answer: 66448580
print(karatsuba(456788124585, 741859638574))  # Answer: 3.38872673×10²³
