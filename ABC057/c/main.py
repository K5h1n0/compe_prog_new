n = int(input())
ans = len(str(n))
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        len1 = len(str(i))
        len2 = len(str(n//i))
    ans = min(ans,max(len1,len2))
print(ans)