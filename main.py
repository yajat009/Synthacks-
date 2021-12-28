import turtle
from turtle import *


type = input("What Kind of Card Would You Like?:\n Type c for Christmas \n Type b for Birthday\n") 

if type == "b": 
  base = input("What would you like for your base picture? \n Type c for a Cake \n Type p for Presents \n")
  if base == "c":
    #cake
    myPen = Turtle()
    myPen.shape("turtle")
    myPen.tracer(0)
    myPen.speed(0)
    myPen.hideturtle() 
    window = turtle.Screen()
    window.bgcolor("#69D9FF")
    y = -140

    #Inititalise the dictionary
    ingredients = {}
    #Add items to the dictionary
    ingredients["vanilla"]="#f3e5ab"
    ingredients["pistachio"]="#7DFA7F"
    ingredients["raspberry"]="#e30b5d"
    ingredients["strawberry"]="#FF0D0D"
    ingredients["cherry"]="#C20067"
    ingredients["apricot"]="#FFB300"
    ingredients["lemon"]="#FFFA5C"
    ingredients["kiwi"]="#67F55F"
    ingredients["pineapple"]="#FFFF17"
    ingredients["mango"]="#FFE838"
    ingredients["mint"]="#5FF5A0"
    ingredients["white chocolate"]="#FFFDC4"
    ingredients["milk chocolate"]="#BF671F"
    ingredients["dark chocolate"]="#2A1506"
    ingredients["coffee"]="#d2691e"
    ingredients["toffee"]="#E35209"
    ingredients["mocha"]="#93c572"
    ingredients["icing sugar"]="#FFFFFF"

    #Initialise the list of layers
    layers = []
    #Add values to the list
    layers.append(["raspberry",30])
    layers.append(["dark chocolate",20])
    layers.append(["milk chocolate",40])
    layers.append(["mango",60])
    #Add more layers...


    #Preview the content of the list
    print(layers)
    ### Now let's preview the layer cake

    #let's draw the plate
    draw_rectangle(turtle, "white", -150, y-10, +300, 10)


    #Iterate through each layer of the list
    for layer in layers:
      draw_rectangle(myPen, ingredients[layer[0]], -120, y, 240, layer[1])
      y+=layer[1]

    addIcing(myPen, ingredients["icing sugar"],y)
    addCherry(myPen, ingredients["cherry"], 0, y+10, 15)

    myPen.getscreen().update()

  elif base == "p":
    #presents
    speed(0)
    # Background
    penup()
    goto(0, -300)
    pendown()
    color("forestgreen")
    begin_fill()
    circle(300)
    end_fill()
    # Lid on gift
    penup()
    goto(-180, 20)
    pendown()
    color("darkred")
    begin_fill()
    for i in range(2):
      forward(360)
      left(90)
      forward(60)
      left(90)
    end_fill()
    # Bottom of gift
    penup()
    goto(-160, 0)
    pendown()
    begin_fill()
    for i in range(2):
      forward(320)
      right(90)
      forward(210)
      right(90)
    end_fill()
    # Green line through middle of gift
    penup()
    goto(-10, 80)
    pendown()
    color("forestgreen")
    begin_fill()
    for i in range(2):
      forward(20)
      right(90)
      forward(290)
      right(90)
    end_fill()
    # Right ribbon
    penup()
    goto(10, 100)
    pendown()
    pensize(10)
    color("darkred")
    for i in range(90):
      forward(1)
      left(0.4)
    for i in range(90):
      forward(1)
      left(2)
    for i in range(90):
      forward(1)
      left(0.4)
    # Left ribbon
    penup()
    goto(-10, 100)
    pendown()
    right(70)
    for i in range(90):
      forward(1)
      right(0.4)
    for i in range(90):
      forward(1)
      right(2)
    for i in range(90):
      forward(1)
      right(0.4)
elif type == "c": 
  base = input("What would you like for your base picture? \n Type w for a Decorated Wreath \n Type o for Christmas Ornaments \n Type t for a Christmas Tree \n")
  if base == "w":
    #wreath
    speed(0)
    bgcolor("black")
    pensize(2)
    penup()
    goto(0, -100)
    pendown()
    
    for i in range(13):
      for colours in ["forestgreen", "darkgreen", "limegreen"]:
          color(colours)
          circle(150)
          left(10)
          forward(20)
    
    # Ribbon bow
    penup()
    goto(-95, 110)
    pendown()
    color("darkred", "red")
    begin_fill()
    forward(200)
    right(120)
    forward(100)
    right(120)
    forward(200)
    left(120)
    forward(100)
    end_fill()
    # Circle in ribbon
    penup()
    goto(-40, 160)
    pendown()
    begin_fill()
    circle(30)
    end_fill()
    # Left dangly bit in ribbon
    penup()
    goto(-25, 132)
    pendown()
    begin_fill()
    right(20)
    forward(130)
    left(80)
    forward(60)
    left(118)
    forward(150)
    end_fill()
    # Right dangly bit of ribbon
    begin_fill()
    right(92)
    forward(5)
    right(80)
    forward(150)
    left(110)
    forward(60)
    left(89)
    forward(139)
    end_fill()
    # Yellow Decoration 1
    penup()
    goto(-150, 20)
    pendown()
    color("gold", "yellow")
    begin_fill()
    circle(10)
    end_fill()
    # Yellow Decoration 2
    penup()
    goto(140, -50)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    # Yellow Decoration 3
    penup()
    goto(-30, -130)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    # Yellow Decoration 4
    penup()
    goto(120, 110)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    # Red Decoration 1
    penup()
    goto(140, 40)
    pendown()
    color("darkred", "red")
    begin_fill()
    circle(10)
    end_fill()
    # Red Decoration 2
    penup()
    goto(-120, -80)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    # Red Decoration 3
    penup()
    goto(60, -120)
    pendown()
    begin_fill()
    circle(10)
    end_fill()
    # Red Decoration 4
    penup()
    goto(-135, 110)
    pendown()
    begin_fill()
    circle(10)
    end_fill()

  elif base == "o": 
    #ornaments
    speed(0)
    # Background
    bgcolor("indigo")
    # Chain
    penup()
    goto(0, 250)
    pendown()
    color("darkkhaki")
    pensize(10)
    right(90)
    forward(100)
    # Attachment
    pensize(1)
    right(90)
    back(20)
    begin_fill()
    for i in range(2):
        forward(40)
        left(90)
        forward(10)
        left(90)
    end_fill()
    # Red bauble
    penup()
    goto(0, 140)
    pendown()
    color("crimson")
    begin_fill()
    circle(200)
    end_fill()
    # Gold zigzag
    penup()
    goto(176, 30)
    pendown()
    color("gold")
    pensize(3)
    left(45)
    for i in range(5):
        forward(50)
        right(90)
        forward(50)
        left(90)
    # Green circles
    penup()
    goto(-160, -65)
    pendown()
    color("limegreen")
    left(135)
    begin_fill()
    for i in range(5):
        circle(10)
        penup()
        forward(80)
        pendown()
    end_fill()
    # Gold zigzag 2
    penup()
    goto(-185, -135)
    pendown()
    color("gold")
    left(45)
    for i in range(5):
        forward(50)
        right(90)
        forward(50)
        left(90)
    forward(35)    
    # Stars at top
    penup()
    goto(-105, 80)
    pendown()
    pensize(1)
    color("aliceblue")
    setheading(0)
    for i in range(3):
        begin_fill()
        for i in range(5):
            forward(30)
            right(144)
        end_fill()
        penup()
        forward(90)
        pendown()
    # Stars at bottom
    penup()
    goto(-105, -180)
    pendown()
    setheading(0)
    for i in range(3):
        begin_fill()
        for i in range(5):
            forward(30)
            right(144)
        end_fill()
        penup()
        forward(90)
        pendown()

  elif base == "t": 
    #christmastree
    n = 50
    speed("fastest")
    left(90)
    forward(3*n)
    color("orange", "yellow")
    begin_fill()
    left(126)
    for i in range(5):
      forward(n/5)
      right(144)
      forward(n/5)
      left(72)
    end_fill()
    right(126)
    color("dark green")
    backward(n*4.8)
    def tree(d, s):
      if d <= 0: return
      forward(s)
      tree(d-1, s*.8)
      right(120)
      tree(d-3, s*.5)
      right(120)
      tree(d-3, s*.5)
      right(120)
      backward(s)
    tree(15, n)
    backward(n/2)
    import time
    time.sleep(60)

  else: 
    print("please enter valid letter")
  
tline = input("What message would you like at the top of the card?")
mline = input("What message would you like on the bottom of the card?")

penup()
goto(0, 208)
pendown()
color("red")
write(tline, font=("Impact", 24, "bold"), align = "center")
penup()
goto(0, -212)
pendown()
color("forestgreen") 
write(mline,font=("Impact", 24, "bold"), align = "center")

hideturtle()


