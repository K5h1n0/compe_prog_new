n = int(input())
l = list(map(int,input().split()))
l.sort(reverse=True)
oddl = []
evenl = []
for i in l:
    if i%2 == 0:
        evenl.append(i)
    else:
        oddl.append(i)
ans = -1
if 2 <= len(oddl):
    ans = max(ans,oddl[0]+oddl[1])
if 2 <= len(evenl):
    ans = max(ans,evenl[0]+evenl[1])
print(ans)