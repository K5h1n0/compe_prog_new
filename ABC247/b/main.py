# 難しかった。でも、解答見れば単純だったから、ちゃんと一つずつ丁寧に考えないと駄目。

n = int(input())
l = []
ans = [0] * n
for i in range(n):
    l.append(list(input().split()))
for i in range(len(l)):
    last = 0
    first = 0
    for j in range(len(l)):
        if i != j:
            if l[i][0] == l[j][0] or l[i][0] == l[j][1]:
                first = 1
            if l[i][1] == l[j][0] or l[i][1] == l[j][1]:
                last = 1
    if first == 1 and last == 1:
        print("No")
        exit()
print("Yes")