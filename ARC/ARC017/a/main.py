def is_primenumber(x:int): # 素数判定
    if x == 1 or x == 0: return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: return False
    return True # 返却値は素数かどうかのbool型

if is_primenumber(int(input())):
    print("YES")
else:
    print("NO")