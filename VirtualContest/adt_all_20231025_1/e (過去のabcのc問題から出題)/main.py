n = int(input())
ans = []
for i in range(120):
    if n%2:
        n -= 1
        ans.append("A")
    else:
        n //= 2
        ans.append("B")
    if n == 0:
        break
ans.reverse()
print("".join(ans))