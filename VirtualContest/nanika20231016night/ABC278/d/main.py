n = int(input())
a = list(map(int,input().split()))
q = int(input())
ans = []
nowlist = a[:]
nowval = 0
for i in range(q):
    inp = list(input().split())
    
    if inp[0] == "1":
        nowval = int(inp[1])
        nowlist = [0]*n
    elif inp[0] == "2":
        nowlist[int(inp[1])-1] += int(inp[2])
    elif inp[0] == "3":
        ans.append(nowval+nowlist[int(inp[1])-1])
print(*ans,sep="\n")