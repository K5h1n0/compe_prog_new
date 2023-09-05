from functools import lru_cache

p = int(input())
coin = []


@lru_cache(maxsize=1000)
def recursion(n):
    if n == 0:
        return 1
    return n * recursion(n-1)


for i in range(1, 11):
    coin.append(recursion(i))
coin.sort(reverse=True)
cnt = 0
while 0 < p:
    for v in coin:
        if 0 <= p - v:
            p -= v
            cnt += 1
            break
print(cnt)
