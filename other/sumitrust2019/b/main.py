n = int(input())
for i in range(50000):
    if int(i * 108 / 100) == n:
        print(i)
        exit()
print(":(")