#なぜか分からないけどゲキムズだった

n = int(input())
s = input()
acc = "b"
if n == 1:
    if s == acc:
        print(0)
        exit()
    else:
        print(-1)
        exit()
for i in range(1,101):
    if i % 3 == 0:
        acc = "b" + acc + "b"
    elif i % 3 == 1:
        acc = "a" + acc + "c"
    elif i % 3 == 2:
        acc = "c" + acc + "a"
    if s == acc:
        print(i)
        exit()
print(-1)