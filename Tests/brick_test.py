import unittest
from Classes.Brick import Brick


class TestBrickMethods(unittest.TestCase):

    def test_is_powerUp(self):
        brick = Brick(0, 0)
        self.assertTrue(brick.is_powerUp()<=1 and brick.is_powerUp()>=0)

    def test_pick_poweUp(self):
        brick = Brick(0,0)
        self.assertTrue(brick.pick_powerUp()<5 and brick.pick_powerUp()>0)
        self.assertTrue(type(brick.pick_powerUp())==int)


if __name__ == '__main__':
    unittest.main()