n = int(input())

l = []

for i in range(n):
    for j in range(1):
        temp = [int(x) for x in input().split()]
        l.append(temp)
        
        
for i in range(n):
    for j in range(n):
        if(i<j):
            if(j!=n-1):
                print(0,end=" ")
            else:
                print(0,end="\n")
        else:
            if(j!=n-1):
                print(l[i][j],end=" ")
            else:
                print(l[i][j],end="\n")
                