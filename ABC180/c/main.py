def calc_divisors(x:int): # 約数列挙
    list_divisors = []
    for i in range(1,int(x**0.5)+1):
        if x % i == 0:
            list_divisors.append(i)
            if x // i != i: list_divisors.append(x//i)
    list_divisors.sort()
    return list_divisors # 返却値は約数のリスト

print(*calc_divisors(int(input())),sep="\n")