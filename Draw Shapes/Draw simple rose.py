import turtle
def draw_circles(vcircle):
	vcircle.circle(5)
	vcircle.circle(10)
	vcircle.circle(15)
	vcircle.circle(20)
	vcircle.circle(25)
	vcircle.circle(30)

def right_direction(vcircle):
	vcircle.right(90)

def draw_rose_side(vcolor, vcircle):
	vcircle.color(vcolor)
	draw_circles(vcircle)
	right_direction(vcircle)

def draw_rose(vcircle):
	colors = ["blue", "red", "yellow", "green"]
	for color in colors:
		draw_rose_side(color, vcircle)

def draw():
	window = turtle.Screen()
	window.bgcolor("black")

	brad = turtle.Turtle()
	brad.shape("circle")
	brad.speed(10)

	draw_rose(brad)
	brad.hideturtle()

	window.exitonclick()

draw()