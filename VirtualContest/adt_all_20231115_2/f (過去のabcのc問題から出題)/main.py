from collections import defaultdict

n = int(input())
l = list(map(int,input().split()))
d = defaultdict(set)
cnt = 0
for i in range(1,n+1):
    if i == l[i-1]:
        cnt += 1
    else:
        d[l[i-1]].add(i)
cnt = cnt*(cnt-1)//2
cnt2 = 0
for i in range(1,n+1):
    if l[i-1] in d[i]:
        cnt2 += 1
print(cnt + cnt2//2)