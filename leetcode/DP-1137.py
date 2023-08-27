class Solution:
    def tribonacci(self, n: int) -> int:
        l = [0]*(n+1)
        for i in range(n+1):
            if i == 0:
                continue
            elif i == 1 or i == 2:
                l[i] = 1
                continue
            l[i] = l[i-1] + l[i-2] + l[i-3]
        return l[n]

if __name__ == "__main__":
    solve = Solution()
    print(solve.tribonacci(int(input())))
