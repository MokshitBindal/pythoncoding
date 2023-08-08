print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want extra pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0
'''if size in ["s", "S"]:
    bill = 150
elif size in ["m", "M"]:
    bill = 200
elif size in ["l", "L"]:
    bill = 250

if size in ["s", "S"] and add_pepperoni in ["y", "Y"]:
    bill += 10
elif size in ["m", "M", "l", "L"] and add_pepperoni in ["y", "Y"]:
    bill += 30

if extra_cheese in ["y", "Y"]:
    bill += 10

print(f"Your total bill is {bill}rs")
'''

if size in ["s", "S"]:
    bill = 150
elif size in ["m", "M"]:
    bill = 200
else:
    bill = 250

if add_pepperoni in ["y", "Y"]:
    if size in ["s", "S"]:
        bill += 10
    else:
        bill += 30

if extra_cheese in ["y", "Y"]:
    bill += 10

print(f"Your total bill is {bill}rs")
