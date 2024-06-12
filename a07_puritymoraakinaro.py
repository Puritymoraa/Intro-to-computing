#####################################################################
# Original Author: Purity Moraa Kinaro
# Program that incorporates turtles, functions and loops to
#tell help children know the big five animals.
#####################################################################
import turtle
import random
wn = turtle.Screen()
wn.bgcolor("lightblue")
wn.title("THE BIG FIVE ZOO")
name = turtle.Turtle()
name.shape("turtle")
name.pensize(5)
name.speed(10)
name.penup()
#Draw letter W
name.goto(-600, 200)
name.color("Red")
name.right(90)
def letter_w():
    for i in range(5):
        name.stamp()
        name.forward(50)
    name.left(150)
    for i in range(3):
        name.forward(50)
        name.stamp()
    name.right(120)
    for i in range(2):
        name.forward(50)
        name.stamp()
    name.left(60)
    name.forward(20)
    name.left(90)
    for i in range(4):
        name.forward(50)
        name.stamp()
letter_w()
    
#Draw letter E
name.color("Orange")
name.right(-90)
name.back(200)
def letter_E():
    for i in range(3):
        name.stamp()
        name.forward(50)
    name.left(90)
    for i in range(4):
        name.stamp()
        name.forward(50)
    name.left(90)
    for i in range(4):
        name.stamp()
        name.forward(50)
    name.left(90)
    name.forward(100)
    name.left(90)
    for i in range(3):
        name.forward(50)
        name.stamp()
letter_E()
name.right(90)
name.forward(100)
name.right(90)
name.forward(150)
name.right(90)

#Draw letter L
name.color("Yellow")
for i in range(4):
    name.stamp()
    name.forward(50)
name.left(90)
for i in range(3):
    name.stamp()
    name.forward(50)
name.left(90)
name.forward(200)
name.left(90)
name.back(100)

#Draw letter C
name.color("Green")
name.stamp()
name.forward(30)
for i in range(4):
    name.circle(130,36)
    name.stamp()
    name.left(10)
name.forward(60)
name.stamp()
name.left(90)
name.forward(180)
name.right(90)
name.forward(170)

#Draw letter O
name.color("Blue")
for i in range(8):
    name.circle(-130, 36)
    name.stamp()
    name.right(10)
name.forward(180)
    
#Draw letter M
name.color("Indigo")
name.forward(140)
name.right(90)
name.forward(200)
name.left(185)
letter_w()
    
#Draw letter E
name.color("Violet")
name.left(90)
name.forward(160)
name.left(90)
name.forward(200)
name.right(90)
name.forward(200)
name.left(180)
letter_E()

name.clear()
name.hideturtle()    
wn.delay(1)
wn.addshape("lion_animatedimg.gif")
wn.addshape("leopard_animatedimg.gif")
wn.addshape("Elephant_animatedimg.gif")
wn.addshape("Buffalo_animatedimg.gif")
wn.addshape("Rhino_animatedimg.gif")
def text():
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.goto(-100,350)
    name.pendown()
    name.write("THESE ARE THE BIG\n"
                 "FIVE ANIMALS IN THE WORLD", font=("Verdana",
                                        15, "normal"))
    name.penup()
    name.goto(-800,300)
    name.write("CLICK L TO SHOW LION\n"
               "CLICK I TO SHOW LEOPARD\n"
               "CLICK E TO SHOW ELEPHANT\n"
               "CLICK B TO SHOW BUFFALO\n"
               "CLICK R TO SHOW RHINO\n", font=("Verdana",
                                            12, "normal"))
def sun():
    sunn = turtle.Turtle()
    sunn.speed(0)
    sunn.color("Yellow")
    sunn.hideturtle()
    sunn.penup()
    sunn.goto(500,250)
    sunn.pendown()
    sunn.fillcolor("Yellow")
    sunn.begin_fill()
    sunn.circle(70)
    sunn.end_fill()
    
def clouds():
    cloud = turtle.Turtle() # Make a background with a clouds
    cloud.speed(0)
    cloud.pensize(5)
    cloud.hideturtle()
    cloud.penup()
    x = random.randrange(-500, 500)
    cloud.goto(x, 200)
    cloud.pendown()
    for i in range(10):
        cloud.circle(20, 180)
        cloud.right(160)
    cloud.right(200)
    cloud.forward(230)
    
def trees():
    """ Draw a tree """
    tree = turtle.Turtle()
    tree.speed(0)
    tree.color("brown")
    tree.pensize(40)
    tree.penup()
    tree.goto(700, -300)
    tree.pendown()
    tree.left(90)
    tree.forward(350)
    tree.right(90)
    tree.color("green")
    tree.pensize(140)
    tree.forward(100)
    for i in range(10):
        tree.circle(20, 180)
        tree.right(160)
    tree.right(200)
    tree.forward(100)
    
def lion1():
    """ Introduce an image of a lion"""
    lion = turtle.Turtle()
    lion.shape("lion_animatedimg.gif")
    lion.penup()
    lion.goto(0,-150)
def leopard1():
    """ Introduce an image of a leopard"""
    leopard = turtle.Turtle()
    leopard.shape("leopard_animatedimg.gif")
    leopard.penup()
    leopard.goto(300,100)
def elephant1():
    """ Introduce an image of an elephant"""
    elephant = turtle.Turtle()
    elephant.shape("Elephant_animatedimg.gif")
    elephant.penup()
    elephant.goto(-300,-100)
    
def buffalo1():
    """ Introduce an image of a buffalo"""
    buffalo = turtle.Turtle()
    buffalo.shape("Buffalo_animatedimg.gif")
    buffalo.penup()
    buffalo.goto(300,-300)
    
def rhino1():
    """ Introduce an image of a rhino"""
    rhino = turtle.Turtle()
    rhino.shape("Rhino_animatedimg.gif")
    rhino.penup()
    rhino.goto(-500,-300)
    
text()
sun()
clouds()
clouds()
clouds()
trees()
wn.onkey(lion1,'l')
wn.onkey(leopard1,'i')
wn.onkey(elephant1,'e')
wn.onkey(buffalo1,'b')
wn.onkey(rhino1,'r')
wn.listen()
    

wn.exitonclick()
