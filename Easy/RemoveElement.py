# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: [], val: int) -> int:
        i = 0

        c = len(nums)
        while i < c:
            if nums[i] == val:
                nums.remove(nums[i])
                c -= 1
            else:
                i += 1

        return len(nums)


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.removeElement([3, 2, 2, 3], 3) == 2
        assert test.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
