print("Welcome to the love calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# t,r,u,e,l,o,v = 0,0,0,0,0,0,0
total_t = name1.count("t") + name2.count("t")
total_r = name1.count("r") + name2.count("r")
total_u = name1.count("u") + name2.count("u")
total_e = name1.count("e") + name2.count("e")
total_l = name1.count("l") + name2.count("l")
total_o = name1.count("o") + name2.count("o")
total_v = name1.count("v") + name2.count("v")

true = str(total_t + total_r + total_u + total_e)
love = str(total_l + total_o + total_v + total_e)

love_score = true + love
int_score = int(love_score)

# or love_score = int(str(true) + str(love))

if int_score < 10 or int_score > 90:
    print(f"Your love score is {int_score},You go together like coke and mentos")
elif int_score >= 40 and int_score <= 50:
    print(f"Your love score is {int_score},You are alright together")
else:
    print(f"Your love score is {int_score}")
