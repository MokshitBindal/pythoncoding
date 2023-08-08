# armstrong numbers between 1 and 500
# armstrong number is like 153, cube of 1 + 5 + 3 gives 153
'''sum = 0
for i in range(1,501):
    a = str(i)
    count1 = len(a)
    if count1 == 1:
        sum = i*i*i
        if sum == i:
            print(i)
    elif count1 == 2:
        p,q = int(a[0]) , int(a[1])
        sum = p*p*p + q*q*q
        if sum == i:
            print(i)
    elif count1 == 3:
        p,q,r = int(a[0]) , int(a[1]) , int(a[2])
        sum = p*p*p + q*q*q + r*r*r
        if sum == i:
            print(i)'''


# 5 digit number is given add 1 to each
'''num = int(input("enter a 5 digit number: "))
print(num + 11111)'''


# print the kth element from list where the smallest element is k


list1 = [7,10,4,3,20,15]
list2 = sorted(list1)
print(list1)
print(list2)
k = list2[0]
if k<=len(list2):
    print(list2[k-1])
else:
    print("list is smaller than k")