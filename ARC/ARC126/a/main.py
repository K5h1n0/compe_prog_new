t = int(input())
ans = []
for i in range(t):
    n2, n3, n4 = map(int, input().split())
    nowans = 0
    b1 = min(n3//2, n4)
    nowans += b1
    n3 -= b1*2
    n4 -= b1
    b2 = min(n3//2, n2//2)
    nowans += b2
    n3 -= b2*2
    n2 -= b2*2
    b3 = min(n4//2, n2)
    nowans += b3
    n4 -= b3*2
    n2 -= b3
    b4 = min(n4, n2//3)
    nowans += b4
    n4 -= b4
    n2 -= b4*3
    b5 = n2//5
    nowans += b5
    n2 -= b5*5
    ans.append(nowans)
print(*ans, sep="\n")

# 2,3,4で10を作るには、以下の5パターンがある。
# 3 3 4
# 3 3 2 2
# 4 4 2
# 4 2 2 2
# 2 2 2 2 2
