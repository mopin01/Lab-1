from datetime import datetime

#gets name, birthday month, and current month
name = input("What is your name: ")
birthdayMonth = input("What is your birthday month: ")
currentMonth = datetime.now().month

#prints name and total letters in name
print("Hello " + name)
print("The number of letters in your name is " + str(len(str(name))))

#compares birthday month with current month
if int(birthdayMonth) == currentMonth:
    print("Happy birthday month!")