s = input()
minimum = 10**6
for i in range(len(s)-2):
    if abs(int(s[i:i+3])-753) < minimum:
        minimum = abs(int(s[i:i+3])-753)
print(minimum)