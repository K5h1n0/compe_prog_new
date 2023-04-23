a,b = map(int,input().split())
if a == b:
    print(0)
    exit()
cnt = 0
while a != b and a != 0 and b != 0:
    if a < b:
        cnt += b//a
        b = b%a
    elif a > b:
        cnt += a//b
        a = a%b
    # print(a,b)
print(cnt-1)