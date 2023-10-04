s = input()
correct = "CODEFESTIVAL2016"
ans = 0
for i in range(len(correct)):
    if correct[i] != s[i]:
        ans += 1
print(ans)