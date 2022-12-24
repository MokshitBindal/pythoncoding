# FIND age of a person born on 29,FEB.



def leap_year_finder(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


print("        Welcome to 29,FEB age finder.      ")
age = 0
birthyear = int(input("In which leap year you were born? "))
if leap_year_finder(birthyear) == True:
    for i in range(birthyear+1,2023):
        if leap_year_finder(i) == True:
            age += 1
    print("You are {} years old".format(age))
else:
    print("give a leap year as input.")
