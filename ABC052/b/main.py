n = int(input())
s = input()
maximum = 0
now = 0
for i in range(n):
    if s[i] == "I":
        now += 1
    else:
        now -= 1
    maximum = max(maximum, now)
print(maximum)
