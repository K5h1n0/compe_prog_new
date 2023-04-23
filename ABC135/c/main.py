def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    ans = 0
    for i in range(len(b)):
        lft = min(a[i],b[i])
        ans += lft
        a[i] -= lft
        b[i] -= lft
        
        rht = min(a[i+1],b[i])
        ans += rht
        a[i+1] -= rht
        b[i] -= rht
    print(ans)

if __name__ == "__main__":
    main()