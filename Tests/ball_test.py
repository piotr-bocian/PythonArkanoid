import unittest
from Classes.Ball import Ball
from Classes.Paddle import Paddle
from Classes.Brick import Brick


class TestBallMethods(unittest.TestCase):

    def test_fallen_check(self):
        ball1 = Ball(0, 0)
        ball2 = Ball(0, 1000)
        self.assertEqual(ball1.check_if_fallen(), False)
        self.assertEqual(ball2.check_if_fallen(), True)

    def test_check_hit_paddle(self):
        paddle = Paddle(100,700)
        ball1 = Ball(0, 0)
        ball2 = Ball(0, 688)
        ball3 = Ball(110, 0)
        ball4 = Ball(110, 688)
        self.assertEqual(ball1.check_hit_paddle(paddle), False)
        self.assertEqual(ball2.check_hit_paddle(paddle), False)
        self.assertEqual(ball3.check_hit_paddle(paddle), False)
        self.assertEqual(ball4.check_hit_paddle(paddle), True)

    def test_check_hit_brick(self):
        brick = Brick(100,700)
        ball1 = Ball(0, 0)
        ball2 = Ball(0, 688)
        ball3 = Ball(110, 0)
        ball4 = Ball(110, 688)
        self.assertEqual(ball1.check_hit_paddle(brick), False)
        self.assertEqual(ball2.check_hit_paddle(brick), False)
        self.assertEqual(ball3.check_hit_paddle(brick), False)
        self.assertEqual(ball4.check_hit_paddle(brick), True)


if __name__ == '__main__':
    unittest.main()
