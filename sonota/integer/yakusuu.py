def calc_divisors(x:int): # 約数列挙
    list_divisors = []
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            list_divisors.append(i)
            if x // i != i: list_divisors.append(x//i)
    list_divisors.sort()
    return list_divisors # 返却値は約数のリスト




n = int(input())
print(calc_divisors(n))
print(len(calc_divisors(n))) #約数の個数を求めたいときはlen()を取ればOK

# 約数の個数を求める他の方法として、素因数分解をした後、指数部分+1の積を求める方法もある。


"""
#ベタ書き
n = int(input())
l = []
for i in range(1,int(n**0.5)+1):
    if n % i == 0:
        l.append(i)
        if n//i != i:
            l.append(n//i)
l.sort()
print(l)
"""