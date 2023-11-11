n = int(input())
s = []
for i in range(n):
    s.append(list(input()))
t = []
for i in range(n):
    t.append(list(input()))

def cut(h,w,inp_list):
    min_h = h
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

h,w,test = cut(n,n,s)

def kaiten(l):
    new_list = []
    for j in range(len(l[0])):
        now = []
        for i in range(len(l)-1,-1,-1):
            now.append(l[i][j])
        new_list.append(now)
    new_h = len(new_list)
    new_w = len(new_list[0])
    return new_h,new_w,new_list

h,w,test = kaiten(test)

h,w,s = cut(n,n,s)
for k in range(4):
    for i in range(n-h+1):
        for j in range(n-w+1):
            flg = True
            for m in range(h):
                for o in range(w):
                    flg &= t[i+m][j+o] == s[m][o]
            if flg:
                print("Yes")
                
    h,w,s = kaiten(s)
    print(h,w)
    print(*s,sep="\n")
print("No")