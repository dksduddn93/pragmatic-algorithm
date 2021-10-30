import unittest
from typing import List

"""
02 문자열 뒤집기
 - 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
 - 01 투포인터
"""


def solve(input_value: List[str]) -> List[str]:
    input_value = input_value[::-1]  # 공간 복잡도를 O(1) 제한 ?

    return input_value


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(["o", "l", "l", "e", "h"], solve(["h", "e", "l", "l", "o"]))

    def test_case02(self):
        self.assertEqual(["h", "a", "n", "n", "a", "H"], solve(["H", "a", "n", "n", "a", "h"]))


if __name__ == "__main__":
    unittest.main()
