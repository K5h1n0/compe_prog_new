N = int(input())
str_list = [input() for _ in range(N)]
flag = 0
counter = 0
ex = 0
for i in range(N-1):
    for i in range(N-1):
        a = 0 + ex
        b = 1 + counter
        word = str_list[a] + str_list[b]
        drow = str_list[b] + str_list[a]
        if counter != N - 1:
            counter += 1
        if a == b:
            continue
        if str(word) == str(word)[::-1] :
            flag += 1
        if str(drow) == str(drow)[::-1] :
            flag += 1
    if ex != N - 1:
        ex += 1
        counter = 0
    else:
        counter = 0

if flag >= 1:
    print('Yes')
else:
    print('No')