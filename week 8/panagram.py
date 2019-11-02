alphabet = []

for i in range(97,123):
    alphabet.append(chr(i))

a = input()
a = a.lower()
a = set(a)
a = list(a)

for i in a:
    if i in alphabet:
        alphabet.remove(i)
        
if(len(alphabet) == 0):
    print("YES",end="")
else:
    print("NO",end="")