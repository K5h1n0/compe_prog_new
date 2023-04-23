n = int(input())
list1 = [0]*100
for i in range(n):
    l,r = map(int,input().split())
    list1[l] += 1
    list1[r] -= 1
tmp = 0
ans = []
for i in range(len(list1)):
    ans =
    tmp += list1[i]
    list1[i] = tmp
print(list1)