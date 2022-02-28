def make_positive(number):
    abs_value = abs(number)
    return abs_value


# Main routine
number_to_check = int(input("input a number to check: "))
print(f"The absolute value of {number_to_check} is {make_positive(number_to_check)}")
