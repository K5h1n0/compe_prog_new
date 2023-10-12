n,m = map(int,input().split())
foods = [True]*m
for i in range(n):
    l = list(map(int,input().split()))
    now = set(l[1:])
    for i in range(1,m+1):
        if not i in now:
            foods[i-1] = False
print(sum(foods))