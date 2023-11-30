d,p = map(int,input().split())
tax = d*p
d*= 100
d += tax
print(d//100)