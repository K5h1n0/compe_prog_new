import itertools

n = int(input())
p = list(map(int,input().split()))
q = list(map(int,input().split()))
ans = []
i = 0
for v in itertools.permutations(range(1,n+1)):
    if list(v) == p:
        ans.append(i)
    if list(v) == q:
        ans.append(i)
    i += 1
print(abs(ans[0]-ans[1]))