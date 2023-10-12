# WA
a, b, c, k = map(int, input().split())
if k % 2:
    if 10**18 < k*(abs(b-a)):
        print("Unfair")
        exit()
    print(b-a)
else:
    if 10**18 < k*(abs(a-b)):
        print("Unfair")
        exit()
    print(a-b)
