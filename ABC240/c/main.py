# DPでした
n,x = map(int,input().split())
lb = []
l_sa = []
suma = 0
sumb = 0
for i in range(n):
    a,b = map(int,input().split())
    suma += a
    sumb += b
    lb.append(b)
    l_sa.append(b-a)
if x < suma or sumb < x:
    print("No")
    exit()

