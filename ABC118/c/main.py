def gcd(a:int,b:int): #最大公約数 ユークリッドの互除法
    if b == 0: return a
    else: return gcd(b,a%b)

n = int(input())
a = list(map(int,input().split()))
ans = a[0]
for i in range(1,len(a)):
    ans = gcd(ans,a[i])
print(ans)