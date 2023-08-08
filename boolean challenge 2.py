# Write a program to print all the ASCII values and their equivalent characters 
# using a while loop. The ASCII values vary from 0 to 255.


'''i=0
while i <= 255:
    print(f"{i} :", chr(i))
    i += 1'''


# Write a program to print all prime numbers from 1 to 300. (Hint: Use nested loops, break and continue)


'''for i in range(1,301):
    n = 2
    while n < i:
        if i % n == 0:
            break
        n += 1  
    if i == n:
        print(i)
        continue  '''



# Write a program to generate all combinations of 1, 2 and 3 using for loop.
values = [1, 2, 3]
for i in values:
    for j in values:
        for k in values:
            if i == j == k or i == j or j == k or k == j or k == i:
                continue
            else:
                print(i, j, k)


