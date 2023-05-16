def eratosthenes(saidai): # エラトステネスの篩
    # 計算量はO(nloglogn)
    # 先にエラトステネスの篩で素数表を作っておけば、O(1)で素数判定が可能。
    list_prime_number = [True for _ in range(saidai+1)]
    list_prime_number[0], list_prime_number[1] = False, False
    for i in range(2, int(saidai**0.5)+1):
        if list_prime_number[i]:
            for j in range(2*i, saidai+1, i): # iずつ増やしていって、該当したらFalseにする。
                list_prime_number[j] = False
    return list_prime_number  # saidaiまでの素数かどうかがbool型で入っているリストを返却する。

x = int(input())
l = eratosthenes(1000009)

li_int_prime = []
li_int_prime = [i for i in range(len(l)) if l[i]]
for i in li_int_prime:
    if x <= i:
        print(i)
        exit()