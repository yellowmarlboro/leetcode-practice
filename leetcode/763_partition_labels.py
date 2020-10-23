"""
763. 划分字母区间
字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。

示例：
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

提示：
S的长度在[1, 500]之间。
S只包含小写字母 'a' 到 'z' 。
"""
from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        dic = dict()
        res = []
        idx = 0
        # length = len(S)
        # while idx <= len(S) - 1:
        for idx, item in enumerate(S):
            # item = S[idx]
            if item not in dic:
                dic[item] = idx
            else:
                for i in range(len(res)-1, -1, -1):
                    if res[i] >= dic[item]:
                        res.pop()
            res.append(idx)
            # idx += 1
        idx = len(res) - 1
        while idx > 0:
            res[idx] = res[idx] - res[idx-1]
            idx -= 1
        if res:
            res[0] = res[0] + 1

        return res
