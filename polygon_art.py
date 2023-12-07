import turtle
import random

class Polygon:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        self.num_sides = 0
        self.color = ()
        self.size = 0
        self.orientation = 0
        self.location = []
        self.border_size = 0
    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()

    def run(self, user_int):
        for i in range(30):
            if user_int == 4:
              self.num_sides = random.randint(3, 5)
            else:
              self.num_sides = user_int%4 + 2

            check = False
            if user_int > 4 and user_int != 8:
                check = True

            if user_int == 8:
                self.num_sides = random.randint(3, 5)
                check = True

            self.get_size()
            self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
            self.get_new_orientation()
            self.new_location()
            self.new_border()
            self.draw_polygon()
            # specify a reduction ratio to draw a smaller polygon inside the one above
            reduction_ratio = 0.618

            # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.left(90)
            turtle.forward(self.size * (1 - reduction_ratio) / 2)
            turtle.right(90)
            self.location[0] = turtle.pos()[0]
            self.location[1] = turtle.pos()[1]

            # adjust the size according to the reduction ratio
            self.size *= reduction_ratio

            # draw the second polygon embedded inside the original
            if check:
               self.draw_polygon()
               turtle.penup()
               turtle.forward(self.size * (1 - reduction_ratio) / 2)
               turtle.left(90)
               turtle.forward(self.size * (1 - reduction_ratio) / 2)
               turtle.right(90)
               self.location[0] = turtle.pos()[0]
               self.location[1] = turtle.pos()[1]

               # adjust the size according to the reduction ratio
               self.size *= reduction_ratio
               self.draw_polygon()
    def get_size(self):
        self.size = random.randint(50, 150)

    def get_new_orientation(self):
        self.orientation =  random.randint(0, 90)

    def new_location(self):
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]

    def new_border(self):
        self.border_size = random.randint(1, 10)


user_input = int(input("Which art do you want to generate? Enter a number between 1 to 8,inclusive "))

polygon = Polygon()
polygon.run(user_input)
# hold the window; close it by clicking the window close 'x' mark
turtle.done()