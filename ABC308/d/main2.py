# 解説見ながらBFS
# https://qiita.com/hyouchun/items/2e207f41b7a0ace5509b

from collections import deque

def is_next(e1,e2):
    snuke = "snuke" #下でインデックスの値が必要なため、setに出来ない
    if e1 not in snuke or e2 not in snuke: #そもそもsnuke以外の文字ならダメ
        return False
    idx1 = snuke.index(e1)
    idx2 = snuke.index(e2) 
    if idx2 == (idx1+1) % 5: #snukeの文字が隣合ってるかどうか判定
        return True
    return False #隣合ってない

h,w = map(int,input().split())
l = [input() for _ in range(h)]

checked = [[0]*w for _ in range(h)]

q = deque()
q.append((0,0))
checked[0][0] = 1

while q:
    nowi,nowj = q.popleft()
    nowstr = l[nowi][nowj]
    for nexti,nextj in (nowi-1,nowj),(nowi,nowj+1),(nowi+1,nowj),(nowi,nowj-1):
        if not (0 <= nexti < h and 0 <= nextj < w): #この書き方良いな
            continue
        if checked[nexti][nextj] == 1: #1ならもう訪問済み。単にif checked[nexti][nextj]:という書き方でも良い（bool型が入っているので。）。
            continue
        nextstr = l[nexti][nextj]
        if is_next(nowstr,nextstr):
            checked[nexti][nextj] = 1
            q.append((nexti,nextj))

if checked[-1][-1]: #天才か？
    print("Yes")
else:
    print("No")