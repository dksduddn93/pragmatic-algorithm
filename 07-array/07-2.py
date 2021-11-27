import unittest
from typing import List

"""
07 두수의 합
    - 덧셈하여 타겟을 만들수 있는 배열의 두 숫자 인덱스를 리턴하라.

* 풀이 2 in을 이용한 탐색
"""


def solve(self, nums: List[int], target: int) -> List[int]:
    for i, n in enumerate(nums):
        complement = target - n

        if complement in nums[i + 1:]:
            return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual([0, 1], solve([2, 7, 11, 15], 9))

    def test_case02(self):
        self.assertEqual([1, 2], solve([3, 2, 4], 6))

    def test_case03(self):
        self.assertEqual([0, 1], solve([3, 3], 6))


if __name__ == "__main__":
    unittest.main()
