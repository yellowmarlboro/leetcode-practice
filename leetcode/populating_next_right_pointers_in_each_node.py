"""
116. 填充每个节点的下一个右侧节点指针
给定一个完美二叉树，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。
初始状态下，所有 next 指针都被设置为 NULL。

示例： https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/116_sample.png
输入：
{
    "$id":"1",
    "left":{
        "$id":"2",
        "left":{
            "$id":"3",
            "left":null,
            "next":null,
            "right":null,
            "val":4
        },
        "next":null,
        "right":{
            "$id":"4",
            "left":null,
            "next":null,
            "right":null,
            "val":5
        },
        "val":2
    },
    "next":null,
    "right":{
        "$id":"5",
        "left":{
            "$id":"6",
            "left":null,
            "next":null,
            "right":null,
            "val":6
        },
        "next":null,
        "right":{
            "$id":"7",
            "left":null,
            "next":null,
            "right":null,
            "val":7
        },
        "val":3
    },
    "val":1
}
输出：
{
    "$id":"1",
    "left":{
        "$id":"2",
        "left":{
            "$id":"3",
            "left":null,
            "next":{
                "$id":"4",
                "left":null,
                "next":{
                    "$id":"5",
                    "left":null,
                    "next":{
                        "$id":"6",
                        "left":null,
                        "next":null,
                        "right":null,
                        "val":7
                    },
                    "right":null,
                    "val":6
                },
                "right":null,
                "val":5
            },
            "right":null,
            "val":4
        },
        "next":{
            "$id":"7",
            "left":{
                "$ref":"5"
            },
            "next":null,
            "right":{
                "$ref":"6"
            },
            "val":3
        },
        "right":{
            "$ref":"4"
        },
        "val":2
    },
    "next":null,
    "right":{
        "$ref":"7"
    },
    "val":1
}
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。

提示：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
"""
# Definition for a Node.
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    # def walk2right(self, current: 'None') -> 'Node':
    #     current.left.next = current.right
    #     if current.next:
    #         current.right.next = current.next.left
    #         self.walk2right(current.next)

    # def connect(self, root: 'Node') -> 'Node':
    #     if not root:
    #         return root
    #     current = root
    #     while current.left:
    #         self.walk2right(current)
    #         current = current.left
    #     return root

    def connect(self, root: 'Node') -> 'Node':

        if not root:
            return root
        # 初始化队列同时将第一层节点加入队列中，即根节点
        Q = collections.deque([root])

        # 外层的 while 循环迭代的是层数
        while Q:

            # 记录当前队列大小
            size = len(Q)
            # 遍历这一层的所有节点
            for i in range(size):
                # 从队首取出元素
                node = Q.popleft()
                # 连接
                if i < size - 1:
                    node.next = Q[0]
                # 拓展下一层节点
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)

        # 返回根节点
        return root
