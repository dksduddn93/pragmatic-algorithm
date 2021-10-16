import unittest


def solve(input: str):
    filtered = []
    for char in input:
        if char.isalnum():
            filtered.append(char)


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertTrue("A man a plan, a canal: Panama")

    def test_case02(self):
        self.assertFalse("race a car")

"""
주어진 문자열이 팰린드롬인지 확인하라. 대소문자를 구분하지 않으며 영문자와 숫자만을 대상으로 한다.

# 풀이 

1. 문자열을 모두 바꾼다. 
"""

if __name__ == "__main__":
    unittest.main()
