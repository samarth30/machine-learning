a = int(input())
b  =[]
for i in range(a):
    x = int(input())
    b.append(x)

b.sort()

for i in range(a):
    if(i != a-1):
        print(b[i],end=" ")
    else:
        print(b[i],end="")