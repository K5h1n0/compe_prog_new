s = input()
for i in range(len(s)):
    if ord("A") <= ord(s[i]) <= ord("Z"):
        print(i+1)
        exit()