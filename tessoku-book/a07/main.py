d = int(input())
n = int(input())
list_att = [0]*(d+1)
for i in range(n):
    l,r = map(int,input().split())
    list_att[l-1] += 1
    list_att[r] -= 1
tmp = 0
ans = []
for i in range(len(list_att)):
    tmp += list_att[i]
    ans.append(tmp)
ans = ans[:-1]
print(*ans,sep="\n")