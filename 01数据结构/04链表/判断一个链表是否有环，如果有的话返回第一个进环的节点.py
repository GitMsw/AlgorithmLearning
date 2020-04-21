'''
题目：判断一个链表是否有环，如果有则返回第一个进环的结点

思路：
1 判断是否有环：快慢指针，fast=2n，slow=1n
2 返回第一个结点，指针slow不动，fast继续从头开始

'''

class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None

def getloopmeet(head):
    fast = head.next.next
    slow = head.next
    while fast != slow:
        if fast == None or slow == None:
            return None
        fast = fast.next.next
        slow = slow.next
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    return fast

tt = 0 
class LinkList:
    def __init__(self):
        self.head=None

    def initList(self, data):
        # 创建头结点
        self.head = Node(data[0])
        r=self.head
        p = self.head
        # 逐个为 data 内的数据创建结点, 建立链表
        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next
        return r
    def printlist(self,head):
        global tt
        if head == None: return
        node = head
        while node != None:
            print(node.val,node)
            node = node.next
            if tt > 8:
                break
            tt += 1
if __name__ == '__main__':
    L = LinkList()
    # 创建头结点
    head = Node(1)
    L.head = head
    r = head
    p = head
    # 逐个为 data 内的数据创建结点, 建立链表
    p.next = Node(2)
    p = p.next     
    p.next = Node(3)
    p = p.next
    pp = p
    p.next = Node(4)
    p = p.next 
    p.next = Node(5)
    p = p.next
    p.next = Node(6)
    p = p.next
    p.next = pp

    print('rrr=',r)
    L.printlist(r)
    print()
    print('结果=',getloopmeet(r))