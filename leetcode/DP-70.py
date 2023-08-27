class Solution:
    def climbStairs(self, n: int) -> int:
        steps = [0]*(n+1)
        steps[0] = 1
        for i in range(1,n+1):
            if i == 1:
                steps[i] += 1
                continue
            steps[i] = steps[i-1] + steps[i-2]
        return steps[-1]


if __name__ == "__main__":
    instance = Solution()
    print(instance.climbStairs(int(input())))
