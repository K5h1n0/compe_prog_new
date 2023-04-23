#解説AC　仕組みを理解していない

a,b,w = map(int,input().split())
minimum = 99999999
maximum = 0
for i in range(1000000+1):
    if a*i <= 1000*w and 1000*w <= b*i:
        minimum = min(minimum,i)
        maximum = max(maximum,i)
if maximum == 0:
    print("UNSATISFIABLE")
else:
    print(minimum,maximum)