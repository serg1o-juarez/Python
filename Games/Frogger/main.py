from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(height=600,width=600)
screen.tracer(0)
player = Player()
screen.listen()
screen.onkey(player.move_forward, 'Up')
scoreboard = ScoreBoard()
car_manager=CarManager()









gameon=True
while gameon:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            gameon = False
            scoreboard.game_over()

    if player.ycor() >= 280:
        player.reset()
        scoreboard.clear_level()
        scoreboard.update_scoreboard()
        car_manager.level_up()




screen.exitonclick()
