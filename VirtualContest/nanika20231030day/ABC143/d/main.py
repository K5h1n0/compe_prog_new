n = int(input())
l = sorted(list(map(int,input().split())))
length = 2000
count_list = [0]*length
for i in l:
    count_list[i] += 1
print(count_list)
accum = count_list[:]
for i in range(1,length):
    
"""
# https://drken1215.hatenablog.com/entry/2019/10/20/032700
n = int(input())
l = sorted(list(map(int,input().split())))
ans = 0
for i in range(n):
    now = i
    for j in range(i+1,n):
        while now < n and l[now] < l[i]+l[j]: #尺取り法
            now += 1
        ans += now-1 -j
print(ans)
"""