# 背包问题 动态规划

def Solution(w, v_arr):
    def back(arr, ind, rst):
        if rst < 0:
            return -1
        if ind == len(arr):
            return 1
        ways = 0
        next = back(arr, ind + 1, rst)  # 不包含当前值2几种结果
        ways += next if next != -1 else 0
        next = back(arr, ind + 1, rst - arr[ind])  # 包含当前值2几种结果
        ways += next if next != -1 else 0
        return ways

    ways = back(v_arr, 0, w)
    print(ways)


def SolutionDP(w, v_arr):
    if not v_arr or w < 0:
        return 0
    dp = [[0 for _ in range(w + 1)] for _ in v_arr]
    for i in range(len(v_arr)):
        dp[i][0] = 1
    for j in range(1, w + 1):
        dp[0][j] = 2 if j >= v_arr[0] else 1  # 表示有几种方法

    for i in range(1, len(v_arr)):
        for j in range(1, w + 1):
            dp[i][j] = dp[i - 1][j]
            if j - v_arr[i] >= 0:
                dp[i][j] += dp[i - 1][j - v_arr[i]]
    print(dp)
    return dp[len(v_arr) - 1][w]


if __name__ == "__main__":
    w = 7
v_arr = [3, 2, 5]
SolutionDP(w, v_arr)
