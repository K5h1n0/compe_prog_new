n = int(input())
s = input()
sset = set(s)
if len(sset) == 1:
    print(-1)
    exit()
now = 0
maximum = 0
for i in range(n):
    if s[i] == "-":
        now = 0
    elif s[i] == "o":
        now += 1
        maximum = max(maximum,now)
print(maximum)