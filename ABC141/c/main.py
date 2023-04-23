n,k,q = map(int,input().split())
score = [k]*n
for i in range(q):
    a = int(input())
    score[a-1] += 1
for i in range(len(score)):
    score[i] -= q
for i in range(len(score)):
    if score[i] > 0:
        print("Yes")
    else:
        print("No")