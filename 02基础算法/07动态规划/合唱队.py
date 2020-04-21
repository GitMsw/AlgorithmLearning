'''
题目描述
计算最少出列多少位同学，使得剩下的同学排成合唱队形

说明：

N位同学站成一排，音乐老师要请其中的(N-K)位同学出列，使得剩下的K位同学不交换位置就能排成合唱队形。
合唱队形是指这样的一种队形：设K位同学从左到右依次编号为1, 2, …, K，他们的身高分别为T1, T2, …, TK，
则他们的身高满足T1<T2<......<Ti-1<Ti>Ti+1>......>TK（1<=i<=K）
你的任务是，已知所有N位同学的身高，计算最少需要几位同学出列，可以使得剩下的同学排成合唱队形。

输入例子:
8
186 186 150 200 160 130 197 200
输出例子:
4

思路：
两遍最长递增子序列，第一遍从左往右，第二遍从右往左，然后把两遍动态
规划的结果相加，区最大的那个，比如 8 186 186 150 200 160 130 197 200
第一遍dp的结果是1 1 1 2 2 1 3 4，第二遍dp的结果是3 3 2 3 2 1 1 1，
那么相加最大是5，所以需要出列的同学的个数是8-5+1 = 4.

'''

def solution(arr: list) -> int:
    c =len(arr)
    res1 = [1 for i in range(c)]
    res2 = [1 for i in range(c)]
    res = [0 for i in range(c)]

    for i in range(c):  # 从做左到右dp
        for j in range(i):
            if arr[i] <= arr[j]:
                continue
            elif res1[i] < res1[j] + 1:
                res1[i] += 1
    for i in range(c-1,-1,-1):  # 从右到左dp
        for j in range(c-1,i,-1):
            if arr[i] <= arr[j]:
                continue
            elif res2[i] < res2[j] + 1:
                res2[i] += 1
    for i in range(c):
        res[i]  =res1[i] + res2[i]

    ret = c - max(res) + 1
    return ret

while 1:
    n = input()
    arr = list( map(int, input().split()) )
    print(solution(arr))
