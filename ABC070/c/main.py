# 最小公倍数の導入に良い問題だと思う。

def lcm(a:int,b:int): # 最小公倍数
    return a*b//gcd(a,b) # 最小公倍数を求めるのに最大公約数が必要になる。

def gcd(a:int,b:int): #最大公約数 ユークリッドの互除法
    if b == 0: return a
    else: return gcd(b,a%b)

n = int(input())
l = [int(input()) for __ in range(n)]
ans = 1
for i in range(n):
    ans = lcm(ans,l[i])
print(ans)