def days_to_unit(days: int, unit: str):
    min_unit = days * 24 * 60
    print(f"{days} days have {min_unit} {unit}")
    print("All Good!")


days_to_unit(25, "min")
