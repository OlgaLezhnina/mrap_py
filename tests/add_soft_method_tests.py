import unittest
from unittest.mock import patch
from mrap.add_soft_method import add_soft_method
from dtreg.load_datatype import load_datatype


class TestSoftMethod(unittest.TestCase):

    def test_soft_method_label(self):
        new_dt = load_datatype("https://doi.org/21.T11969/ff5e3f857788d20dd1aa")
        with patch('mrap.add_soft_method.dt', new_dt):
            soft_method_inst = add_soft_method("scipy", "f_oneway")
            self.assertEqual(soft_method_inst.label, "f_oneway")


if __name__ == '__main__':
    unittest.main()
