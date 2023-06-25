n = int(input())
accepted = set()
ans = []
for i in range(n):
    s = input()
    if s not in accepted:
        accepted.add(s)
        ans.append(i+1)
print(*ans,sep="\n")