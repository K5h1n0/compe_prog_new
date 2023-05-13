n = int(input())
h = list(map(int,input().split()))
ans = "Yes"
now1 = h[-1]
now2 = h[-1] + 1
for i in range(n-2,-1,-1):
    # print(f"now1={now1} now2={now2} h[i]={h[i]}")
    if h[i] <= now1:
        # print("now1が合致")
        now1 = h[i]
        now2 = h[i] + 1
    elif h[i] == now2:
        # print("now2が合致")
        h[i] -= 1
        now1 = h[i]
        now2 = h[i] + 1
    else:
        ans = "No"
        break
print(ans)