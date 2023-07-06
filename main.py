from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)  # set st 0 doesn't make anything move

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")

game_on = True
while game_on:
	screen.update()
	time.sleep(0.1)
	snake.move()

	# Detect collision with food
	if snake.head.distance(food) < 15:
		food.refresh()
		snake.extend()  # extends the snake anytime it eats a food
		score.increase_score()

	# Detect collision with wall
	if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
		score.reset()
		snake.start_over()

	# Detect collision with tail
	for segment in snake.box[1:]:
		if snake.head.distance(segment) < 10:
			score.reset()
			snake.start_over()

screen.exitonclick()
