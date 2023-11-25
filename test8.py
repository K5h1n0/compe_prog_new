l = [10,50,20,100,10]
accum = [0]
for i in l:
    accum.append(accum[-1]+i)
print(*accum)