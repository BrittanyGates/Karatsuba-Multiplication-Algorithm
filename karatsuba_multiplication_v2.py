#!/usr/bin/python3
"""Karatsuba Multiplication
My implementation of the multiplication algorithm that works correctly with parameters of different sizes.
I fixed my code from v1 using hints from Gemini Canvas.
"""


def karatsuba(digit_1: int, digit_2: int) -> int:
    """Divides the n-digits and multiplies them.
    :param digit_1: The first digit.
    :param digit_2: The second digit.
    :return: The product of the two digits.
    """
    # Base cases
    if digit_1 == 0 or digit_2 == 0:
        return 0
    elif digit_1 < 10 or digit_2 < 10:
        return digit_1 * digit_2
    # End of base cases
    else:
        # Convert parameters to strings
        digit_1_string: str = str(digit_1)
        digit_2_string: str = str(digit_2)

        # Find the length of both strings
        digit_1_string_length: int = len(digit_1_string)
        digit_2_string_length: int = len(digit_2_string)

        # Find the max length of the strings
        digit_string_max_length: int = max(digit_1_string_length, digit_2_string_length)

        # Pad the shorter string with zeroes on the left
        digit_1_string: str = digit_1_string.zfill(digit_string_max_length)
        digit_2_string: str = digit_2_string.zfill(digit_string_max_length)

        # Find the midpoints of each string
        midpoint_of_digit_string_max_length: int = digit_string_max_length // 2

        # Use slice
        first_half_of_digit_1_string: str = digit_1_string[:midpoint_of_digit_string_max_length]
        second_half_of_digit_1_string: str = digit_1_string[midpoint_of_digit_string_max_length:]
        first_half_of_digit_2_string: str = digit_2_string[:midpoint_of_digit_string_max_length]
        second_half_of_digit_2_string: str = digit_2_string[midpoint_of_digit_string_max_length:]

        # Convert the strings back into integers
        first_half_of_digit_1: int = int(first_half_of_digit_1_string)
        second_half_of_digit_1: int = int(second_half_of_digit_1_string)
        first_half_of_digit_2: int = int(first_half_of_digit_2_string)
        second_half_of_digit_2: int = int(second_half_of_digit_2_string)

        # Add the numbers together before performing the multiplication operation.
        digit_1_sum: int = first_half_of_digit_1 + second_half_of_digit_1
        digit_2_sum: int = first_half_of_digit_2 + second_half_of_digit_2

        # Perform the recursive calls to multiply the numbers.
        product_of_first_half: int = karatsuba(first_half_of_digit_1, first_half_of_digit_2)
        product_of_second_half: int = karatsuba(second_half_of_digit_1, second_half_of_digit_2)
        product_of_the_sum_of_both_halves: int = karatsuba(digit_1_sum, digit_2_sum)

        # Per the algorithm's design I need to subtract all the products
        subtraction_total: int = product_of_the_sum_of_both_halves - product_of_first_half - product_of_second_half

        # Now to add trailing zeroes to the product in the first half
        shift_amount: int = digit_string_max_length - midpoint_of_digit_string_max_length

        # Then add trailing zeroes to the subtraction total
        shift_midpoint: int = 2 * shift_amount

        final_result: int = (product_of_first_half * 10 ** shift_midpoint) + (
                subtraction_total * 10 ** shift_amount) + product_of_second_half

        return final_result


print(karatsuba(7894, 12))  # Answer: 94728
print(karatsuba(25, 1425))  # Answer: 35625
print(karatsuba(456, 918))  # Answer: 418608
print(karatsuba(8965, 7412))  # Answer: 66448580
print(karatsuba(456788124585, 741859638574))  # Answer: 3.38872673×10²³
