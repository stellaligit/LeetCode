# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""

        ans = []
        for i in range(len(strs[0])):
            ch = strs[0][i]
            flag = True

            for j in strs:
                if i >= len(j) or j[i] != ch:
                    flag = False
                    break

            if flag:
                ans.append(ch)
            else:
                break

        return "".join(ans)


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.longestCommonPrefix(["fly", "flu", "flew"]) == "fl"
        assert test.longestCommonPrefix(["a", "b", "c"]) == ""
        assert test.longestCommonPrefix(["abc", "ab", "abd"]) == "ab"
        assert test.longestCommonPrefix(["a", "a", "b"]) == ""
        assert test.longestCommonPrefix(["fly", "flu", "flew"]) == "fl"
        assert test.longestCommonPrefix([]) == ""
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
