n = int(input())
a = [0] + list(map(int,input().split()))
for i in range(1,len(a)):
    a[i] += a[i-1]
q = int(input())
ans = []
for i in range(q):
    left,right = map(int,input().split())
    total = right-left+1
    lucky = a[right] - a[left-1]
    if total/2 == lucky:
        ans.append("draw")
    elif total/2 < lucky:
        ans.append("win")
    else:
        ans.append("lose")
print(*ans,sep="\n")