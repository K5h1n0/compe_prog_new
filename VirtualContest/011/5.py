n = int(input())
cnt = 0
for i in range(1,1000000):
    if len(set(str(i))) == 1:
        cnt += 1
    if cnt == n:
        print(i)
        exit()