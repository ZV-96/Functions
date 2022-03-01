""" Function to print name multiple times
"""

def print_name(name, number):
    for person in range(0, number):
        print(name)


# Main Routine
name_ = input("insert name to print: ")
number_ = int(input("Times to print: "))
print_name(name_, number_)
