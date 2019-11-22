n,v1,v2 = input().split()

n = int(n)
v1 = int(v1)
v2 = int(v2)

d1 = pow(2,1/2)*n
t1 = d1/v1

d2 = n*2
t2 = d2/v2

if(t1>t2):
    print("cab",end="")
else:
    print("walk",end="")

