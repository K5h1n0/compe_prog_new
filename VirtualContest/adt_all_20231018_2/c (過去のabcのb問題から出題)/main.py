k = int(input())
a,b = input().split()
a = a[::-1]
b = b[::-1]
x = 0
y = 0
for i in range(len(a)):
    x += int(a[i])*k**i
for i in range(len(b)):
    y += int(b[i])*k**i
print(x*y)