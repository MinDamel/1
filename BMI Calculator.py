weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in kg? "))

bmi = round((weight/height**2),2)

print(f"Your Body Mass Index is: {bmi}")