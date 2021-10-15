import unittest

def solve(input):
    return 1

class TestMethod(unittest.TestCase):
    def test_case01(self):
        result = solve(1)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
