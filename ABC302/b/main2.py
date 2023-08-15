# 解説AC

h,w = map(int,input().split())
s = []
for i in range(h):
    s.append(list(input()))
snuke = "snuke"
di = [-1,-1,-1,0,1,1,1,0]
dj = [-1,0,1,1,1,0,-1,-1]
for i in range(h):
    for j in range(w):
        
        for k in range(8):
            for m in range(5):
                nowi = i+di[k]*m
                nowj = j+dj[k]*m
                if nowi < 0 or nowj < 0 or h <= nowi or w <= nowj:
                    break
                if s[nowi][nowj] != snuke[m]:
                    break
                if m == 4:
                    for o in range(5):
                        nowi = (i+di[k]*o)+1
                        nowj = (j+dj[k]*o)+1
                        print(nowi,nowj)
                    exit()