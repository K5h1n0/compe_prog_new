def eratosthenes(saidai):
    list_prime_number = [True for _ in range(saidai+1)]
    list_prime_number[0], list_prime_number[1] = False, False
    for i in range(2, int(saidai**0.5)+1):
        if list_prime_number[i]:
            for j in range(2*i, saidai+1, i):
                list_prime_number[j] = False
    return list_prime_number


n = int(input())
l = eratosthenes(100010)
for i in range(n, 100010):
    if l[i]:
        print(i)
        exit()
