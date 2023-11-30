import bisect

n,q = map(int,input().split())
a = sorted(list(map(int,input().split())))
ans = []
for _ in range(q):
    x = int(input())
    ans.append(n-bisect.bisect_left(a,x))
print(*ans,sep="\n")