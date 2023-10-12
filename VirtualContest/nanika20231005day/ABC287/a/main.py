n = int(input())
l = []
for i in range(n):
    l.append(input())
if l.count("For") > l.count("Against"):
    print("Yes")
else:
    print("No")