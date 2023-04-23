h1,h2,h3,w1,w2,w3 = map(int,input().split())
"""
   w1 w2 w3
h1 i  l  o 
h2 j  m  p
h3 k  n  q
"""
ans = 0
for i in range(1,31):
    for j in range(1,31):
        for l in range(1,31):
            for m in range(1,31):
                k = w1 - i - j
                n = w2 - l - m
                o = h1 - i - l
                p = h2 - j - m
                q1 = h3 - k - n
                q2 = w3 - o - p
                if k <= 0 or n <= 0 or o <= 0 or p <= 0 or q1 <= 0 or q2 <= 0 or q1 != q2:
                    pass
                else:
                    ans += 1
print(ans)