n = int(input())
l = sorted(list(map(int,input().split())))
l1 = set((l[:(n//2)+1]))
l2 = set((l[(n//2)+1:]))
if max(l1) < min(l2):
    print("Yes")
else:
    print("No")