a, b, c = map(int, input().split())
l = sorted([a, b, c])
if a <= c <= b:
    print("Yes")
else:
    print("No")
