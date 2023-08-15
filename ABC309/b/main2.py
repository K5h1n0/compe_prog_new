#解説AC

n = int(input())
l = []
l2 = []
for i in range(n):
    tmp = list(input())
    l.append(tmp[:])
    l2.append(tmp[:])
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            if i == 0 and j < n-1:
                l2[i][j+1] = l[i][j]
            if j == n-1 and i < n-1:
                l2[i+1][j] = l[i][j]
            if i == n-1 and 0 < j:
                l2[i][j-1] = l[i][j]
            if j == 0 and 0 < i:
                l2[i-1][j] = l[i][j]
for i in range(n):
    print("".join(l2[i]))