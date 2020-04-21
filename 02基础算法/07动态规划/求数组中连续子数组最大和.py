'''
题目：求数组中 连续子数组最大和

例子：求一数组如 l = [0, 1, 2, 3, -4, 5, -6]，求该数组的最大连续子数组的和 如结果为[0,1,2,3,-4,5] 的和为7

思路：动态规划，dp[i]表示第i个数字时最大值,dp[i] = max{a[i], dp[i-1]+a[i]}

'''

def solution(nums):
    dp = []
    dp.append(nums[0])
    for i in nums[1:]:
        dp.append(max(i, dp[-1]+i)) 
    print(dp)
    return max(dp)


nums = [-1,4,-2,3,11]
solution(nums)