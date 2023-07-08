from gasp import *
begin_graphics()
Line((290, 190), (310, 190))
Circle((300, 200), 40)
Line((290, 190), (300,210))
for r in 285,315:
    Circle((r, 210), 5)
Arc((300, 200), 30, 280, 320)
update_when('key_pressed')
end_graphics()