n,m,k = map(int,input().split())
def lcm(a:int,b:int): # 最小公倍数
    return a*b//gcd(a,b) # 最小公倍数を求めるのに最大公約数が必要になる。

def gcd(a:int,b:int): #最大公約数 ユークリッドの互除法
    if b == 0: return a
    else: return gcd(b,a%b)

num_lcm = lcm(n,m)
tmp1 = num_lcm//n
tmp2 = num_lcm//m
tmp3 = tmp1 + tmp2 - 2
#print(num_lcm)
#print(tmp3)
#print(k//tmp3)
remain = k%tmp3
#print(remain)
base = num_lcm * (k//tmp3)
#print(base)
if tmp3 == 1:
    print(1+num_lcm*(k-1))
else:
    l = []
    for x in range(n,num_lcm,n):
        l.append(x)
        if remain < len(l):
            break
    for x in range(m,num_lcm,m):
        l.append(x)
        if remain * 2 < len(l):
            break
    l.sort()
    print(base+l[remain-1])