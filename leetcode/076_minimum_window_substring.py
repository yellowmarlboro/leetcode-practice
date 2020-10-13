"""
给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：包含 T 所有字符的最小子串。

示例：
输入：S = "ADOBECODEBANC", T = "ABC"
输出："BANC"


提示：
如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

how:
采用 滑动窗口 思想。
一个宽度可变的窗口，由两侧指针控制窗口大小，先扩大窗口宽度满足要求，再缩小求最小子串。然后左指针往右移一位，继续之前的操作。
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        # 初始化字符key: count字典
        for item in t:
            dic[item] = 1 if item not in dic else dic[item] + 1
        left_pointer = 0
        count = len(t)
        min_str = ''
        length = float('inf')
        if not s:
            return ''
        for idx, item in enumerate(s):
            if item in dic:
                count -= 1 if dic[item] > 0 else 0
                dic[item] -= 1
            while count == 0:
                if s[left_pointer] in dic:
                    if dic[s[left_pointer]] < 0:
                        dic[s[left_pointer]] += 1
                    else:
                        min_str = s[left_pointer:idx + 1] if length > idx - left_pointer + 1 \
                            else min_str
                        length = len(min_str)
                        dic[s[left_pointer]] += 1
                        left_pointer += 1
                        count += 1
                        break
                left_pointer += 1

        return min_str
