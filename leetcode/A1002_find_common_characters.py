"""
1002. 查找常用字符
给定仅有小写字母组成的字符串数组 A，返回列表中的每个字符串中都显示的全部字符（包括重复字符）组成的列表。
例如，如果一个字符在每个字符串中出现 3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。
示例 1：

输入：["bella","label","roller"]
输出：["e","l","l"]
示例 2：

输入：["cool","lock","cook"]
输出：["c","o"]


提示：

1 <= A.length <= 100
1 <= A[i].length <= 100
A[i][j] 是小写字母
"""
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if not A:
            return A
        dic = {}
        for word in A[0]:
            dic[word] = [1, 0] if word not in dic else [dic[word][0] + 1, 0]
        for item in A[1:]:
            for word in item:
                if word in dic:
                    # dic[word] = 1
                    if dic[word][1] < dic[word][0]:
                        dic[word][1] += 1
            dic = dict(filter(lambda x: False if x[1][1] == 0 else True, dic.items()))
            dic = dict(map(lambda x: (x[0], [x[1][1], 0]), dic.items()))
        lis = []
        for k, v in dic.items():
            lis.extend(v[0] * [k])
        return lis


if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]))
    # print(s.commonChars(["acabcddd","bcbdbcbd"]))