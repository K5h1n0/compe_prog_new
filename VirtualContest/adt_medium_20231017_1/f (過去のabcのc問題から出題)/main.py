n = int(input())
s = input()
visited = set()
x = 0
y = 0
visited.add((x,y))
for i in range(n):
    if s[i] == "R":
        x += 1
    if s[i] == "D":
        y += 1
    if s[i] == "L":
        x -= 1
    if s[i] == "U":
        y -= 1
    if (x,y) in visited:
        print("Yes")
        exit()
    visited.add((x,y))
print("No")