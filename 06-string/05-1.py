import unittest
from collections import defaultdict
from typing import List

"""
05 그룹 애너그램
    - 문자열 배열을 받아 애너그램 단위로 그룹핑하라.

* 풀이 1 정렬하여 딕셔너리에 추가
"""


def solve(word_list: List[str]) -> List[List[str]]:
    anagrams = defaultdict(list)

    for word in word_list:
        sort_word = sorted(word)
        key = ''.join(sort_word)
        anagrams[key].append(word)

    result = list(anagrams.values())
    return result


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(
            [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]],
            solve(["eat", "tea", "tan", "ate", "nat", "bat"])
        )


if __name__ == "__main__":
    unittest.main()
