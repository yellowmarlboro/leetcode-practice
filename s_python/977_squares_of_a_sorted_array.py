"""
有序数组的平方

给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。

示例 1：
输入：[-4,-1,0,3,10]
输出：[0,1,9,16,100]

示例 2：
输入：[-7,-3,2,3,11]
输出：[4,9,9,49,121]

提示：

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
A 已按非递减顺序排序。
"""

from typing import List


class Solution:

    def sortedSquares(self, A: List[int]) -> List[int]:
        from collections import deque
        # index = 0
        # while index <= len(A) - 1:
        #     if A[0] < 0:
        #         num = A.pop(0)
        #         for idx, item in enumerate(A):
        #             if abs(num) <= item:
        #                 A.insert(idx, abs(num))
        #                 break
        #         else:
        #             A.append(abs(num))
        #     else:
        #         A[index] *= A[index]
        #         index += 1
        #
        # return A

        lis = deque()
        ret = []
        if not A:
            return A
        while A:
            if A[0] < 0:
                lis.appendleft(abs(A.pop(0)))
            else:
                break
        print(lis)
        while lis and A:
            n = lis[0]
            m = A[0]
            if n <= m:
                ret.append(n**2)
                lis.popleft()
            else:
                ret.append(m**2)
                A.pop(0)
        print(ret)
        ret.extend([i**2 for i in lis]) if lis else ret.extend([j**2 for j in A])
        return ret


if __name__ == "__main__":
    s = Solution()
    print(s.sortedSquares([-4,-1,0,3,10]))
