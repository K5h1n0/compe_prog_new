a,b = map(int,input().split())
if b-a == 1 and b%3 != 1:
    print("Yes")
else:
    print("No")