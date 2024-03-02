s = input()
abc = list("abcdefghijklmnopqrstuvwxyz")
l = [0]*26
for i in range(len(s)):
    for j in range(len(abc)):
        if s[i] == abc[j]:
            l[j] += 1
maximum = max(l)
for i in range(len(l)):
    if l[i] == maximum:
        print(abc[i])
        exit()