n = int(input())
a = list(map(int,input().split()))
ans = []
for i in range(n-1):
    ans.append(a[i])
    if abs(a[i] - a[i+1]) == 1:
        pass
    else:
        if a[i] < a[i+1]:
            tmp_list = list(range(a[i]+1,a[i+1]))
        else:
            tmp_list = list(range(a[i+1]+1,a[i]))
            tmp_list.reverse()
        ans += tmp_list
ans.append(a[n-1])
print(*ans)