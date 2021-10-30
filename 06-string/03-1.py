import unittest
from typing import List

"""
03 로그파일 재정렬
 - 로그를 재정렬하라. 기준은 다음과 같다.
    1. 로그의 가장 앞 부분은 식별자다.
    2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
    3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
    4. 숫자 로그는 입력 순서대로 한다.
    
* 풀이 1 람다와 + 연산자를 이용
"""


def solve(input_value: List[str]) -> List[str]:
    input_value = input_value[::-1]  # 공간 복잡도를 O(1) 제한 ?

    return input_value


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(
            ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
            solve(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
        )

    def test_case02(self):
        self.assertEqual(solve(["H", "a", "n", "n", "a", "h"]), ["h", "a", "n", "n", "a", "H"])


if __name__ == "__main__":
    unittest.main()
