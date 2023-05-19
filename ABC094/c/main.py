# WA

n = int(input())
x = list(map(int,input().split()))
x2 = sorted(x)
m1 = x2[len(x2)//2]
m2 = x2[(len(x2)//2)-1]
ans = []
print(x2)
print(m1)
print(m2)
for i in range(len(x)):
    if x[i] == m1:
        ans.append(m2)
    else:
        ans.append(m1)
# print(*ans,sep="\n")