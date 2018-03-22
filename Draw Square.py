import turtle

def draw_square(sturtle):
	for x in range(1,5):
		sturtle.forward(100)
		sturtle.right(90)

def draw():
	window = turtle.Screen()
	window.bgcolor("black")

	#Draw Square
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("red")
	brad.speed(5)
	draw_square(brad)

	window.exitonclick()

draw()