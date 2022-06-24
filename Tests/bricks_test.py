import unittest
from Classes.Bricks import Bricks


class TestPaddleMethods(unittest.TestCase):

    def test_add_remove_brick(self):
        bricks = Bricks()
        self.assertEqual(len(bricks.bricks_array),0)
        bricks.add_brick(0,0)
        self.assertEqual(len(bricks.bricks_array),1)
        bricks.remove_brick(bricks.bricks_array[0])
        self.assertEqual(len(bricks.bricks_array),0)



if __name__ == '__main__':
    unittest.main()
