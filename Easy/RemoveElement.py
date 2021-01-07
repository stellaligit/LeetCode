# https://leetcode.com/problems/remove-element/

class Solution:
    def removeElement(self, nums: [], val: int) -> int:
        c = len(nums)
        for i in range(c-1, -1, -1):
            if nums[i] == val:
                nums.remove(nums[i])

        return len(nums)


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.removeElement([3, 2, 2, 3], 3) == 2
        assert test.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2) == 5
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
