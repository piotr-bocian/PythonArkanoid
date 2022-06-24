import unittest
from Classes.Paddle import Paddle


class TestPaddleMethods(unittest.TestCase):

    def test_move_left(self):
        paddle1 = Paddle(200, 100)
        paddle2 = Paddle(180, 100)
        paddle3 = Paddle(0, 100)
        self.assertEqual(paddle1.move_left(), 199.3)
        self.assertEqual(paddle2.move_left(), 180)
        self.assertEqual(paddle3.move_left(), 0)

    def test_move_right(self):
        paddle1 = Paddle(200, 100)
        paddle2 = Paddle(1160, 100)
        paddle3 = Paddle(2000, 100)
        self.assertEqual(paddle1.move_right(), 200.7)
        self.assertEqual(paddle2.move_right(), 1160)
        self.assertEqual(paddle3.move_right(), 2000)


if __name__ == '__main__':
    unittest.main()
