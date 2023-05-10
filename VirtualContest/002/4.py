n = int(input())
for i in range(1,10):
    kai = int(str(i)+str(i)+str(i))
    if n <= kai:
        print(kai)
        exit()