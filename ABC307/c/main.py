
# 余白を切り取る処理
def cut(h,w,inp_list):
    min_h = h # "#"の存在する行・列の最小・最大値を求める。初期化。
    max_h = -1
    min_w = w
    max_w = -1    
    for i in range(h):
        for j in range(w):
            if inp_list[i][j] == '#':
                min_h = min(min_h, i)
                max_h = max(max_h, i)
                min_w = min(min_w, j)
                max_w = max(max_w, j)
    
    new_list = []
    for i in range(min_h, max_h + 1):
        tmp = inp_list[i][min_w:max_w + 1]
        new_list.append(tmp)
    new_h = max_h - min_h + 1
    new_w = max_w - min_w + 1
    return new_h,new_w,new_list

ha,wa = map(int,input().split())
la = []
for i in range(ha):
    la.append(list(input()))
ha,wa,la = cut(ha,wa,la)

hb,wb = map(int,input().split())
lb = []
for i in range(hb):
    lb.append(list(input()))
hb,wb,lb = cut(hb,wb,lb)

hx,wx = map(int,input().split())
lx = []
for i in range(hx):
    lx.append(list(input()))
hx,wx,lx = cut(hx,wx,lx)
"""
print(ha,wa)
print(*la,sep="\n")
print(hb,wb)
print(*lb,sep="\n")
print(hx,wx)
print(*lx,sep="\n")
"""
largeh = 20
largew = 20
black_grids = set()
sheetx = [["."]*largeh for _ in range(largew)] #透明なsheetx
for i in range(hx): #lxをsheetxの左上に転写する。
    for j in range(wx):
        sheetx[i][j] = lx[i][j]
        if lx[i][j] == "#":
            black_grids.add((i,j))
#print(*sheetx,sep="\n")

for i in range(largeh-ha+1):
    for j in range(largew-wa+1):

        a_set = set()
        for k in range(ha):
            for m in range(wa):
                # print(i,j,k,m)
                if la[k][m] == "#":
                    if sheetx[i+k][j+m] == "#": #シートaが"#"ならば、シートxも"#"であって欲しい。
                        a_set.add((i+k,j+m))
                    else:
                        break # シートaが"#"なのに、シートxが"#"じゃない時は抜ける。
            else: continue
            break
        else:
            #ここにシートbの処理

            # ここに来ることができれば、シートaは合致したことになるので、次にシートbを調べていく。
            # print("ここからシートb")
            for n in range(largeh-hb+1):
                for o in range(largew-wb+1):

                    b_set = set()
                    for p in range(hb):
                        for q in range(wb):
                            # print(n,o,p,q)
                            if lb[p][q] == "#":
                                if sheetx[n+p][o+q] == "#":
                                    b_set.add((n+p,o+q))
                                else:
                                    break
                        else: continue
                        break
                    else:
                        #ここに来れたらシートbの黒い部分がシートxの黒い部分と全て重なる。
                        # ここでやっと合致してるか判定。
                        if black_grids == a_set | b_set:
                            print("Yes")
                            exit()    
                        continue

            #もし残念ながらシートbが合致しなかったら、引き続きシートaからやり直しのcontinue
            continue
print("No")
