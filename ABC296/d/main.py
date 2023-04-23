import math

n,m = map(int,input().split())
def f(x):
    answer = []
    for i in range(1,int(math.sqrt(x)+1)):
        if x % i == 0:
            answer.append(i)
            answer.append(x//i)
    return sorted(answer)

for i in range(m,m+11):
    print(f(i))