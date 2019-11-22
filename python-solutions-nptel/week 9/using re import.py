import re

def extractmax(s):
    numbers = re.findall('\d+',s)
    n = map(int,numbers)
    print(max(n))
    
s = input()
extractmax(s)