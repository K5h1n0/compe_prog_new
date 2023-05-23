def is_primenumber(x:int): # 素数判定
    if x == 1 or x == 0: return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: return False
    return True # 返却値は素数かどうかのbool型

x = int(input())
for i in range(x,200000):
    if is_primenumber(i):
        print(i)
        exit()