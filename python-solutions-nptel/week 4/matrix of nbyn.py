a = [int(x) for x in input().split()]

b = a[0]
c = a[1]
x = 1
for i in range(b):
    for j in range(c):
        if(j!=c-1):
            print(x,end=" ")
            x+=1
        else:
            print(x,end="\n")
            x+=1
            