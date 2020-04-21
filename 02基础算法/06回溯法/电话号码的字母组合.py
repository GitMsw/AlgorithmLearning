'''
题目：电话号码的字母组合
描述：
给定一个仅包含数字 2-9 的字符串，
返回所有它能表示的字母组合。给出数字到字母的映射如下
（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

思路：
回溯法
        2
      / | \
     a  b  c
    /|\
   d e f 
  ad ae af
'''
class Solution:
    def letterCombinations(self, digits: str) -> list:
        maps = {
        '2':'abc',
        '3':'def',
        '4':'ghi',
        '5':'jkl',
        '6':'mno',
        '7':'pqrs',
        '8':'tuv',
        '9':'wxyz'
       }
        if not digits:
            return []
        c = len(digits)
        res = []
        def func(index, item):
            if len(item) == c:  # 终止条件
                res.append(item)
                return
            for i in range(index, c):  # 依次取出2，3
                for j in maps[digits[i]]:  # 依次取出a-d,a-e,a-f
                    func(i+1, item+j)
        func(0, '')
        return res


s = Solution()
print(s.letterCombinations('22'))