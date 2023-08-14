n,k = map(int,input().split())
a = list(map(int,input().split()))
seta = set(a)
l = []
for i in range(n):
    x,y = map(int,input().split())
    l.append([x,y])
ans = []
for i in range(n):
    if i+1 in seta:
        continue
    minimum = 10**10
    for j in a:
        minimum = min(minimum,((l[i][0]-l[j-1][0])**2 + (l[i][1]-l[j-1][1])**2)**0.5)
    ans.append(minimum)
print(max(ans))

# 明かりを持っていない人から、誰でも良いので明かりを持っている人の最短距離を求める。
# 次に、明かりを持っていない人から持っている人の最短距離の中で、最も長い距離を探す。
# 持っていない人から持っている人の最短距離を求めたので、少なくともその距離は無いと、どの明かりにも照らされるという条件を満たさなくなってしまう。