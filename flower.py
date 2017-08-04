import turtle

def draw_things():
    window = turtle.Screen ()
    window.bgcolor("#0074E7")
    
    brad = turtle.Turtle()

    brad.shape("circle")
    brad.color("#33FCFF")
    brad.speed(100)

    i=0
    while i<34:
        brad.forward(60)
        brad.right(128)
        brad.forward(60)
        brad.left(75)
        i+=1
    brad.color("#0074E7")
    brad.right(130)
    brad.forward(60)
    brad.color("#33FCFF")
 
    j=0
    while j<55:
        brad.left(3.25)
        brad.forward(60)
        brad.right(93.25)
        brad.forward(3)
        brad.right(93.25)
        brad.forward(60)
        j+=1
    brad.left(40)
    brad.forward(180)
    window.exitonclick()

draw_things()
