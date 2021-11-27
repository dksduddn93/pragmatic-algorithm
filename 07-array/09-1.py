import unittest
from typing import List

"""
08 세 수의 합
    - 배열을 입력받아 합으로 0을 만들 수 이쓴ㄴ 3개의 엘러먼트를 출력하라.
 
* 풀이 1 브루트 포스로 계산
"""


def solve(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    # 브루트 포스 n^3 반복
    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 1):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            for k in range(j + 1, len(nums)):
                if k > j + 1 and nums[k] == nums[k - 1]:
                    continue
                if nums[i] + nums[j] + nums[k] == 0:
                    results.append([nums[i], nums[j], nums[k]])

    return results


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual([[-1, -1, 2], [-1, 0, 1]], solve([-1, 0, 1, 2, -1, -4]))

    def test_case02(self):
        self.assertEqual([], solve([]))

    def test_case03(self):
        self.assertEqual([], solve([0]))


if __name__ == "__main__":
    unittest.main()
