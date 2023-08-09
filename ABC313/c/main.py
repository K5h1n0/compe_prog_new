n = int(input())
a = list(map(int,input().split()))
a.sort()
total = sum(a)
#print(a)
#print(total)
v = total//n
new = [v]*n
#print(v)
for i in range(total - v*n):
    new[n-i-1] += 1
#print(new)
total = 0
for i in range(n):
    total += abs(a[i]-new[i])
print(total//2)