n = int(input())
s = list(map(int, input().split()))
t = list(map(int, input().split()))
l = [10**10]*n
for i in range(2*n):
    ind = i % n
    l[ind] = min(t[ind], l[ind-1]+s[ind-1])
print(*l, sep="\n")
