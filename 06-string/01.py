import unittest


def solve(input_value: str) -> bool:
    filtered = []
    for char in input_value:
        if char.isalnum():  # return : 영문자 true, 이외 false
            filtered.append(char.lower())  # 영어 소문자로 치환 후 리스트에 하나씩 넣기 => Filtered 는 이제 영어 소문자로만 이루어진 리스트

    while(len(filtered)) > 1:  # 홀수면 사이즈가 1인채로 반복 종료, 짝수면 사이즈가 0인채로 반복 종료
        if filtered.pop(0) != filtered.pop():  # stack. 첫문자,끝문자 꺼낸 후 비교
            return False  # 첫문자, 끝문자 불일치면 팰린도롬 아님
    return True  # 첫문자, 끝문자 모두 일치하므로 팰린도롬


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertTrue(solve("A man a plan, a canal: Panama"))

    def test_case02(self):
        self.assertFalse(solve("race a car"))

"""
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다.

# 풀이 

1. 문자열을 모두 바꾼다. 
"""

if __name__ == "__main__":
    unittest.main()
