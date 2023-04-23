#解説読んでもそんなに分かんなかった……。
n = int(input())
a = list(map(int,input().split()))
l = []
for i in range(0,n-1):
    for j in range(1,n):
        if i == j:
            continue
        l.append(a[i] * a[j])
print(l)