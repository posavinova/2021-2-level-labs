"""
Programming 2021
Seminar 3
Data Type: Integer
"""


# Three main ideas:
# 1. In Python, numbers are represented as int, float, or complex.
# 2. To check the data type of a number, you need to call type() function.
# 3. Numbers can only be added and subtracted with numbers
#       and not with other data types, like strings and lists.


# General integer understanding:
first_number = 5
print(first_number, 'is of type', type(first_number))

# float
second_number = 2.0
print(second_number, 'is of type', type(second_number))

# complex
third_number = 1 + 2j
print(third_number, 'is of type', type(third_number))


# Task 1:
def sorta_sum(num_a, num_b):
    """
    Given two numbers as input, return their sum.
    If the resulting sum is in range of [10, 20], return 20 instead.
    """
    # student realisation goes here


# Function calls with expected result:
sorta_sum(3, 4)  # 7
sorta_sum(9, 4)  # 20
sorta_sum(10, 11)  # 21
sorta_sum(4, 6)  # 20
sorta_sum(12, -3)  # 9
sorta_sum(14, 6)  # 20


# Task 2:
def party(num_nuts, is_weekend):
    """
    When squirrels are going to a party, they love to nibble on nuts.
    A squirrel party is considered successful if the number of nuts is between 40 and 60, inclusive.
    If it is a weekend (is_weekend parameter is True), there is no upper limit on the number of nuts.
    Return True if the party is successful, False otherwise.
    """
    # student realisation goes here


# Function calls with expected result:
party(30, False)  # False
party(50, False)  # True
party(70, True)  # True
party(61, False)  # False
party(39, False)  # False
party(39, True)  # False


# Task 3:
def lone_sum(num_1, num_2, num_3):
    """
    Given three integer values as input, return their sum.
    However, if one of the values is the same as any other,
        they are both ignored in calculating the amount.
    """
    # student realisation goes here


# Function calls with expected result:
lone_sum(1, 2, 3)  # 6
lone_sum(3, 2, 3)  # 2
lone_sum(3, 3, 3)  # 0
lone_sum(2, 9, 2)  # 9
lone_sum(2, 9, 3)  # 14
lone_sum(1, 3, 1)  # 3


# Task 1: advanced
def caught_speeding(speed_num, is_birthday):
    """
    You are driving too fast and a police officer stops you.
    Write code to compute the result, encoded as an int:
        0 = no penalty,
        1 = small penalty,
        2 = large penalty.
    If the speed is 60 or less, the result is 0.
    If the speed is between 61 and 80 inclusive, the result is 1.
    If the speed is 81 or more, the result is 2.
    If it is your birthday, the speed can be 5 more in all cases.
    """
    # student realisation goes here


# Function calls with expected result:
caught_speeding(60, False)  # 0
caught_speeding(65, False)  # 1
caught_speeding(65, True)  # 0
caught_speeding(85, True)  # 1
caught_speeding(75, True)  # 1
caught_speeding(40, False)  # 0
caught_speeding(90, False)  # 2


# Task 2: advanced
def close_far(num_1, num_2, num_3):
    """
    Given three integers as input, return True
        if any two values are "close" (differ by no more than 1),
        and the other is "far", differing from both other values by 2 or more.
    """
    # student realisation goes here


# Function calls with expected result:
close_far(1, 2, 10)  # True
close_far(1, 2, 3)  # False
close_far(4, 1, 3)  # True
close_far(4, 5, 3)  # False
close_far(10, 10, 8)  # True
close_far(8, 9, 10)  # False
close_far(0, -1, 10)  # True
close_far(-1, 10, 0)  # True
close_far(8, 6, 9)  # True
