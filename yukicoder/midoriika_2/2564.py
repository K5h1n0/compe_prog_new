t = int(input())
l = []
v = {"R":"L","L":"R","U":"D","D":"U"}
for _ in range(t):
    tmp = []
    for i in range(2):
        x,y,d = input().split()
        tmp.append((int(x),int(y),d))
    l.append(tmp)
ans = []
for i in l:
    now1x = i[0][0]
    now1y = i[0][1]
    now2x = i[1][0]
    now2y = i[1][1]
    now1d = i[0][2]
    now2d = i[1][2]
    if v[i[0][2]] == i[1][2]: # ぶつかる方向
        if now1x == now2x:
            if now2y < now1y:
                now1y,now2y = now2y,now1y
                now1d,now2d = now2d,now1d
            if now1y <= now2y and now1d == "U":
                ans.append("Yes")
            else:
                ans.append("No")
            continue
        elif now1y == now2y:
            if now2x < now1x:
                now1x,now2x = now2x,now1x
                now1d,now2d = now2d,now1d
            if now1x <= now2x and now1d == "R":
                ans.append("Yes")
            else:
                ans.append("No")
            continue
        else:
            ans.append("No")
    else: # ぶつかる方向でないなら
        dist1 = abs(now1x-now2x)
        dist2 = abs(now1y-now2y)
        if v[i[0][2]] != i[1][2] and dist1 == dist2:
            if now1d == "R" and now1x <= now2x:
                ans.append("Yes")
            elif now1d == "L" and now2x <= now1x:
                ans.append("Yes")
            elif now1d == "U" and now1y <= now2y:
                ans.append("Yes")
            elif now1d == "D" and now2y <= now1y:
                ans.append("Yes")
            else:
                ans.append("No")
        else:
            ans.append("No")
print(*ans,sep="\n")