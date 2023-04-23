#解説AC

import math

n = int(input())
ans = set()
for i in range(1,int(math.sqrt(n)+1)):
    #print(i,n//i,i*(n//i))
    ans.add(abs(i-n//i)+(n-(i*(n//i))))
print(min(ans))