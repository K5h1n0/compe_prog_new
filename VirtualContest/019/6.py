a,b,c,x,y = map(int,input().split())
l = []
l.append(a*x+b*y)

a_cost = c*2*x
b_cost = 0
if x < y:
    b_cost = (y-x)*b
l.append(a_cost+b_cost)

b_cost = c*2*y
a_cost = 0
if y < x:
    a_cost = (x-y)*a
l.append(a_cost+b_cost)
print(min(l))