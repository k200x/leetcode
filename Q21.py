#coding:utf-8

w = [0, 2, 3, 4, 5]
v = [0, 3, 4, 5, 6]

bagV = 8

rows = 5
cols = 9

dp = [[0] * cols for i in range(rows)]
print(dp)

for i in range(0, rows):
    j = 1
    while j <= bagV:
        if j < w[i]:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w[i]] + v[i])
        j += 1

print(dp)





























