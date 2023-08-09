s = list(input())
t = list(input())
s_flg = []
s_str = []
s_flg_idx = -1
now = ""
for i in range(len(s)):
    if now != s[i]:
        s_flg.append(0)
        s_str.append(s[i])
        now = s[i]
        s_flg_idx += 1
    elif now == s[i]:
        s_flg[s_flg_idx] = 1
print(s_flg)
print(s_str)
t_str_idx = 0
now = ""
ans = "Yes"

print(ans)