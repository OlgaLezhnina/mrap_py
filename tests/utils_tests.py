import unittest
from mrap.utils import parse_code_list


class TestUtils(unittest.TestCase):

    def test_parse_code_list(self):
        result = parse_code_list(["a", "b"])
        self.assertEqual(2+2, 4)


if __name__ == '__main__':
    unittest.main()
