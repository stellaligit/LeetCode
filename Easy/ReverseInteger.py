# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        m = abs(x)
        r = 0
        ans = 0
        while m > 0:
            r = m % 10
            m = m // 10
            ans = ans * 10 + r

        if ans > 2147483647:
            return 0
        elif x >= 0:
            return ans
        else:
            return ans * -1

        # Q: BUT what if there is... OH NO! OVERFLOW!
        # A: Um, we already figured out a solution to that.
