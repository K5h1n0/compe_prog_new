n = int(input())
l = []
for i in range(n):
    l.append(input())
ans = "No"
for i in range(n-1):
    for j in range(i+1,n):
        nows1 = l[i]+l[j]
        revs1 = nows1[::-1]
        nows2 = l[j]+l[i]
        revs2 = nows2[::-1]
        if nows1 == revs1 or nows2 == revs2:
            ans = "Yes"
            break
print(ans)