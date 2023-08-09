# setとinを使う方法。確かに、whileを使う所が尺取法に似ているかも知れない。
# https://blog.hamayanhamayan.com/entry/2020/10/10/232835
n = int(input())
p = list(map(int,input().split()))
already = set()
ans = []
now = 0
for i in range(len(p)):
    already.add(p[i])
    if now in already:
        while now in already:
            now += 1
    ans.append(now)
print(*ans,sep="\n")
