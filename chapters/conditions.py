calculate_to_value = 24
name_of_unit = "hours"


def days_to_unit(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculate_to_value} {name_of_unit}"


def validate_and_execute():
    try:
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            return "you entered 0 value..."
        else:
            return "Please enter valid integer value...."
    except ValueError:
        return "Your input is not a number..."


user_input = input("Hey user, enter no of days i will convert it to hours\n")
validate = validate_and_execute()
print(validate)
