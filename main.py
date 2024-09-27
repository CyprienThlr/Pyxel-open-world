import pyxel

# Window initialization
pyxel.init(128, 128, title="Open World")

# Texture loading
pyxel.load("texture.pyxres")

# Player informations
player_x = 60
player_y = 60
player_speed = 1

# Running
run = True

# Open world gestion
# Default map coordinates
map_x = 40
map_y = 40


def update():
    global map_x, map_y

    if run:
        
        if pyxel.btn(pyxel.KEY_UP):
            if map_y > 0:
                map_y -= player_speed

        if pyxel.btn(pyxel.KEY_DOWN):
            if map_y < 255:
                map_y += player_speed

        if pyxel.btn(pyxel.KEY_LEFT):
            if map_x > 0:
                map_x -= player_speed

        if pyxel.btn(pyxel.KEY_RIGHT):
            if map_x < 255:
                map_x += player_speed

def draw():
    global map_x, map_y

    pyxel.cls(0)
    
    if run:

        pyxel.mouse(False)

        # Map drawing
        pyxel.blt(0, 0, 2, map_x, map_y, 128, 128)
        
        # Player drawing
        pyxel.blt(player_x, player_y, 0, 8, 0, 8, 8, 5)

# Running
pyxel.run(update, draw)