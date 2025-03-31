import unittest
from mrap.add_input import add_input
from dtreg.load_datatype import load_datatype


class TestTarget(unittest.TestCase):

    def target_inst_name(self):
        dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
        target_inst = add_target(dt, ["XXX", 100, 12])
        self.assertEqual(dt.data_item.dt_name, input_inst.dt_name)


if __name__ == '__main__':
    unittest.main()
