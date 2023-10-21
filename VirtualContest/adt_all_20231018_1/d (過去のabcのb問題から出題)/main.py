n = int(input())
l = []
for i in range(n):
    l.append(input())
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        now = l[i] + l[j]
        if now == now[::-1]:
            print("Yes")
            exit()
print("No")