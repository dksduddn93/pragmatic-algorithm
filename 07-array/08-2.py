import unittest
from typing import List

"""
08 빗물 트래핑
    - 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.
 
* 풀이 2 스택 쌓기
"""


def solve(self, height: List[int]) -> int:
    stack = []
    volume = 0

    for i in range(len(height)):
        # 변곡점을 만나는 경우
        while stack and height[i] > height[stack[-1]]:
            # 스택에서 꺼낸다
            top = stack.pop()

            if not len(stack):
                break

            # 이전과의 차이만큼 물 높이 처리
            distance = i - stack[-1] - 1
            waters = min(height[i], height[stack[-1]]) - height[top]

            volume += distance * waters

        stack.append(i)
    return volume


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(6, solve([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

    def test_case02(self):
        self.assertEqual(9, solve([4, 2, 0, 3, 2, 5]))


if __name__ == "__main__":
    unittest.main()
