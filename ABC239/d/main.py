a,b,c,d = map(int,input().split())
prime = set()
for i in range(1,201):
    flg = 0
    for j in range(1,i+1):
        if i % j == 0:
            if i == j and flg == 1:
                prime.add(i)
                break
            flg += 1
for i in range(a,b+1):
    for j in range(c,d+1):
        print(i+j)
        if i+j in prime:
            print("Aoki")
            exit()
print("Takahashi")