def day_of_week(number):
    if number == 1:
        return "Monday"
    elif number == 2:
        return "Tuesday"
    elif number == 3:
        return "Wednesday"
    elif number == 4:
        return "Thursday"
    elif number == 5:
        return "Friday"
    elif number == 6:
        return "Saturday"
    elif number == 7:
        return "Sunday"
    else:
        return "Invalid input. Please enter a number between 1 and 7."

num = int(input("Enter a number (1-7): "))
print(day_of_week(num))
