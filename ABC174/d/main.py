n = int(input())
c = list(input())
i = 0
cnt = 0
for back_idx in range(n-1,-1,-1):
    while i < n and c[i] != "W":
        i += 1
    if c[back_idx] == "W":
        continue
    if back_idx < i:
        break
    # "R"ならば
    c[i] = "R"
    c[back_idx] = "W"
    cnt += 1
    i += 1
print(cnt)