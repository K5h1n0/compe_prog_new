from collections import deque,defaultdict

path = "/mnt/c/Users/n1220390.STCN2/Downloads/ipfctf_input.txt"
flg = False
l = []
with open(path) as f:
    for input_line in f:
        if not flg:
            n,m = map(int,input_line.split())
            flg = True
            continue
        l.append(tuple(map(int,input_line.split())))
d = defaultdict(list)
for a,b in l:
    d[a].append(b)
    d[b].append(a)
searched = [True] + [False]*1300

maxpeople = 0
groupnumber = 0
for i in range(1,1300+1):
    if searched[i]:
        continue
    searched[i] = True
    q = deque()
    q.append(i)
    nowgroupset = set()
    nowgroupset.add(i)
    nownumberpeople = 0
    while q:
        nownumberpeople += 1
        now = q.popleft()
        nowgroupset.add(now)
        for next in d[now]:
            if searched[next]:
                continue
            searched[next] = True    
            q.append(next)
    #print(nowgroupset)
    maxpeople = max(maxpeople,nownumberpeople)
    groupnumber += 1
print("ipfctf{"+str(groupnumber)+":"+str(maxpeople)+"}")