# 紙に樹形図を書いた
h = int(input())
for i in range(1, 41):
    if 2**(i-1) <= h < 2**i:
        print((2**i)-1)
        exit()
