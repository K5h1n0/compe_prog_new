n = int(input())
s = input()
q = int(input())
alph = []
for i in range(26):
    alph.append(chr(ord("a")+i))
for i in range(q):
    c,d = input().split()
    for j in range(len(alph)):
        if alph[j] == c:
            alph[j] = d
ans = []
for i in range(len(s)):
    ans.append(alph[ord(s[i])-ord("a")])
print("".join(ans))