# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: []) -> int:
        length = len(nums)

        if length == 0:
            return 0

        i = 0
        t = nums[i]
        j = i + 1
        while j < length:
            if nums[j] != t:
                i += 1
                nums[i] = nums[j]
                t = nums[i]

            j += 1

        # print(nums, a)
        return i + 1


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.removeDuplicates([]) == 0
        assert test.removeDuplicates([2]) == 1
        assert test.removeDuplicates([2, 2, 2]) == 1
        assert test.removeDuplicates([2, 2, 2, 3, 3, 4]) == 3
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
