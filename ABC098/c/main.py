n = int(input())
s = input()
e_l = [0]*n
w_l = [0]*n
tmp = 0
for i in range(n):
    if s[i] == "W":
        tmp += 1
    w_l[i] = tmp
tmp = 0
for i in range(n-1,-1,-1):
    if s[i] == "E":
        tmp += 1
    e_l[i] = tmp
minimum = 10**10
for i in range(n):
    minimum = min(minimum,e_l[i]+w_l[i]-1)
print(minimum)