n,x = map(int,input().split())
z = [0]*x
for _ in range(n):
    a,b = map(int,input().split())
    now = a-1
    for i in range(b):
        sei_zahyo = now + i
        hu_zahyo = now - i
        if 0 <= sei_zahyo < x:
            z[sei_zahyo] = max(z[sei_zahyo],b-i)
        if 0 <= hu_zahyo < x:
            z[hu_zahyo] = max(z[hu_zahyo],b-i)
print(*z)