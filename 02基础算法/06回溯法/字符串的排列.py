'''
题目：输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
'''

'''
依次取一个元素，然后依次和之前递归形成的所有子串组合，形成新的字符串。
33ms
5632k
'''

# -*- coding:utf-8 -*-
class Solution: 
    def Permutation(self, ss):
        if not ss:
            return []
        res = []
        ss = list(ss)
        def tracback(index, ss):

            if index == len(ss):
                res.append(ss)  # 这里append有坑，需要深拷贝-》 ss.copy()
                
            for i in range(index, len(ss)):
                ss[index], ss[i] = ss[i], ss[index]
                print(ss,i,index)
                tracback(index+1, ss)
                ss[index], ss[i] = ss[i], ss[index]

        tracback(0, ss)
        return res


s = Solution()
print( s.Permutation('abc') )