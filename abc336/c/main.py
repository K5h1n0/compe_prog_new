n = int(input())
def f(x):
    res = ''
    while x:
        res += str(x%5)
        x //= 5
    if len(res) == 0:
        return 0
    return int(res[::-1])
print(f(n-1)*2)