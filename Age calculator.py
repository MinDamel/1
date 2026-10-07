Age = int(input("How old are you? "))

Age_in_days = Age * 365

Age_in_hours = Age_in_days * 24

Age_in_minutes = Age_in_hours * 60

age = f"You are roughly {Age_in_days} days, {Age_in_hours} hours, and {Age_in_minutes} minutes old."
print(age)