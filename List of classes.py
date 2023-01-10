classes = []

#Asks and adds classes to class list
while True:
    className = input("Enter class: ")
    classes.append(className)
    loop = input("Do you have anymore classes? y/n: ")
    if loop == "n": #Loop breaks if user inputs "n"
        break

#prints classes
print("Your classes are:")
for className in classes:
    print(className)