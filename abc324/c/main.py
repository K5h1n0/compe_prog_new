def check(s,t):
    #Sが現在の文字列、tが比較用の元々の文字列
    if len(s) > len(t):
        return check(t,s) #すごい
    if len(s) < len(t)-1:
        return False
    i,j,miss = 0,0,0
    while i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else: # 文字が一致しなければ
            miss += 1
            if miss > 1: #miss一回まで許す
                return False
            if len(s) == len(t):
                i += 1
            j += 1
    return True

n,t = input().split()
n = int(n)
ans = []
for i in range(n):
    s = input()
    if check(s,t):
        ans.append(i+1)
print(len(ans))
print(" ".join(map(str,ans))) #この書き方