a = input()

b = []

x = str(a)

for i in x:
    b.append(int(i))
    

count_0 = 0
count_1 = 0

for i in b:
    if(i == 0):
        count_0+=1
    elif(i == 1):
        count_1+=1
        
if((count_1 ==1) or (count_0 == 1)):
    print("Yes")
else:
    print("No")