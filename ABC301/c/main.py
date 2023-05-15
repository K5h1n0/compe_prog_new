from collections import defaultdict

s = list(input())
t = list(input())

if "@" not in set(s) and "@" not in set(t):
    if s == t: print("Yes")
    else:print("No")
    exit()

dict_s = defaultdict(int)
dict_t = defaultdict(int)

s_atcount = s.count("@")
t_atcount = t.count("@")
for i in range(len(s)):
    dict_s[s[i]] += 1
    dict_t[t[i]] += 1
