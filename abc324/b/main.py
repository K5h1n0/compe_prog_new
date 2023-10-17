n = int(input())
for i in range(50):
    for j in range(50):
        if (2**i)*(3**j) == n:
            print("Yes")
            exit()
print("No")