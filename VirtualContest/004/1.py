k = int(input())
h = 21
m = 0
if k//60 == 0:
    m += k
else:
    h+=1
    m += k%60
print(str(h)+":"+str(m).zfill(2))