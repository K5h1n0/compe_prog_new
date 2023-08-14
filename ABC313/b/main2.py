n,m = map(int,input().split())
lose_list = [1]*n
for _ in range(m):
    a,b = map(int,input().split())
    lose_list[b-1] = 0
if sum(lose_list) == 1:
    print(lose_list.index(1)+1)
else:
    print(-1)