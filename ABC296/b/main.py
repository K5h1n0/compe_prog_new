for i in range(8):
    tmp = input()
    for j in range(8):
        if tmp[j] == "*":
            ans = chr(ord("a")+j) + str(8-i)
print(ans)