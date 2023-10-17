s = "." + input()
t = input()
for i in range(len(s)-1,-1,-1):
    if s[i] != t[i]:
        print(i+1)
        exit()