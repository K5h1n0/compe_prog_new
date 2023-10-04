n = int(input())
a = list(map(int, input().split()))
q = int(input())
ans = []
for i in range(q):
    inp = list(map(int, input().split()))
    if inp[0] == 1:
        a[inp[1]-1] = inp[2]
    elif inp[0] == 2:
        ans.append(a[inp[1]-1])
print(*ans, sep="\n")
