a,b,c,d = map(int,input().split())

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y,x%y)

def lcm(x,y):
    return x*y//gcd(x,y)

print((b-(b//c + b//d - b//lcm(c,d)))-(a-(a//c + a//d - a//lcm(c,d))))
