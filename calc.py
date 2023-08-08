first = int(input("enter first number"))
second = int(input("enter second number"))
operation = input("enter the operator[+,-,*,/]")


def multiply():
    return first * second


def add():
    return first + second


def subtract():
    return first - second


def divide():
    return first / second


if operation == "+":
    print(add())
elif operation == "-":
    print(subtract())
elif operation == "*":
    print(multipy())
elif operation == "/":
    print(divide()
          )

input()
