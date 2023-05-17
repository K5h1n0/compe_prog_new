n = int(input())
ans_alphabet = [100]*26
l = []
for i in range(n):
    l.append(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
for i in range(len(l)):
    for j in range(26):
        ans_alphabet[j] = min(ans_alphabet[j],l[i].count(alphabet[j]))
ans = ""
for i in range(26):
    for j in range(ans_alphabet[i]):
        ans += alphabet[i]
print(ans)