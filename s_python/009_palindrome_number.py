"""
9. 回文数
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
"""


class Solution:

    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        if 0 <= x < 10:
            return True
        revert_num = 0
        mc = 0
        _x = x
        while revert_num < x:
            revert_num = revert_num * 10 + _x % 10
            mc += 1
            _x = _x // 10
            if 0 < _x // 10**mc < 10:
                return _x // 10 == revert_num

            elif _x // 10**mc == 0:
                return _x == revert_num


if __name__ == "__main__":
    s = Solution()
    s.isPalindrome(1)
