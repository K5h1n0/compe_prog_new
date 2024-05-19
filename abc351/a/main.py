a = list(map(int,input().split()))
b = list(map(int,input().split()))
if sum(a)-sum(b) < 0:
    print(0)
else:
    print(abs(sum(a)-sum(b))+1)