# https://leetcode.com/problems/two-sum/

# solution 1:
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = len(nums)
        for i in range(a):
            d = target - nums[i]
            for j in range(i + 1, a):
                if d == nums[j]:
                    return [i, j]

# solution 2:


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = len(nums)
        for i in range(a):
            for j in range(i+1, a):
                if (nums[i] + nums[j]) == target:
                    return [i, j]
