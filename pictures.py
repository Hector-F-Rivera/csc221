from gasp import *
def faced(x,y):
    begin_graphics()
    Line((x-54, y-46), (x+54, y-46))
    Circle((x,y), 220)
    Line((x-54, y-46), (x,y+46))
    for r in x-81,x+81:
        Circle((r, y+46), 28)
    Arc((x, y), 150, 280, 320)
    for r in x-81, x+81:
        Arc((r,y+46,),40,25,155)
q = "Enter the X value."
x = int(input(q))
qt = "Enter the y value"
y = int(input(q))
faced(x,y)
def moan():
    print("Python is useless")
    print("And so are these worksheets.")
moan()
def Square(x):
    print(x, 'times', x, 'is', x * x)
Square(3)
update_when('key_pressed')
end_graphics()