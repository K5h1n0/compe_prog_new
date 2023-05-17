n = int(input())
h = list(map(int,input().split()))
now = h[0]
for i in range(1,len(h)):
    if now < h[i]:
        now = h[i]
    else:
        break
print(now)