import turtle

def draw_square(vSquare):
    for i in range (1, 5):
        vSquare.forward(100)
        vSquare.right(90)

def draw():
    window = turtle.Screen()
    window.bgcolor('purple')
   
    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('turtle')
    brad.speed(20)
    
    for i in range (1, 74):
        draw_square(brad)
        brad.right(5)
    
    window.exitonclick()
    
draw()