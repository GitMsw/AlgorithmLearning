'''
题目： 0-1背包问题。在使用动态规划算法求解0-1背包问题时，
      使用二维数组m[i][j]存储背包剩余容量为j，
      可选物品为i、i+1、……、n时0-1背包问题的最优值

例子：
价值数组v = {8, 10, 6, 3, 7, 2}，
重量数组w = {4, 6, 2, 2, 5, 1}，
最大容量c = 12

思路：动态规划
if(j>=w[i])
    m[i][j]=max(m[i-1][j],m[i-1][j-w[i]]+v[i]);
else
    m[i][j]=m[i-1][j];

'''

def solution(v, w, c):
    dp = [ [0 for _ in range(c+1)] for _ in range(len(v)) ]
    for i in range(len(v)):
        for j in range(c+1):
            if j < w[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]]+v[i])
    for i in dp:
        print(i)
    return dp[-1][-1]


if __name__ == '__main__':
    w = [5, 2, 3]
    v = [5, 3, 3]
    c = 5

    solution(v,w,c)