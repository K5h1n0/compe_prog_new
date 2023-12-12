k,g,m = map(int,input().split())
mug = 0
glass = 0
for i in range(k):
    if glass == g:
        glass = 0
    elif mug == 0:
        mug += m
    else:
        remain = g - glass
        glass += min(remain,mug)
        mug -= min(remain,mug)
print(glass,mug)