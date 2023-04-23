n,k = map(int,input().split())
a = list(map(int,input().split()))
a = list(set(a))
a.sort()
ans = 0
for i in range(min(len(a),k)):
    if i == a[i]:
        ans = i
if ans == 0 and 0 not in a:
    print(0)
else:
    print(ans+1)