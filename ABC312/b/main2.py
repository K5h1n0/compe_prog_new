# 解説AC

n,m = map(int,input().split())
s = []
for _ in range(n):
    s.append(input())
code = ["###.?????",
        "###.?????",
        "###.?????",
        "....?????",
        "?????????",
        "?????....",
        "?????.###",
        "?????.###",
        "?????.###"]

for i in range(n-8):
    for j in range(m-8):
        flag = True
        for di in range(9):
            for dj in range(9):
                #スゴイ書き方
                flag &= s[i+di][j+dj] == code[di][dj] or code[di][dj] == "?"
        if flag:
            print(i+1,j+1)