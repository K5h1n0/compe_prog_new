n,time = map(int,input().split())
t = list(map(int,input().split()))
total = 0
for i in range(len(t)-1):
    total += min(time,t[i+1]-t[i])
print(total+time)