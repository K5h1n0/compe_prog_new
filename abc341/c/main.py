h,w,n = map(int,input().split())
t = input()
s = []
for i in range(h):
    s.append(input())

ans = 0
for i in range(h):
    for j in range(w):
        
        if s[i][j] == "#":
            continue
        flg = True
        nowi = i
        nowj = j
        for k in range(n):
            if t[k] == "L":
                nowj -= 1
            elif t[k] == "R":
                nowj += 1
            elif t[k] == "U":
                nowi -= 1
            elif t[k] == "D":
                nowi += 1
            flg &= s[nowi][nowj] == "."
            if not (0 <= nowi < h and 0 <= nowj < w) or s[nowi][nowj] == "#":
                flg = False
                break
        if flg:
            ans += 1

print(ans)