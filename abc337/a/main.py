n = int(input())
ta = 0
ao = 0
for i in range(n):
    x,y = map(int,input().split())
    ta += x
    ao += y
if ta == ao:
    print("Draw")
elif ta > ao:
    print("Takahashi")
else:
    print("Aoki")