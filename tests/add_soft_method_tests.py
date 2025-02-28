import unittest
from mrap.add_soft_method import add_soft_method
from dtreg.load_datatype import load_datatype


class TestSoftMethod(unittest.TestCase):
    def test_soft_method_inst_name(self):
        dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
        soft_method_inst = add_soft_method(dt, "scipy", "f_oneway")
        self.assertEqual(dt.software_method.dt_name, soft_method_inst.dt_name)

    def test_soft_method_label(self):
        dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
        soft_method_inst = add_soft_method(dt, "scipy", "f_oneway")
        self.assertEqual(soft_method_inst.label, "f_oneway")

    def test_soft_method_lib_label(self):
        dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
        soft_method_inst = add_soft_method(dt, "scipy", "f_oneway")
        self.assertEqual(soft_method_inst.part_of.label, "scipy")


if __name__ == '__main__':
    unittest.main()
