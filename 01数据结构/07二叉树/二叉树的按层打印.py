'''
题目描述
请实现一个函数按照之字形打印二叉树，
即第一行按照从左到右的顺序打印，
第二层按照从右至左的顺序打印，
第三行按照从左到右的顺序打印，其他行以此类推。

思路：
需要反转队列的结果，想到就是用到栈
需要用到两个栈，依次入栈，出栈，输出就行
如果打印是奇数层，先保存左节点再保存右节点到栈，如果是偶数，则先保存右再保存左

'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        list = []  #队列
        result = []  #每一层的结果
        results = []  #存储result的list
        nextLevel = 0
        toBeList = 1   #这层还需要加入result的元素个数
        if pRoot == None:
            return list
        list.append(pRoot)
        while list != []:
            treeNode = list.pop(0)
            toBeList -= 1
            result.append(treeNode.val)
            if treeNode.left:
                nextLevel += 1
                list.append(treeNode.left)
            if treeNode.right:
                nextLevel += 1
                list.append(treeNode.right)
            if toBeList == 0:
                results.append(result)
                result = []
                toBeList = nextLevel
                nextLevel = 0
        for i, result in enumerate(results):
            if i & 0x1 == 1:
                result.reverse()
        return results

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    results = Solution().Print(root)
    for i in results:
        print(i)