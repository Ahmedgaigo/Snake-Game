from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
NEW_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
	def __init__(self):
		self.box = []
		self.create_snake()
		self.head = self.box[0]

	def create_snake(self):
		for position in STARTING_POSITIONS:
			self.add_segment(position)

	def add_segment(self, position):
		t = Turtle()
		t.color("white")
		t.shape('square')
		t.pu()
		t.setposition(position)
		self.box.append(t)

	def start_over(self):
		for box in self.box:
			box.goto(1000, 1000)
		self.box.clear()
		self.create_snake()
		self.head = self.box[0]

	def extend(self):
		self.add_segment(self.box[-1].position())

	def move(self):
		for each_box in range(len(self.box) - 1, 0, -1):
			new_x = self.box[each_box - 1].xcor()
			new_y = self.box[each_box - 1].ycor()
			self.box[each_box].goto(new_x, new_y)
		self.head.fd(NEW_DISTANCE)

	def right(self):
		if self.head.heading() != LEFT:
			self.head.seth(RIGHT)

	def left(self):
		if self.head.heading() != RIGHT:
			self.head.seth(LEFT)

	def up(self):
		if self.head.heading() != DOWN:
			self.head.seth(UP)

	def down(self):
		if self.head.heading() != UP:
			self.head.seth(DOWN)
