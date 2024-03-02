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

n = int(input())
a = list(map(int,input().split()))
a.sort()
# print(a)
l = []
d = defaultdict(list)
for i in range(len(a)):
    res = calc_prime_factorization(a[i])
    l.append(res)
    for j in res:
        d[j[0]].append((a[i],i))
# print(d)
searched = [[False]*n for _ in range(n)]
ans = 0
for i in range(len(a)):
    flg = 0
    if a[i] == 0:
        ans += n-i-1
        continue
    for j in l[i]:
        for k in d[j[0]]:
            if i == k[1]:
                continue
            if (((a[i]*k[0])**0.5)%1 == 0) and i < k[1]:
                ans += 1
print(ans)