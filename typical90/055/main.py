n,p,q = map(int,input().split())
a = list(map(int,input().split()))
cnt = 0
for i in range(n-4):
    for j in range(i+1,n-3):
        for k in range(j+1,n-2):
            for m in range(k+1,n-1):
                for o in range(m+1,n):
                    b = a[i]%p
                    c = a[j]%p
                    d = a[k]%p
                    e = a[m]%p
                    f = a[o]%p
                    if (b*c*d*e*f)%p == q:
                        cnt += 1
print(cnt)