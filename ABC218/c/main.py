n = int(input())
s1 = []
for i in range(n):    
    s1.append(list(input()))
t = []
for i in range(n):    
    t.append(list(input()))
s2 = []
for i in map(list,zip(*s1[::-1])):
    s2.append(i)
s3 = []
for i in map(list,zip(*s2[::-1])):
    s3.append(i)
s4 = []
for i in map(list,zip(*s3[::-1])):
    s4.append(i)
ans = "No"
print(*s1,sep="\n")
print(*s2,sep="\n")
print(*s3,sep="\n")
print(*s4,sep="\n")
for i in range(n):
    for j in range(n):
        flg = 0
        for k in range(n):
            for m in range(n):
                if t[k][m] != s1[(i+k)%n][(j+m)%n]:
                    flg = 1
                    break
            else:
                continue
            break
        if flg == 0:
            ans = "Yes"
            print(ans)
            exit()
        
        flg = 0
        for k in range(n):
            for m in range(n):
                if t[k][m] != s2[(i+k)%n][(j+m)%n]:
                    flg = 1
                    break
            else:
                continue
            break
        if flg == 0:
            ans = "Yes"
            print(ans)
            exit()
        
        flg = 0
        for k in range(n):
            for m in range(n):
                if t[k][m] != s3[(i+k)%n][(j+m)%n]:
                    flg = 1
                    break
            else:
                continue
            break
        if flg == 0:
            ans = "Yes"
            print(ans)
            exit()
        
        flg = 0
        for k in range(n):
            for m in range(n):
                if t[k][m] != s4[(i+k)%n][(j+m)%n]:
                    flg = 1
                    break
            else:
                continue
            break
        if flg == 0:
            ans = "Yes"
            print(ans)
            exit()
print(ans)