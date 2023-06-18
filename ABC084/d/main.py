def eratosthenes(saidai): # エラトステネスの篩
    # 計算量はO(nloglogn)
    # 先にエラトステネスの篩で素数表を作っておけば、O(1)で素数判定が可能。
    list_prime_number = [1 for _ in range(saidai+1)]
    list_prime_number[0], list_prime_number[1] = 0, 0
    for i in range(2, int(saidai**0.5)+1):
        if list_prime_number[i]:
            for j in range(2*i, saidai+1, i): # iずつ増やしていって、該当したらFalseにする。
                list_prime_number[j] = 0
    return list_prime_number  # saidaiまでの素数かどうかがbool型で入っているリストを返却する。

q = int(input())
l = []
sosuu = eratosthenes(100000)
like2017 = [0]*len(sosuu)
for i in range(len(like2017)):
    if i%2 == 1 and sosuu[i] and sosuu[(i+1)//2]:
        like2017[i] = 1
for i in range(1,len(like2017)):
    like2017[i] += like2017[i-1]
ans = []
for i in range(q):
    left,right = map(int,input().split())
    ans.append(like2017[right]-like2017[left-1])
print(*ans,sep="\n")