from collections import deque

s = input()
if len(s) <= 2:
    print(s)
    exit()
q = deque()
mae2 = s[0]
mae1 = s[1]
q.append(mae2)
q.append(mae1)
for i in range(2,len(s)):
    now = s[i]
    if now == "C" and mae2 == "A" and mae1 == "B":
        q.pop()
        q.pop()
        if len(q) > 0:
            mae1 = q.pop()
        else:
            mae1 = ""
        if len(q)>0:
            mae2 = q.pop()
        else:
            mae2 = ""
        q.append(mae2)
        q.append(mae1)
    else:
        mae2 = mae1
        mae1 = now
        q.append(now)
print("".join(q))