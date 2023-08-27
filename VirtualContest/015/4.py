a, b = map(int, input().split())
for i in range(1, 2000):
    taxa = int(i*0.08)
    taxb = int(i*0.1)
    if a == taxa and b == taxb:
        print(i)
        exit()
print(-1)
