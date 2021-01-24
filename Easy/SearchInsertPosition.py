# https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: [], target: int) -> int:
        # if target not in nums:
        flag = False
        for i in nums:
            if i == target:
                flag = True

        if not flag:
            for i in range(len(nums)):
                if nums[-1] < target:
                    return len(nums)
                elif nums[0] > target:
                    return 0
                elif nums[i] < target and nums[i + 1] > target:
                    return i + 1

        for i in range(len(nums)):
            if nums[i] == target:
                return i


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.searchInsert([1, 3, 5, 6], 5) == 2
        assert test.searchInsert([1, 3, 5, 6], 2) == 1
        assert test.searchInsert([1, 3, 5, 6], 7) == 4
        assert test.searchInsert([1, 3, 5, 6], 0) == 0
        assert test.searchInsert([1], 0) == 0
        print("Good job :)")
    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
