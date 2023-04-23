s = list(input())
t = int(input())

s.sort(reverse=True)
x = 0
y = 0
for i in range(len(s)):
    if s[i] == "U":
        y -= 1
    elif s[i] == "R":
        x += 1
    elif s[i] == "L":
        x -= 1
    elif s[i] == "D":
        y += 1
    elif s[i] == "?":
        x = abs(x)
        y = abs(y)
        if t == 1:
            x += 1
        elif t == 2:
            if x <= y:
                y -= 1
            else:
                x -= 1
print(abs(x)+abs(y))