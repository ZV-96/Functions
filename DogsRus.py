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


def pick_up():
    dog_pickup = str(input("What is the name of the dog you want to pick up"))
    if dog_pickup in dog_list:
        confirm = str(input("Confirm your choice(Y/N): ")).upper()
        if confirm == "Y":
            print(f"{dog_pickup} has been removed from the list")
            dog_list.remove(dog_pickup)
            main_function()
        else:
            main_function()
    else:
        print("dog name is not in list")
        main_function()


def calc_cost(number):
    days = int(input("how many days are your dogs staying"))
    rate = 22.50
    cost = days*rate*number
    confirm = str(input("Do you want to calculate the cost(Y/N): ")).upper()
    if confirm == "Y":
        print(f"Your cost for {days} days and {number} dogs is {cost}")
        main_function()
    else:
        main_function()


def print_roll():
    confirm = str(input("would you like to view the list(Y/N): ")).upper()
    if confirm == "Y":
        print(f"this is the list: {dog_list}")
        main_function()
    else:
        main_function()


def terminate_program():
    confirm = str(input("Are you sure you want to quit(Y/N): ")).upper()
    if confirm == "Y":
        print("Thanks for using DogsRus today")
    else:
        main_function()

