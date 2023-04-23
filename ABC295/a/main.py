n = int(input())
l = list(input().split())
ans = "No"
l2 = ["and","not","that","the","you"]
for i in range(n):
    if l[i] in l2:
        ans = "Yes"
print(ans)