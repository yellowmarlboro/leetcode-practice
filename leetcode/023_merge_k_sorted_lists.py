"""
合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。
请你将所有链表合并到一个升序链表中，返回合并后的链表。

示例 1：
输入：lists = [[1,4,5],[1,3,4],[2,6]]
输出：[1,1,2,3,4,4,5,6]
解释：链表数组如下：
[
  1->4->5,
  1->3->4,
  2->6
]
将它们合并到一个有序链表中得到。
1->1->2->3->4->4->5->6
示例 2：

输入：lists = []
输出：[]
示例 3：

输入：lists = [[]]
输出：[]

提示：
k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] 按 升序 排列
lists[i].length 的总和不超过 10^4


how:
两两合并数组并排序，直到合并为一个数组为止，数组由 n个 => n/2 => n/4 => 1。
类似归并排序，两个合并为2路归并。
"""
from typing import List


# pre class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# code
class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        p1 = 0
        new_lists = []
        if not lists:
            return None
        while len(lists) > 1:
            if p1 > len(lists) - 1:
                lists = new_lists
                new_lists = []
                p1 = 0
            elif p1 == len(lists) - 1:
                new_lists.append(lists[p1])
                lists = new_lists
                new_lists = []
                p1 = 0
            else:
                l = self.merge_2_lists(lists[p1], lists[p1+1])
                new_lists.append(l)
                p1 += 2
        return lists[0]

    @staticmethod
    def merge_2_lists(l1, l2):
        new_node = ListNode()
        moved_node = new_node
        while l1 and l2:
            if l1.val < l2.val:
                moved_node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                moved_node.next = ListNode(l2.val)
                l2 = l2.next
            moved_node = moved_node.next
        moved_node.next = l1 if l1 else l2
        return new_node.next


if __name__ == '__main__':
    pass
