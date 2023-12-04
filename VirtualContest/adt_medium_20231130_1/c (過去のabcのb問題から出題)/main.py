h,w = map(int,input().split())
alph = ".ABCDEFGHIJKLMNOPQRSTUVWXYZ"
l = []
for i in range(h):
    inp = list(map(int,input().split()))
    now = []
    for j in range(len(inp)):
        now.append(alph[inp[j]])
    l.append("".join(now))
print(*l,sep="\n")