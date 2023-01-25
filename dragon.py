import turtle
t = turtle.Turtle()
t.color("Black", "orange")

s = turtle.Screen()
t.speed(10)

t.begin_fill()

t.right(30)
t.forward(100)
t.right(150)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90) 
t.forward(150)

t.end_fill()
# This make the head.

t.begin_fill()

t.right(180)
t.forward(150)
t.left(90)
t.forward(10)
t.right(90)
t.forward(300)
t.left(90)
t.forward(80)
t.left(90)
t.forward(300)
t.left(90)
t.forward(85)

t.end_fill()
# This make the body.

t.begin_fill()

t.color("black", "black")
t.right(90)
t.right(30)
t.forward(40)
t.left(30)
t.backward(30)
t.left(90)
t.forward(20)

t.end_fill()
# This makes the eye.

t.begin_fill()

t.color("black", "blue")
t.left(90)
t.forward(10)
t.left(90)
t.forward(5)
t.right(180)
t.left(45)
t.forward(90)
t.left(90)
t.forward(90)
t.right(90)
t.forward(90)
t.left(90)
t.forward(90)
t.right(90)
t.forward(30)
t.left(90)
t.forward(30)
t.left(135)
t.forward(310)
t.left(90)
t.forward(10)
t.end_fill()
t.left(90)
t.forward(10)
t.left(90)
t.forward(90)
# This make the spikes.
t.begin_fill()


t.color("pink", "pink")
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(180)
t.forward(150)
for x in "aaaaaaaaaaaaaaa":
    t.left(90)
    t.forward(20)   
    t.right(90)
    t.forward(5)
    t.right(90)
    t.forward(20)
    t.left(90)
    t.forward(5)
t.end_fill()    
# This make the feet.

s.exitonclick()

