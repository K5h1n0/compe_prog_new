n = int(input())
l = ["9"] + ["0"]*n
l[n] = "1"
q = "?" + " " + str(n-1)
print(q,flush=True)
inp = input()
l[n-1] = inp
if l[n] != l[n-1]:
    q = "!" + " " + str(n-1)
    print(q,flush=True)
    exit()
for i in range(2,min(n,21)):
    q = "?" + " " + str(i)
    print(q,flush=True)
    l[i] = input()
    if l[i] != l[i-1]:
        q = "!" + " " + str(i-1)
        print(q,flush=True)
        exit()