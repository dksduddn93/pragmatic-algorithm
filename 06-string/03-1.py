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


def solve(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        temp = log.split()[1]
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 문자 로그는 정렬 요구, 숫자 로그는 입력 그대로

    for x in letters:
        s1 = x.split()[1:]  # 정렬. 첫번쨰 키 - 로그 내용
        s2 = x.split()[0]  # 정렬. 두번째 키 - 식별자
        print(s1)
        print(s2)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))  # ? 첫번째 키가 리스트인대. 리스트를 키로 정렬이 가능한건 파이썬만의 특징인지?


    return letters + digits


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(
            ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"],
            solve(["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"])
        )


if __name__ == "__main__":
    unittest.main()
