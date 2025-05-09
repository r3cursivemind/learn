import sys


def main():
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]

    dp = [[0] * M for _ in range(N)]
    dp[0][0] = grid[0][0]

    for j in range(1, M):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    for i in range(1, N):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    for i in range(1, N):
        for j in range(1, M):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])

    print(dp[N-1][M-1])


if __name__ == '__main__':
    main()