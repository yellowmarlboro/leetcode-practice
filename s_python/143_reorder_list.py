"""
143. 重排链表
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
        items = [head]
        while head.next:
            items.append(head.next)
            head = head.next
        while items:
            if len(items) == 1:
                items[0].next = None
                break
            items.pop(0).next = items[-1]
            if len(items) == 1:
                items[-1].next = None
                break
            items.pop(-1).next = items[0]


if __name__ == "__main__":
    s = Solution()
    head = ListNode(val=1)
    first = head
    for i in range(1, 4):
        head.next = ListNode(val=i)
        head = head.next

    s.reorderList(first)
    print(head.val)