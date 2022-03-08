# accept user input of goal and deadline date
# print out how much time remaining till deadline?
import datetime

user_input = input("enter a goal with deadline separated by colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.datetime.strptime(deadline, "%d.%m.%Y")
# calculate days from now to deadline
print(deadline_date)
today = datetime.datetime.today()
time_till = deadline_date - today

print(f"Dear user! time remaining for your goal: {goal} is {time_till.days} days")
