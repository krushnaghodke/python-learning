convertor = 24
custom_message = "All Good!"


def days_to_unit(days: int, unit: str):
    min_unit = days * 24 * 60
    print(f"{days} days have {min_unit} {unit}")


def scope_check():
    print(custom_message)


days_to_unit(25, "min")
days_to_unit(35, "min")
days_to_unit(45, "min")
days_to_unit(55, "min")
scope_check()
