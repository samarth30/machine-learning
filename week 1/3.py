n = int(input())

a = [int(x) for x in input().split()]

x = a[::-1]

for i in range(n):
    if(i!= n-1):
        print(a[i]+x[i],end=" ")    
    else:
        print(a[i]+x[i],end="")
