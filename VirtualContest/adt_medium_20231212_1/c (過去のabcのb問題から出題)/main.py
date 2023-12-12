s = list(input())
if len(set(s)) == 1:
    print("Weak")
    exit()
cnt = 0
for i in range(1,4):
    if (int(s[i-1])+1)%10 == int(s[i]):
        cnt += 1
if cnt == 3:
    print("Weak")
else:
    print("Strong")