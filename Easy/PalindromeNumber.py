# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        y = x
        count = 0
        while y > 0:
            y = y // 10
            count += 1

        for i in range(count // 2):
            unit_digit = x % 10
            first_digit = x // 10 ** (count - 1)

            if unit_digit != first_digit:
                return False

            x = (x - first_digit * (10 ** (count - 1))) // 10
            count -= 2

        return True


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.isPalindrome(-121) == False
        assert test.isPalindrome(123454321) == True
        assert test.isPalindrome(1231) == False
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
