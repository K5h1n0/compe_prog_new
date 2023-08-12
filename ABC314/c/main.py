from collections import defaultdict

n,m = map(int,input().split())
s = input()
c = list(map(int,input().split()))
d = defaultdict(list)
for i in range(n):
    d[c[i]].append(i)
s_list = [""]*n
for i in d:
    for j in range(len(d[i])):
        # print(d[i][(j+1)%len(d[i])])
        s_list[d[i][(j+1)%len(d[i])]] = s[d[i][j]]
print("".join(s_list))