a = [int(x) for x in input().split()]

a1 = sorted(a)
count = 0
for i in range(len(a)):
    if(a[i] != a1[i]):
        count+=1

print(count,end="")        