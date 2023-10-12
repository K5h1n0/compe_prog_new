# 結構躓く
n = int(input())
s = [0] + list(map(int,input().split())) # 
ans = []
for i in range(1,len(s)):
    ans.append(s[i]-s[i-1])
print(*ans)