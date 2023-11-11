n = int(input())
accum = [0]*((10**6)+2)
for _ in range(n):
    l,r = map(int,input().split())
    accum[l] += 1
    accum[r+1] -= 1
for i in range(1,len(accum)):
    accum[i] += accum[i-1]
print(max(accum))