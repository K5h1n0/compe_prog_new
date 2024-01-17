n = int(input())
now = 0
for i in bin(n)[2:][::-1]:
    if i == "0":
        now += 1
    else:
        break
print(now)