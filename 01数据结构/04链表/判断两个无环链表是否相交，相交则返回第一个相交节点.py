'''
题目：判断两个无环链表是否相交，相交则返回第一个相交节点

思路：
1. 则先判断链表的尾指针是否一样，如果不一样，则没有相交
2. 如果一样，则找出两个链表的长度差，将两个链表从距离尾节点同样的距离进行扫描，如果相交，
 则必然有一处扫描节点相同。实例数据List1：1->2->3->4->5->6->7->null，List2：0->9->8->6->7->null，第一个相交节点为6
'''
class Node():
    def __init__(self, val=None):
        self.val = val
        self.next = None

def Loop(head1, head2):
    n1 = 0
    n2 = 0
    cur1 = head1
    cur2 = head2
    while cur1 != None:
        n1 += 1
        cur1 = cur1.next
        print(n1)
    while cur2 != None:
        n2 += 1
        cur2 = cur2.next
        print(n2)

    n = abs(n1 - n2)
    print(n)
    cur1 = head1
    cur2 = head2
    if n1 > n2:
        while n > 0:
            cur1 = cur1.next
    else:
        while n > 0:
            cur2 = cur2.next

    while cur1 != cur2:
        cur1 = cur1.next
        cur2 = cur2.next
    return cur1

node1 = Node([1, 2, 3])
node2 = Node([2, 3])
print(Loop(node1, node2))