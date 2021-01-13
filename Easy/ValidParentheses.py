# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                if ((ch == ")" and stack[-1] == "(") or
                    (ch == "]" and stack[-1] == "[") or
                        (ch == "}" and stack[-1] == "{")):
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.isValid("()[]") == True
        assert test.isValid("({[]})") == True
        assert test.isValid("[)") == False
        assert test.isValid("[(]{)}") == False
        assert test.isValid("(") == False
        assert test.isValid("]") == False
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
