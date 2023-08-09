n = int(input())
l = list(map(int,input().split()))
if max(l) == l[0] and max(l) not in l[1:]:
    print(0)
else:
    print(max(l)-l[0]+1)