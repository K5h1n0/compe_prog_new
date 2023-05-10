def is_primenumber(x:int):
    if x == 1 or x == 0: return False
    for i in range(2,int(x**0.5)+1):
        if x % i == 0: return False
    return True

print(is_primenumber(int(input())))

"""
# ベタ書き
n = int(input())
if n == 1:
    print("No")
ans = "Yes"
for i in range(2,int(n**0.5)+1):
    print(i)
    if n % i == 0:
        ans = "No"
        break
print(ans)
"""