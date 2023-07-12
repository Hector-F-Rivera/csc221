from gasp import *
def faced(x,y):
    begin_graphics()
    Line((x-54, y-46), (x+54, y-46))
    Circle((x,y), 220)
    Line((x-54, y-46), (x,y+46))
    def eyed(x,y):
        for e in x-81,x+81:
            Line((e-7, y-6), (e+7, y-6))
            Circle((e,y), 28)
            Line((e-7, y-6), (e,y+6))
            for r in e-10,e+10:
                Circle((r, y+3), 3)
            Arc((e, y), 19, 280, 320)
            for r in e-10, e+10:
                Arc((r,y+6,),5,25,155)
    eyed(x,y+46)
    Arc((x, y), 150, 280, 320)
    for r in x-81, x+81:
        Arc((r,y+46,),40,25,155)
q = "Enter the X value."
x = int(input(q))
qt = "Enter the y value"
y = int(input(q))
faced(x,y)
faced(x+440,y)
faced(x-440,y)
def moan():
    print("Python is useless")
    print("And so are these worksheets.")
moan()
def Square(x):
    print(x, 'times', x, 'is', x * x)
Square(3)
update_when('key_pressed')
end_graphics()