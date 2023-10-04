n = input()
tmp = int(n[0])
for i in range(1,len(n)):
    if tmp > int(n[i]):
        tmp = int(n[i])
    else:
        print("No")
        exit()
print("Yes")