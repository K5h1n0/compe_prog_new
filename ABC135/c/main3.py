def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    before = sum(a)
    for i in range(len(b)):
        tmp = min(a[i],b[i])
        a[i] -= tmp
        b[i] -= tmp
        a[i+1] = max(0,a[i+1]-b[i])
    after = sum(a)
    print(before - after)

if __name__ == "__main__":
    main()