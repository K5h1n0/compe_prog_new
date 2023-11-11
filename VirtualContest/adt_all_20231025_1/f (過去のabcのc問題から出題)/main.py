n = int(input())
s = list(input())
w = list(map(int,input().split()))
child = []
adult = []
for i in range(len(s)):
    if s[i] == "1":
        adult.append(w[i])
    else:
        child.append(w[i])
print(child)
print(adult)