n = int(input())
ans = []
for i in range(120):
    if n == 0:
        break
    if n % 2 == 0:
        n //= 2
        ans.append("B")
    else:
        n -= 1
        ans.append("A")
ans.reverse()
print(*ans,sep="")