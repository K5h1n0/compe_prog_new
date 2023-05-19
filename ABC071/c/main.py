from collections import defaultdict

n = int(input())
a = list(map(int,input().split()))
d = defaultdict(int)
for i in a:
    d[i] += 1
d_sorted = sorted(d.items(),reverse=True)
ans = [0]
flg = 0
for i,v in d_sorted:
    if 4 <= v:
        ans.append(i**2)
    if flg == 0 and 2 <= v:
        tmp = i
        flg = 1
    elif flg == 1 and 2 <= v:
        ans.append(tmp*i)
        flg = 2
print(max(ans))