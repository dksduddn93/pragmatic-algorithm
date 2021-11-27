import unittest
from typing import List

"""
07 두수의 합
    - 덧셈하여 타겟을 만들수 있는 배열의 두 숫자 인덱스를 리턴하라.
 
* 풀이 4 조회 구조 개선
"""


def solve(self, nums: List[int], target: int) -> List[int]:
    nums_map = {}
    # 키와 값을 바꿔서 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target - num in nums_map and i != nums_map[target - num]:
            return [i, nums_map[target - num]]


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual([0, 1], solve([2, 7, 11, 15], 9))

    def test_case02(self):
        self.assertEqual([1, 2], solve([3, 2, 4], 6))

    def test_case03(self):
        self.assertEqual([0, 1], solve([3, 3], 6))


if __name__ == "__main__":
    unittest.main()
