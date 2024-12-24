donje_x, donje_y = list(map(int, input().split(' ')))
gornje_x, gornje_y = list(map(int, input().split(' ')))

robot_x, robot_y = list(map(int, input().split(' ')))
punjac_x, punjac_y = list(map(int, input().split(' ')))

gore_dole_robot = 'sredina'
gore_dole_punjac = 'sredina'

levo_desno_robot = 'sredina'
levo_desno_punjac = 'sredina'

polovina_levo_desno = (gornje_x - donje_x) / 2
polovina_gore_dole = (gornje_y - donje_y) / 2

if gore_dole_robot > polovina_gore_dole:
    gore_dole_robot = 'gore'

elif gore_dole_robot < polovina_gore_dole:
    gore_dole_robot = 'dole'

if levo_desno_robot < polovina_levo_desno:
    gore_dole_robot = 'levo'

elif levo_desno_robot > polovina_levo_desno:
    gore_dole_robot = 'desno'


if gore_dole_punjac > polovina_gore_dole:
    gore_dole_robot = 'gore'

elif gore_dole_punjac < polovina_gore_dole:
    gore_dole_punjac = 'dole'

if levo_desno_punjac < polovina_levo_desno:
    levo_desno_punjac = 'levo'

elif levo_desno_punjac > polovina_levo_desno:
    levo_desno_punjac = 'desno'

pravac_gore_dole = 'levo'
pravac_levo_desno = 'gore'

if punjac_x > robot_x:
    pravac_levo_desno = 'desno'

if punjac_y < robot_y:
    pravac_gore_dole = 'dole'
