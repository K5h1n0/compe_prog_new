def gcd(a:int,b:int): #最大公約数 ユークリッドの互除法
    if b == 0: return a
    else: return gcd(b,a%b)

l = sorted(list(map(int,input().split())))
minimum = gcd(gcd(l[0],l[1]),l[2])
print(l[0]//minimum + l[1]//minimum + l[2]//minimum -3)