# single and double quotes - No difference
print("This is string")
print(2)
print(3.5)

print(20 * 24 * 60)
print("20 days have " + str(20 * 24 * 60) + " min")
print(f"20 days have {20 * 24 * 60} min")  # f stands for format

calculate_to_sec = 20 * 24 * 60 * 60
duration = "sec"

print(f"20 days have { calculate_to_sec } {duration}")
