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


# エラトステネスの篩は素数判定に用いる。
n = int(input())
l = eratosthenes(100000009)
print(l[n])

li_int_prime = []
# O(n)でリストを作ることも可能
li_int_prime = [i for i in range(n+1) if l[i]]
print(li_int_prime)

"""
# https://qiita.com/drken/items/a14e9af0ca2d857dad23
# ベタ書き
saidai = 100009
list_prime_number = [True for _ in range(saidai+1)]
list_prime_number[0], list_prime_number[1] = False, False  # 0と1は素数ではない。
for i in range(2, int(saidai**0.5)+1):  # √saidaiまでの試し割りで十分。
    if list_prime_number[i]:
        for j in range(2*i, saidai+1, i):  # iずつ増やしていって、該当したらFalseにする。
            list_prime_number[j] = False
"""

