import re
import unittest
from collections import defaultdict, Counter
from typing import List

"""
04 [ 가장 흔한 단어
    - 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점 (마침표, 쉼표 등) 또한 무시한다.
    
* 풀이 1 리스트 컴프리헨션, Counter 객체 사용
"""


def solve(paragraph: str, banned: List[str]) -> str:
    words = [
        word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split()
        if word not in banned
    ]

    counts = Counter(words)
    w1 = counts.most_common(1)  # [('ball', 2)]
    w2 = w1[0]
    w3 = w2[0]

    """
    replace_words: str = re.sub(r'[^\w]', ' ', paragraph)  # r : 특수문자 원문 그대로
    lower_words: str = replace_words.lower()
    split_words: str = lower_words.split()
    words = [
        word for word in split_words
        if word not in banned
    ]

    counts = defaultdict(lambda: 0)
    for word in words:
    counts[word] += 1

    print()
    """

    return w3


class TestClass(unittest.TestCase):

    def test_case01(self):
        self.assertEqual(
            "ball",
            solve("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])
        )


if __name__ == "__main__":
    unittest.main()
