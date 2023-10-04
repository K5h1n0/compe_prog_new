n = int(input())
l = []
for i in range(n):
    l.append(int(input()))

tmp = sorted(set(l[:]))  # setにsorted()をかけると、listになる

d = {}
for i, v in enumerate(tmp):  # 座標圧縮でソート後にenumerateを使うと楽
    d[v] = i  # 普通の辞書型で、新しくキーとバリューを追加する時
for i in range(n):
    print(d[l[i]])
