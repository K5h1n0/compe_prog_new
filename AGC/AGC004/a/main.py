l = sorted(list(map(int,input().split())))
if l[0]%2 == 0 or l[1]%2 == 0 or l[2]%2 == 0:
    print(0)
    exit()
print(l[0]*l[1])