from functools import lru_cache
import math

@lru_cache(maxsize=1000)
def hantei(x):
    kioku = []
    flg = 0
    for i in range(1,int(math.sqrt(x))+1):
        if x/i == i:
            flg = 1
        elif x % i == 0:
            kioku.append(i)
    if flg == 0:
        return len(kioku)*2
    elif flg == 1:
        return len(kioku)*2 + 1


n = int(input())
cnt = 0
for a in range(1,n//2+1):
    b = n - a
    if a < b:
        cnt += hantei(a)*hantei(b)*2
    elif a == b:
        cnt += hantei(a)*hantei(b)
print(cnt)