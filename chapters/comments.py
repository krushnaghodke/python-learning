# In list we can store multiple data item together. [12, 23, 34, 44]

calculate_to_value = 24
name_of_unit = "hours"


def days_to_unit(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculate_to_value} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        # check value is greater than 0
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0 value...")
        else:
            print("Please enter valid integer value....")
    except ValueError:
        print("Your input is not a number...")


user_input = ""


while user_input != 'Exit':
    user_input = input("Hey user, enter no of days i will convert it to hours\n")
    print(type(user_input.split(", ")))
    print(user_input.split(", "))
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()
