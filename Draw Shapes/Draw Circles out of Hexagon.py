import turtle

def draw_hexagon(vHexagon):
    for i in range (1, 7):
        vHexagon.forward(100)
        vHexagon.right(60)
        
def draw():
    window = turtle.Screen()
    window.bgcolor('red')

    brad = turtle.Turtle()
    brad.color('yellow')
    brad.shape('turtle')
    brad.speed(20)
    
    #draw_hexagon(brad)
    for i in range (1, 74):
        draw_hexagon(brad)
        brad.right(5)

    brad.hideturtle()
    window.exitonclick()
    
draw()