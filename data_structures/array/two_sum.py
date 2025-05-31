# data_structures/array/two_sum.py

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表法：一次遍历 O(n)
        lookup = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in lookup:
                return [lookup[diff], i]
            lookup[num] = i
        return []

def test_two_sum():
    s = Solution()
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4])
    ]
    for idx, (nums, target, expected) in enumerate(test_cases):
        output = s.twoSum(nums, target)
        assert sorted(output) == sorted(expected), f"Test {idx} failed: expected {expected}, got {output}"
    print("所有测试用例通过！")

if __name__ == "__main__":
    test_two_sum()
