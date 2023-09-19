w = list(input())
w.sort()
if len(w) % 2:
    print("No")
    exit()
for i in range(0, len(w), 2):
    if w[i] != w[i+1]:
        print("No")
        exit()
print("Yes")
