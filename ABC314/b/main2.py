n = int(input())
l = []
for i in range(n):
    c = int(input())
    l.append(set(list(map(int,input().split()))))
x = int(input())
bet = []
for i in range(n):
    if x in l[i]: #xに賭けた人だけ先に取り出す。
        bet.append((len(l[i]),i+1))
bet.sort() #賭けた数が少ない人を見つけるために昇順にソート。
ans = []
if len(bet) == 0: #賭けた人が誰もいなければ何もせず出力。
    pass
else:
    now = bet[0][0] #最初の人が賭けた人の中で最も数が少ない。
    ans.append(bet[0][1])
    for i in range(1,len(bet)):
        if now == bet[i][0]:
            ans.append(bet[i][1])
        else:
            break #数が等しくなくなったら終了。
print(len(ans))
print(*ans)