s = input()
sset = set()
length = len(s)+1
for i in range(length-1):
    for j in range(i+1,length):
        sset.add(s[i:j])
print(len(sset))