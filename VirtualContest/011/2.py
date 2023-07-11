h,w = map(int,input().split())
r,c = map(int,input().split())
r -= 1
c -= 1
cnt = 0
for nowi,nowj in (r-1,c),(r,c+1),(r+1,c),(r,c-1):
    if 0 <= nowi < h and 0 <= nowj < w:
        cnt += 1
print(cnt)