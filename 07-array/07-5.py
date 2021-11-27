import unittest
from typing import List

"""
07 두수의 합
    - 덧셈하여 타겟을 만들수 있는 배열의 두 숫자 인덱스를 리턴하라.
 
* 풀이 4 조회 구조 개선
"""


def solve(self, nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        # 합이 타겟보다 크면 오른쪽 포인터를 왼쪽으로
        if nums[left] + nums[right] < target:
            left += 1
        # 합이 타겟보다 작으면 왼쪽 포인터를 오른쪽으로
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual([0, 1], solve([2, 7, 11, 15], 9))

    def test_case02(self):
        self.assertEqual([1, 2], solve([3, 2, 4], 6))

    def test_case03(self):
        self.assertEqual([0, 1], solve([3, 3], 6))


if __name__ == "__main__":
    unittest.main()
