import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)


def draw_circle(some_turtle):
    for i in range(1,18):
        some_turtle.forward(10)
        some_turtle.right(25)
        
def spiral(some_turtle):
    for i in range(1,8):
        some_turtle.right(45)
        draw_circle(some_turtle)
    
        

def draw_art():
    
    window = turtle.Screen()
    window.bgcolor("red")
    bob = turtle.Turtle()
    bob.color("black")
    for i in range(1,5):
        bob.forward(25)
        spiral(bob)
    window.exitonclick()




draw_art()

    
