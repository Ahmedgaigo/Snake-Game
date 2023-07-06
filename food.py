from turtle import Turtle
import random as r


# we want the food class to inherit from the Turtle class
class Food(Turtle):
	def __init__(self):
		super().__init__()
		# creating the shape of the food
		self.shape("circle")
		self.color("blue")
		self.pu()
		self.shapesize(0.5, 0.5)  # make the circle shape smaller
		self.speed("fastest")
		self.refresh()

	def refresh(self):
		random_x = r.randint(-280, 280)
		rand_y = r.randint(-280, 280)
		self.goto(random_x, rand_y)
