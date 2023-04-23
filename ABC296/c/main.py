import copy

n,x = map(int,input().split())
a = list(map(int,input().split()))
b = copy.copy(a)
a = set(a)
ans = "No"
for i in range(len(b)):
    if b[i] + x in a:
        ans = "Yes"
        print(ans)
        exit()
print(ans)