def check_factor(list1, multiple):
    new_list = []
    for num in list1:
        if num % multiple == 0:
            new_list.append(num)
    return new_list


# Main Routine
list_ = [1, 4, 6, 7, 15, 22, 35]

print(check_factor(list_, 5))
print(check_factor(list_, 2))
