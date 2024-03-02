s = list(input())
s.reverse()
now = 0
for i in range(len(s)):
    if now == 0:
        if s[-1] == "A":
            now = 1
        elif s[-1] == "B":
            now = 2
        elif s[-1] == "C":
            now = 3
        else:
            break
    elif now == 1:
        if s[-1] == "A":
            pass
        elif s[-1] == "B":
            now = 2
        elif s[-1] == "C":
            now = 3
        else:
            break
    elif now == 2:
        if s[-1] == "B":
            pass
        elif s[-1] == "C":
            now = 3
        else:
            break
    elif now == 3:
        if s[-1] == "C":
            pass
        else:
            break
    s.pop()
if len(s) == 0:
    print("Yes")
else:
    print("No")
