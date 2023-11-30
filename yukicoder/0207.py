a,b = map(int,input().split())
ans = []
for i in range(a,b+1):
    if "3" in str(i) or i%3 == 0:
        ans.append(i)
print(*ans,sep="\n")