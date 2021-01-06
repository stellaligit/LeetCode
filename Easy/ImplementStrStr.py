# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        else:
            return haystack.index(needle)


if __name__ == "__main__":
    try:

        test = Solution()
        assert test.strStr("hello", "ll") == 2
        assert test.strStr("aaaaa", "bba") == -1
        assert test.strStr("", "") == 0
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
