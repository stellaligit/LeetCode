# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt1(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        ans = 0
        for i in range(len(s)):
            ans += m[s[i]]
            if i > 0 and m[s[i-1]] < m[s[i]]:
                ans -= 2 * m[s[i-1]]

        return ans

    def romanToInt2(self, s: str) -> int:
        m = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

        previous = 0
        ans = 0
        for ch in s[::-1]:
            current = m[ch]
            if previous > current:
                ans -= current
            else:
                ans += current
            previous = current

        return ans


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.romanToInt1("II") == 2
        assert test.romanToInt1("LVIII") == 58
        assert test.romanToInt1("MCMXCIV") == 1994
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")

if __name__ == "__main__":
    try:
        test = Solution()
        assert test.romanToInt2("II") == 2
        assert test.romanToInt2("LVIII") == 58
        assert test.romanToInt2("MCMXCIV") == 1994
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
