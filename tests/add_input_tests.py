import unittest
from mrap.add_input import add_input
from dtreg.load_datatype import load_datatype


class TestAddInput(unittest.TestCase):

    def test_input_inst_name(self):
        dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
        input_inst = add_input(dt, "XXX")
        self.assertEqual(dt.data_item.dt_name, input_inst.dt_name)

    def test_input_wrong_argument(self):
        dt = load_datatype("https://doi.org/21.T11969/b9335ce2c99ed87735a6")
        self.assertRaises(TypeError,
                          "Argument data_input should be a pd.DataFrame, a dictionary, or a string",
                          add_input, dt, 7)


if __name__ == '__main__':
    unittest.main()
