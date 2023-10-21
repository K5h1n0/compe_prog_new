n = int(input())
s = ["9"] + ["?"]*n
s[1] = "0"
s[n] = "1"
l = 1
r = n
while l <= r:
    mid = (l+r)//2
    q = "? " + str(mid)
    print(q,flush=True)
    inp = input()
    if inp == "0":
        s[mid] = inp
        l = mid + 1
    elif inp == "1":
        s[mid] = inp
        r = mid - 1
    if s[mid] == "0" and s[mid+1] == "1" or s[mid] == "1" and s[mid+1] == "0":
        ans = "! " + str(mid)
        print(ans,flush=True)
        exit()