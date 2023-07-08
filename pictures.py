from gasp import *
begin_graphics()
Line((266, 194), (364, 194))
Circle((320,240), 220)
Line((266, 194), (320,286))
for r in 239,401:
    Circle((r, 286), 28)
Arc((300, 200), 30, 280, 320)
update_when('key_pressed')
end_graphics()