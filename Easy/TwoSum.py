# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum1(self, nums: [], target: int) -> []:
        a = len(nums)
        for i in range(a):
            d = target - nums[i]
            for j in range(i + 1, a):
                if d == nums[j]:
                    return [i, j]

    def twoSum2(self, nums: [], target: int) -> []:
        a = len(nums)
        for i in range(a):
            for j in range(i+1, a):
                if (nums[i] + nums[j]) == target:
                    return [i, j]

    def twoSum3(self, nums: [], target: int) -> []:
        m = {}
        a = len(nums)
        for i in range(a):
            if nums[i] in m:
                return [m[nums[i]], i]
            else:
                m[target-nums[i]] = i


if __name__ == "__main__":
    try:
        test = Solution()
        assert test.twoSum1([2, 7, 11, 15], 9) == [0, 1]
        assert test.twoSum2([2, 7, 11, 15], 9) == [0, 1]
        assert test.twoSum3([2, 7, 11, 15], 9) == [0, 1]
        print("Good job :)")

        import time
        import random

        print("create a really large list")
        start_time = time.time()
        nums = list(range(1, 10001))
        random.shuffle(nums)
        print(time.time() - start_time)
        print("init done. start to test.\r\n\r\n")

        start_time = time.time()
        res = test.twoSum1(nums, 19999)
        t = time.time() - start_time
        print("Test 1 ans:", res, "time:", t)

        start_time = time.time()
        res = test.twoSum2(nums, 19999)
        t = time.time() - start_time
        print("Test 2 ans:", res, "time:", t)

        start_time = time.time()
        res = test.twoSum3(nums, 19999)
        t = time.time() - start_time
        print("Test 3 ans:", res, "time:", t)

    except AssertionError:
        print("Error! Error! Oh no! Drumroll please! Don don don!!!")
