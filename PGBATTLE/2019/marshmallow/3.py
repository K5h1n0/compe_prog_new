n,m = map(int,input().split())
l = []
pin = [0]*m
for j in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
ans = 0
for i in range(n):
    # iはレーン番号
    hit_time = l[i][0] + l[i][1]
    hit_pin = i - hit_time
    if 0 <= hit_pin < len(pin):
        pin[hit_pin] = 1
print(sum(pin))