from collections import defaultdict

s = sorted(list(input()))
t = sorted(list(input()))

s_dict = defaultdict(int)
t_dict = defaultdict(int)

for i in range(len(s)):
    s_dict[s[i]] += 1
    t_dict[t[i]] += 1

