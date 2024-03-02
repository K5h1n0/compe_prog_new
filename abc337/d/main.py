h,w,k = map(int,input().split())
s = [list(input())for _ in range(h)]
ans = []
for i in range(h):
    for j in range(w):
        cnt = 0
        flg = True
        for m in range(k):
            if w <= j + m:
                flg = False
                break
            if s[i][j+m] == "x":
                flg = False
                break
            if s[i][j+m] == ".":
                cnt += 1
        else:
            if flg:
                ans.append(cnt)
        
        cnt = 0
        flg = True
        for m in range(k):
            if h <= i + m:
                flg = False
                break
            if s[i+m][j] == "x":
                flg = False
                break
            if s[i+m][j] == ".":
                cnt += 1
        else:
            if flg:
                ans.append(cnt)
if len(ans) == 0:
    print(-1)
else:
    print(min(ans))