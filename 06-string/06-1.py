import unittest
from collections import defaultdict
from typing import List

"""
05 가장 긴 팰린드롬 부분 문자열
    - 가장 긴 팰린드롬 부분 문자열을 출력하라

* 풀이 1 정렬하여 딕셔너리에 추가
"""


def solve(s: str) -> str:
    # 팰린드롬 판별 및 투 포인터 확장
    def expand(left: int, right: int) -> str:

        s_length = len(s)
        s_left = s[left]
        s_right = s[right]
        check_a = left >= 0
        check_b = right < s_length
        check_c = s_left == s_right

        while (left >= 0) and (right < len(s)) and (s[left] == s[right]):

            left -= 1
            right += 1

            s_length = len(s)
            s_left = s[left]
            s_right = s[right]
            check_a = left >= 0
            check_b = right < s_length
            check_c = s_left == s_right
            print()

        r = s[left + 1:right]
        return r

    # 해당 사항이 없을 때 빠르게 리턴
    s_reverse = s[::-1]
    if (len(s) < 2) or (s == s_reverse):  # 입력된 단어가 1개이거나, 이미 펠린도롬이면 ==> 자기자신이 가장 긴 펠린도롬 이므로, 그대로 리턴 // 0 이하이면 애초에 판별 불가
        return s

    result = ''
    # 슬라이딩 윈도우 우측으로 이동
    s_len = len(s)
    for i in range(s_len - 1):
        result = max(result, expand(i, i + 1), expand(i, i + 2), # 빈 문자, 홀수, 짝수
                     key=len)  # ?? key=len => 리턴된 문자열의 길이를 기준 // ?? result = '' 를 넣은 이유?

    return result


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual("bab", solve("babad"))

    def test_case02(self):
        self.assertEqual("bb", solve("cbbd"))


if __name__ == "__main__":
    unittest.main()
