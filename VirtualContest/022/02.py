x,y = map(int,input().split())
total = 0
if x == 1 and y == 1:
    total += 400000
if x == 1:
    total += 300000
elif x == 2:
    total += 200000
elif x == 3:
    total += 100000
if y == 1:
    total += 300000
elif y == 2:
    total += 200000
elif y == 3:
    total += 100000
print(total)