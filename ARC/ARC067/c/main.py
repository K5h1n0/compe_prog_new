from collections import defaultdict

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

d = defaultdict(int)
n = int(input())
for i in range(n,1,-1): #真ん中を1にすることで、2までループしてくれる。
    for j in calc_prime_factorization(i):
        d[j[0]] += j[1]
ans = 1
for i in d.values():
    ans *= (i+1) # 約数の個数=(指数部分+1)の積
    ans %= (10**9+7)
print(ans)