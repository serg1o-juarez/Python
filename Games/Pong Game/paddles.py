from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position, color):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(color)
        self.penup()
        self.goto(position)

    def move_up_paddle(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def move_down_paddle(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)


# class LeftPaddle(Turtle):
#     def __init__(self):
#         super().__init__()
#         self.shape('square')
#         self.shapesize(stretch_wid=5, stretch_len=1)
#         self.color('red')
#         self.penup()
#         self.goto(-350,0)

#     def move_up_left_paddle(self):
#         self.new_y = self.ycor() + 20
#         self.goto(self.xcor(),self.new_y)

#     def move_down_left_paddle(self):
#         self.new_y = self.ycor() - 20
#         self.goto(self.xcor(),self.new_y)

    
