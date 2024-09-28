import unittest
from mrap.add_soft_method import add_soft_method


class TestSoftMethod(unittest.TestCase):

    def test_soft_method_props(self):
        soft_method_inst = add_soft_method("Wilcoxon")
        props = ['label', 'uses_software', 'is_implemented_by', 'has_support_url']
        self.assertEqual(soft_method_inst.prop_list, props)


if __name__ == '__main__':
    unittest.main()
