n = int(input())
a = list(map(int,input().split()))
l = [0]*(10**5+2)
for i in range(len(a)):
    l[a[i]] += 1
    l[a[i]-1] += 1
    l[a[i]+1] += 1
print(max(l))

# aの値が0の時がコーナーケース