import collections
import unittest
from typing import Deque


def solve(s: str):
    filtered = []
    for char in s:
        if char.isalnum():
            filtered.append(char)

    # input이 유효하지 않으면 리턴 처리
    print(filtered)
    while len(filtered) > 1:
        if filtered.pop(0) != filtered.pop():
            print(filtered)
            return False
    return True


def solve2(s: str) -> bool:
    strs: Deque = collections.deque()
    for char in s:
        if char.isalnum():
            strs.append(char)
    while len(str) > 1:
        if strs.popleft() != strs.pop():
            return False
    return True


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
    solve("race a car")
