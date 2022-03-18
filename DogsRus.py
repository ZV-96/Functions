def main_function():
    print("--------------- Welcome to DogsRus Dog sitting ---------------")
    print("What do you want to do today: ")
    print("1 Drop off a dog")
    print("2 pick up a dog")
    print("3 calculate cost")
    print("4 print dog list")
    print("5 quit")

    choice = int(input("Enter your choice(Must be between 1 and 5): "))
    if choice == 1:
        drop_off()
    elif choice == 2:
        pick_up()
    elif choice == 3:
        calc_cost(len(dog_list))
    elif choice == 4:
        print_roll()
    elif choice == 5:
        terminate_program()
    else:
        print("That is not a number between 1 and 5")
        main_function()


def drop_off():
    confirm = str(input("Would you like to drop off a dog(Y/N): ")).upper()
    if confirm == "Y":
        dog_name = str(input("What is your dogs name: "))
        dog_list.append(dog_name)
        print(f"{dog_name} has been added to the list")
        main_function()
    else:
        main_function()



