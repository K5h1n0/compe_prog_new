n,k,q = map(int,input().split())
l = [k-q]*n
for i in range(q):
    tmp = int(input())
    l[tmp-1] += 1
for i in range(len(l)):
    if 1 <= l[i]:
        print("Yes")
    else:
        print("No")