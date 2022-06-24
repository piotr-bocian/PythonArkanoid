import unittest
from Classes.Level import Level


class TestLevelMethods(unittest.TestCase):

    def test_add_life(self):
        level = Level(1)
        level.add_life()
        self.assertEqual(level.lives, 4)

    def test_sub_life(self):
        level = Level(1)
        level.sub_life()
        self.assertEqual(level.lives, 2)

    def test_lost_check(self):
        level1 = Level(1)
        level2 = Level(1)
        level2.sub_life()
        level2.sub_life()
        level2.sub_life()
        self.assertEqual(level1.check_if_lost(), False)
        self.assertEqual(level2.check_if_lost(), True)


if __name__ == '__main__':
    unittest.main()
