n = int(input())
l1 = []
l2 = []
c1now = 0
c2now = 0
l1.append(c1now)
l2.append(c2now)
for i in range(n):
    c,p = map(int,input().split())
    if c == 1:
        c1now += p
    elif c ==2:
        c2now += p
    l1.append(c1now)
    l2.append(c2now)
q = int(input())
list_ans = []
for i in range(q):
    l,r = map(int,input().split())
    l -= 1
    ans1 = l1[r] - l1[l]
    ans2 = l2[r] - l2[l]
    list_ans.append([ans1,ans2])
for i in range(len(list_ans)):
    print(*list_ans[i])