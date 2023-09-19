s = input()
idxa = 10**7
idxz = 0
for i in range(len(s)):
    if s[i] == "A":
        idxa = min(i, idxa)
    elif s[i] == "Z":
        idxz = max(i, idxz)
print(idxz+1-idxa)
