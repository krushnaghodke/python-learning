# Dictionary is a key value pair which do not allow duplicate values.


def days_to_unit(num_of_days, conversion_unit):
    if conversion_unit == "hrs":
        calculate_to_value = 24
        return f"{num_of_days} days are {num_of_days * calculate_to_value} {conversion_unit}"
    elif conversion_unit == "min":
        calculate_to_value = 24 * 60
        return f"{num_of_days} days are {num_of_days * calculate_to_value} {conversion_unit}"
    else:
        return "unsupported unit"


def validate_and_execute():
    try:
        user_input_number = int(days_and_unit_dict["days"])
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number, days_and_unit_dict["unit"])
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
    days_and_unit = user_input.split(":")
    days_and_unit_dict = {'days': days_and_unit[0], 'unit': days_and_unit[1]}
    print(days_and_unit)
    print(days_and_unit_dict)
    validate_and_execute()

my_list = ["23", "34", "45"]
print(my_list[2])
