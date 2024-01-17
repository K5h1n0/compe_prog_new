o = input()
w = input()
s = []
for i in range(len(w)):
    s.append(o[i])
    s.append(w[i])
if len(w) < len(o):
    s.append(o[-1])
print("".join(s))