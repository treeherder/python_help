import turtle
class a_turtle(turtle.Turtle):
  def __init__(self, *args,**kwargs):
    super(a_turtle, self).__init__(*args,**kwargs)
    name = input("name this turtle\r\n")
    print(id(self))
  def draw_stats(self, color, size):
    self.pencolor(color)
    self.pensize(size)
    return self.pencolor(), self.pensize()


def move(p, direction, magnitude):
    if direction == "right":
      p.rt(magnitude)
    elif direction == "left":
      p.lt(magnitude)
    elif direction == "forward":
      p.fd(magnitude)
    elif direction == "backward":
      p.bk(magnitude)

title = input("name the world we are in\r\n")

window = turtle.Screen()
t_1 = a_turtle()
window.title(title)
 
