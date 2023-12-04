import math

a,b,c,d = map(int,input().split())

def calc(s,n,m):
    nm = n*m // math.gcd(n,m)
    return s - s//n - s//m + s//nm

print(calc(b,c,d)-calc(a-1,c,d))