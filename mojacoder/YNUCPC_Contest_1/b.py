h,w = map(int,input().split())
if h == 1 or w == 1:
    ansmax = (max(h,w) + 4 - 1)//4
    ansmin = (ansmax-1)*4
else:
    ansmax = h*w
    ansmin = (h*w-1)*3
print(ansmax,ansmin)