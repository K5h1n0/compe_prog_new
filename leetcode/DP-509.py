class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        fibonacci = [0]*n
        for i in range(n):
            if i == 0 or i == 1:
                fibonacci[i] = 1
                continue
            fibonacci[i] = fibonacci[i-1] + fibonacci[i-2]
        return fibonacci[n-1]

if __name__ == "__main__":
    solve = Solution()
    print(solve.fib(int(input())))
