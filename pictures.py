from gasp import *
begin_graphics()
Line((1160, 760), (1240, 760))
Circle((1200, 800), 160)
Line((1160, 760), (1240,840))
for r in 1140,1260:
    Circle((r, 840), 20)
Arc((1200, 800), 120, 1120, 1280)
update_when('key_pressed')
end_graphics()