import unittest
from typing import List

"""
08 세 수의 합
    - 배열을 입력받아 합으로 0을 만들 수 이쓴ㄴ 3개의 엘러먼트를 출력하라.
 
* 풀이 2 투 포인터로 합 계산
"""


def solve(self, nums: List[int]) -> List[List[int]]:
    results = []
    nums.sort()

    for i in range(len(nums) - 2):
        # 중복된 값 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # 간격을 좁혀가며 합 `sum` 계산
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # `sum = 0`인 경우이므로 정답 및 스킵 처리
                results.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1

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
