n = int(input())
total = float(0)
for i in range(n):
    v,s = input().split()
    if s == "JPY":
        total += float(v)
    elif s == "BTC":
        total += float(v)*380000
print(total)