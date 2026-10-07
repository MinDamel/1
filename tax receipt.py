name_of_shop = "Jenny's Market"

Item = input("What item are you buying?\n")

Price = round(float(input("How much is it?\n")),2)

Tax = round(Price * 0.075,2)

Cost = round(Price + Tax,2)

Receipt = f"{name_of_shop}\n Item: {Item}\n Price: {Price}\n Tax: {Tax}\n Cost: {Cost}"

print(Receipt)