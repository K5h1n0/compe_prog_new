n = int(input())
s = input()
t = 0
a = 0
flg = ""
for i in range(n):
    if s[i] == "T":
        t += 1
    else:
        a += 1
if a < t:
    print("T")
elif a > t:
    print("A")
else:
    m = a
    t = 0
    a = 0
    for i in range(n):
        if s[i] == "T":
            t += 1
        else:
            a += 1
        if m == a:
            print("A")
            exit()
        elif m == t:
            print("T")
            exit()