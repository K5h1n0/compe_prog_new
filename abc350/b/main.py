n,q = map(int,input().split())
t = list(map(int,input().split()))
l = [1]*n
for i in range(q):
    if l[t[i]-1] == 1:
        l[t[i]-1] = 0
    else:
        l[t[i]-1] = 1
print(sum(l))