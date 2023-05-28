n = int(input())
s = input()
t = input()
ans = "Yes"
for i in range(n):
    if (s[i] == "l" or s[i] == "1") and (t[i] == "l" or t[i] == "1"):
        pass
    elif (s[i] == "0" or s[i] == "o") and (t[i] == "0" or t[i] == "o"):
        pass
    elif s[i] == t[i]:
        pass
    else:
        ans = "No"
        break
print(ans)

"""
n = int(input())
s = input()
t = input()
ans = "Yes"
l = ["l","1"]
o = ["0","o"]
for i in range(n):
    if s[i] == t[i]:
        continue
    elif s[i] in l and t[i] in l:
        continue
    elif s[i] in o and t[i] in o:
        continue
    else:
        ans = "No"
        break
print(ans)
"""