n, x, y = map(int, input().split())


def red(x):
    if x == 1:
        return 1
    else:
        return red(x-1) + blue(n) * x


def blue(x):
    if x == 1:
        
    return
