def calc_prime_factorization(x:int): # 素因数分解
    if x == 1: return [[]] # 1の素因数分解は出来ない。何を返却すべきか。
    list_prime_factorization = []
    for i in range(2,int(x**0.5)+1):
        if x % i != 0: continue
        elif x % i == 0:
            cnt_divisors = 0
            while x % i == 0:
                cnt_divisors += 1
                x //= i
            list_prime_factorization.append([i,cnt_divisors])
        if x == 1:
            break
    if x != 1:
        list_prime_factorization.append([x,1]) # xが1ならば全部割り切れた。xが1でないなら素数が残っていることになるので、appendする。
    return list_prime_factorization #返却値は[[素因数,個数][素因数,個数]......]の二次元リスト


print(calc_prime_factorization(int(input())))


"""
# https://qiita.com/drken/items/a14e9af0ca2d857dad23#3-%E7%B4%84%E6%95%B0%E5%88%97%E6%8C%99
#ベタ書き
n = int(input())
l = []
if n == 1:
    l.append([1,1])
    print(l)
    exit()
for i in range(2,int(n**0.5)+1):
    if n % i != 0:continue
    elif n % i == 0:
        cnt = 0
        while n % i == 0:
            cnt += 1
            n //= i
    l.append([i,cnt])
if n != 1:
    l.append([n,1])
print(l)
"""
