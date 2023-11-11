n = input()
for i in range(int(n),919+1):
    if int(str(i)[0]) * int(str(i)[1]) == int(str(i)[2]):
        print(i)
        exit()