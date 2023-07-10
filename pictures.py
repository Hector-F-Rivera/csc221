from gasp import *
begin_graphics()
Line((266, 194), (364, 194))
Circle((320,240), 220)
Line((266, 194), (320,286))
for r in 239,401:
    Circle((r, 286), 28)
Arc((320, 240), 150, 280, 320)
for r in 239, 401:
    Arc((r,286,),40,25,155)
def moan():
    print("Python is useless")
    print("And so are these worksheets.")
moan()
def Square(x):
    print(x, 'times', x, 'is', x * x)
Square(3)
update_when('key_pressed')
end_graphics()