from collections import defaultdict

n = int(input())
s = input()
d = defaultdict(int)
now = ""
nowcnt = 0
for i in range(len(s)):
    if s[i] != now:
        now = s[i]
        nowcnt = 1
        d[s[i]] = max(d[s[i]],nowcnt)
    else:
        nowcnt += 1
        d[s[i]] = max(d[s[i]],nowcnt)
print(sum(d.values()))