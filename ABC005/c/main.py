t = int(input())
n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))
bb = [0] * len(b)
ans = "yes"
if n < m:
    ans = "no"
else:
    ai = 0
    for i in range(len(b)):
        while ai != len(a):
            if a[ai] <= b[i] <= a[ai]+t:
                bb[i] = 1
                ai += 1
                break
            ai += 1
    if sum(bb) != len(b):
        ans = "no"
print(ans)