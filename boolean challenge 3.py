# Write a program to add first seven terms of the following series
# using a for loop: 1/1! + 2/2! + 3/3! +.....

'''
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)

sum = 0
for i in range(1,8):
    sum += i/factorial(i)
print(sum)
'''

# According to a study, the approximate level of intelligence of a person
# can be calculated using the following for         1=2+(y+05x)
# Write a program, which will produce a table of values of i, y and x,
# where y varies from 1 to 6, and, for each value of y, x varies from 5.5 to 12.5 in steps of 0.5.

'''
x_range = [5.5,6,6.5,7,7.5,8,8.5,9,9.5,10,10.5,11,11.5,12,12.5]
print("i | y | x")
for y in range(1,7):
    for x in x_range:
        i = 2 + (y + 0.5*x)
        print(f"{i} | {y} | {x}")
'''


#   ABCDEFGFEDCBA
#   ABCDEF FEDCBA
#   ABCDE   EDCBA
#   ABCD     DCBA
#   ABC       CBA
#   AB         BA
#   A           A

spaces = 3
char = ['A','B','C','D','E','F']
rev_char = sorted(char, reverse= True)
print("".join(char)+"G"+"".join(rev_char))
print("".join(char)+" "+"".join(rev_char))
for i in range(len(char)-1,-1,-1):
    char.pop(i)
    rev_char.pop(-(i+1))
    print("".join(char)+" "*spaces+"".join(rev_char))
    spaces += 2




