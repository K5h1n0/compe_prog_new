n = int(input())
l1 = set(range(1,2*n+1+1))
while True:
    for i in l1:
        if i in l1:
            print(i,flush=True)
            l1.remove(i)
            break
    inp = int(input())
    if inp == 0:
        exit()
    l1.remove(inp)