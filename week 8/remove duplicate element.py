def removeDuplicate(li):
    newli = []
    seen = set()
    
    for i in li:
        if i not in seen:
            seen.add(i)
            newli.append(i)
    
    return newli        
    

a = [int() for x in input().split()]
x = removeDuplicate(a)

for i in x:
    print(i,end=" ")