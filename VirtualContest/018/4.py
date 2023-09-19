n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
v1, v2, v3 = 0, 0, 0
for i in range(n):
    if p[i] <= a:
        v1 += 1
    elif a < p[i] <= b:
        v2 += 1
    elif b < p[i]:
        v3 += 1
print(min(v1, min(v2, v3)))
