n = int(input())

l = []

for i in range(n):
    for j in range(1):
        temp = [int(x) for x in input().split()]
        l.append(temp)
        
flag=0        
for i in range(n):
    for j in range(n):
        if(l[i][j] != l[j][i]):
            flag= 1
            
if(flag == 1 ):
    print("no",end="")
else:
    print("yes",end="")