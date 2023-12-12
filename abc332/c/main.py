n,m = map(int,input().split())
s = list(input())
l = []
flg = 0
normalnum = 0
normalmax = 0
eventnum = 0
eventmax = 0
flg = 0
for i in range(n):
    if s[i] == "0":
        if flg == 1:
            l.append([eventnum,normalnum,eventnum+normalnum])
        eventmax = max(eventmax,eventnum)
        normalmax = max(normalmax,normalnum)
        eventnum = 0
        normalnum = 0
        flg = 0
    elif s[i] == "1" or s[i] == "2":
        flg = 1
        if s[i] == "1":
            normalnum += 1
        if s[i] == "2":
            eventnum += 1
l.append([eventnum,normalnum,eventnum+normalnum])
ans = []
for i in l:
    num = i[0]
    if m < i[1]:
        num += i[1] - m
    ans.append(num)
print(max(ans))