n = int(input())
s = list(input())
l1 = set()
now = 300000300000
l1.add(now)
for i in range(n):
    if s[i] == "R":
        now += 1
    elif s[i] == "L":
        now -= 1
    elif s[i] == "U":
        now -= 1000000
    elif s[i] == "D":
        now += 1000000
    
    if now in l1:
        print("Yes")
        exit()
    else:
        l1.add(now)
print("No")