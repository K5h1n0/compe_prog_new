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

x = int(input())
ans = 1
for i in range(2,x+1):
    tmp = calc_prime_factorization(i)
    if len(tmp) == 1 and tmp[0][1] != 1:
        ans = i
print(ans)