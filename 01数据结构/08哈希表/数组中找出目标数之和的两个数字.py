'''
题目：数组中找出目标数之和的两个数字

给定数组，和一个目标值，找出数组中和为目标值的两个数

例子：
nums = [2, 7, 11, 15]
target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
返回[0, 1]

思路：利用哈希原理
d{}是哈希字典，保存了数组的数值和序号的字典，[2, 2, 3, 7] -> d={2: 1, 3: 2, 7: 3}
如果 target - num 在d里则说明，当前值和保存的值和等于目标值
返回之前的最后一个和当前的值的序号即可
'''

def solution(nums, target):
    d = {}
    for i, num in enumerate(nums):
        d[num] = i
        if target - num in d:
            print(d)
            return [d[target - num], i]
        


nums = [2, 2, 3, 7]
target = 10
print( solution(nums, target) )
