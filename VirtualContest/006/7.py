l = list(input())
n = int(input())
for i in range(n):
    a,b = map(int,input().split())
    mae = l[0:a-1]
    naka = l[a-1:b]
    naka.reverse()
    ushiro = l[b:]
    l = mae + naka + ushiro
print("".join(l))