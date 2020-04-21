
# a = input().split()
# n = int(a[0])
# m = int(a[1])
# x = []
# for i in range(n):
#     x.append(list(map(int,input().split())))

n=4
m=4
x = [[1 ,3 ,5 ,9],
[8 ,1 ,3 ,4],
[5 ,0 ,6 ,1],
[8 ,8 ,4 ,0]]

dp = [[0 for _ in range(m)] for _ in range(n)]

i = 0
j = 0
dp[0][0] = x[0][0]

for i in range(1,n):
    dp[i][0] = dp[i-1][0]+x[i][0]

for j in range(1,m):
    dp[0][j] = dp[0][j-1]+x[0][j]

for i in range(1,n):
    for j in range(1,m):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + x[i][j]

print(dp)

