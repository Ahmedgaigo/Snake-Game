from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scoreboard(Turtle):
	def __init__(self):
		super().__init__()
		self.pu()
		self.score = 0
		# read data from file
		with open("data.txt", 'r') as data:
			self.high_score = int(data.read())
		self.color("white")
		self.goto(0, 270)
		self.update_score()
		self.hideturtle()

	def increase_score(self):
		self.score += 1
		self.update_score()

	def update_score(self):
		self.clear()
		self.write(f"Score: {self.score}  High Score: {self.high_score}", False, ALIGNMENT, FONT)

	def reset(self):
		if self.score > self.high_score:
			self.high_score = self.score
			# writing high score into file
			with open("data.txt", 'w') as data:
				data.write(str(self.score))
		self.score = 0
		self.update_score()



