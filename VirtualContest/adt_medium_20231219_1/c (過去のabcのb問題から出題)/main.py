import re

s = input()
if len(s) != 8:
    print("No")
    exit()
pattern = re.compile(r'^[A-Z][1-9][0-9]*[A-Z]$')
if pattern.match(s):
    print("Yes")
else:
    print("No")