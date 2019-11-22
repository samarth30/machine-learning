x = int(input())

a = [int(l) for l in input().split()]

k = int(input())
n = a[k-1]

a = sorted(a)

for i in range(len(a)):
    if(a[i] == n):
        print(i+1,end="")
        break