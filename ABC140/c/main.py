n = int(input())
b = list(map(int,input().split()))
ans = []
for i in range(0,len(b)-1):
    ans.append(min(b[i],b[i+1]))
print(sum(ans)+b[0]+b[-1])