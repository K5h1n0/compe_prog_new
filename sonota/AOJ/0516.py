n,k = map(int,input().split())
ans = []
while n != 0 and k != 0:
    l = [0]
    for i in range(n):
        l.append(int(input()))
    for i in range(1,len(l)):
        l[i] += l[i-1]
    maximum = 0
    for i in range(n-k+1):
        maximum = max(maximum,l[i+k]-l[i])
    ans.append(maximum)
    n,k = map(int,input().split())
print(*ans,sep="\n")