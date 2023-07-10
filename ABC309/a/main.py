a,b = map(int,input().split())
if b-a == 1 and (b%3 == 0 or b%3 == 2):
    print("Yes")
else:
    print("No")