def eratosthenes(saidai):
    # エラトステネスの篩はO(nloglogn)
    # 先にエラトステネスの篩で素数表を作っておけば、O(1)で素数判定が可能。
    list_prime_number = [True for _ in range(saidai+1)]
    list_prime_number[0], list_prime_number[1] = False, False
    for i in range(2, int(saidai**0.5)+1):
        if list_prime_number[i]:
            for j in range(2*i, saidai+1, i): # iずつ増やしていって、該当したらFalseにする。
                list_prime_number[j] = False
    return list_prime_number  # saidaiまでの素数かどうかがbool型で入っているリストを返却する。

n = int(input())
m = int((n//12)**0.5)+1
l = eratosthenes(m)
li_int_prime = [i for i in range(m+1) if l[i]]
set_int_prime = set(li_int_prime)
ans = 0
length = len(li_int_prime)
for i in range(length-2):
    for j in range(i+1,length-1):
        for k in range(j+1,length):
            a = li_int_prime[i]
            b = li_int_prime[j]
            c = li_int_prime[k]
            v = a*a*b
            if n < v: break
            v *= c
            if n < v: break
            v *= c
            if n < v: break
            ans += 1
print(ans)