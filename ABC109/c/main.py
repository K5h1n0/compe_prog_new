def gcd(a:int,b:int): #最大公約数 ユークリッドの互除法
    if b == 0: return a
    else: return gcd(b,a%b)

n,x = map(int,input().split())
x_l = list(map(int,input().split()))
ans = abs(x-x_l[0])
for i in range(1,len(x_l)):
    ans = gcd(ans,abs(x-x_l[i]))
print(ans)