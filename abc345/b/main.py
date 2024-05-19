n = input()
if n[-1] == "0":
    if n[0] == "0":
        print(0)
    else:
        print(n[0:-1])
else:
    if n[0:-1] == "" or (n[0] == "-" and len(n) == 2):
        res = 0
    else:
        res = int(n[0:-1])
    if n[0] != "-":
        res += 1
    print(res)