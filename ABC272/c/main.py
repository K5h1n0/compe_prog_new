n = int(input())
a = list(map(int,input().split()))
ans = -1
a.sort(reverse=True)
even = []
odd = []
for i in a:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
if 2 <= len(even):
    ans = max(ans,even[0] + even[1])
if 2 <= len(odd):
    ans = max(ans,odd[0] + odd[1])
print(ans)