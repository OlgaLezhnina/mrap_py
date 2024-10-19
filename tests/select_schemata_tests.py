import unittest
from mrap.select_schemata import select_stat_test_diff


class TestSelectStatDiff(unittest.TestCase):

    def test_select_stat_diff_epic(self):
        dt = select_stat_test_diff("epic")
        dt_diff = dt.statistical_test_of_difference()
        self.assertEqual(dt_diff.dt_id, "ff5e3f857788d20dd1aa")

    def test_select_stat_diff_orkg(self):
        dt = select_stat_test_diff("orkg")
        dt_diff = dt.statistical_test_of_difference()
        self.assertEqual(dt_diff.dt_id, "R836000")

    def test_select_stat_diff_wrong_dtr(self):
        select_stat_test_diff("wrong_dtr")
        self.assertRaisesRegex(
            ValueError,
            "SystemExit: The dtr can be only epic or orkg")


if __name__ == '__main__':
    unittest.main()
