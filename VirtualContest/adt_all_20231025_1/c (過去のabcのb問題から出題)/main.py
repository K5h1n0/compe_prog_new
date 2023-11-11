h,w = map(int,input().split())
l = []
for i in range(h):
    s = list(input())
    if "o" in s:
        for j in range(w):
            if s[j] == "o":
                l.append([i,j])
print(abs(l[0][1]-l[1][1])+abs(l[0][0]-l[1][0]))