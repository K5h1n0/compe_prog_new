n = int(input())
For = 0
Against = 0
for i in range(n):
    s = input()
    if s == "For":
        For += 1
    elif s == "Against":
        Against += 1
if For > Against:
    print("Yes")
else:
    print("No")