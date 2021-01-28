# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, s: str) -> int:
        string = ""
        cur_ch = s[0]
        count = 1

        for ch in s[1:]:
            if ch == cur_ch:
                count += 1
            else:
                string += str(count)
                string += cur_ch
                cur_ch = ch
                count = 1

        string += str(count)
        string += cur_ch
        return int(string)


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.countAndSay(1) == "1"
        assert test.countAndSay(2) == "11"
        assert test.countAndSay(3) == "21"
        assert test.countAndSay(4) == "1211"
        assert test.countAndSay(5) == "111221"
        assert test.countAndSay(6) == "312211"
        assert test.countAndSay(7) == "13112221"
        assert test.countAndSay(8) == "1113213211"
        assert test.countAndSay(9) == "31131211131221"
        assert test.countAndSay(10) == "13211311123113112211"
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
