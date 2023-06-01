def gcd(a:int,b:int): #最大公約数 ユークリッドの互除法
    if b == 0: return a
    else: return gcd(b,a%b)

a,b = map(int,input().split())
maximum = 0
flg = 0
for i in range(b,a-1,-1):
    for j in range(i-1,a-1,-1):
        print(i,j,i-j)