t=int(input())
for i in range(t):
    X,Y=map(int,input().split()) #changes each element after splitting into integer values
    # eg - 15 20 given as input is split into ["15","20"] and then turned into integers
    print(max(X,Y))