n = int(input())
a = list(map(int,input().split()))
x = int(input())
total_a = sum(a)
remainder = x%total_a
cnt = x//total_a*len(a)
for i in range(len(a)):
    remainder -= a[i]
    cnt += 1
    if remainder < 0:
        break
print(cnt)