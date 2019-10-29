a = [int(x) for x in input().split()]
x = len(a)
b = []

for i in range(x):
    if(a[i]%5 != 0):
        b.append(a[i])
        
        

z = len(b)

for i in range(z):
    if(i != z-1):
        print(b[i],end=" ")
    else:
        print(b[i],end="")