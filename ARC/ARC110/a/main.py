def lcm(a:int,b:int): # 最小公倍数
    return a*b//gcd(a,b) # 最小公倍数を求めるのに最大公約数が必要になる。

def gcd(a:int,b:int): #最大公約数 ユークリッドの互除法
    if b == 0: return a
    else: return gcd(b,a%b)

n = int(input())
ans = 1
for i in range(1,n+1):
    ans = lcm(ans,i)
print(ans+1)