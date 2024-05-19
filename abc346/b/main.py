w,b = map(int,input().split())
s = "wbwbwwbwbwbw"*20
for i in range(len(s)-1):
    for j in range(i,len(s)):
        noww = 0
        nowb = 0
        for k in range(i,j):
            if s[k] == "w":
                noww += 1
            elif s[k] == "b":
                nowb += 1
        if noww == w and nowb == b:
            print("Yes")
            exit()
print("No")