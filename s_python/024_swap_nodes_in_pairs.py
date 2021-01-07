"""
两两交换链表中的节点

给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

输入：head = [1,2,3,4]
输出：[2,1,4,3]


提示：
链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def swapPairs(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if head.next is None:
            return head
        first = head.next
        prev = first
        while head.next:

            _n = head.next
            # head.val, _n.val = _n.val, head.val
            head.next, _n.next = _n.next, head
            if _n != prev:
                prev.next = _n
            prev = head

            if head.next is not None:
                head = head.next
            else:
                break

        return first


if __name__ == '__main__':
    _first = ListNode(1)
    _first.next = ListNode(2)
    head = _first.next
    for i in range(3, 6):
        _next = ListNode(i)
        head.next = _next
        head = _next

    s = Solution()
    res = s.swapPairs(_first)

    while res.next:
        print(res.val)
        res = res.next
