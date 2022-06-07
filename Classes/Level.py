from Classes.Ball import Ball


class Level:
    def __init__(self):
        self. initial = True
        self.pause = True
        self.number = 1

    def toggle_pause(self):
        if self.pause:
            self.pause = False
            print(self.pause)
            return
        self.pause = True

    # def shoot_ball(self,ball):
    #     ball.x_speed = random()
