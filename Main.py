import pgzrun
import random

FONT_OPTION = (255,255,255)

WIDTH = 800
HEIGHT = 600

CENTER = (400,300)
FINAL_LEVEL = 6
START_SPEED = 10
ITEMS = ["bag", "bottle", "chips", "battery"]

game_over = False
game_complete = False
current_level = 1
items = []
animations = []


def draw():
    global game_over, game_complete, current_level, items, animations
    screen.clear()
    screen.blit("backgroundimg", (0,0))

    if game_over:
        display_message("GAMEOVER, TRY AGAIN")
    elif game_complete:
        display_message("YOU WON")
    else: 
        for i in items:
            i.draw()


def display_message():
    pass
def update():
    global game_over, game_complete, current_level, items, animations
    if len(items) == 0:
        items = make_items(current_level)

def make_items(extraitems):
    items_to_create = get_option_to_create(extraitems)
    new_items = create_item(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

def get_option_to_create(numextraitems):
    items_to_create = ["paper"]
    for i in numextraitems:
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

def create_item():
    global items_to_create
    new_items = []
    for i in items_to_create:
        items = Actor(i + "img")
        new_items.append(items)
    return new_items

       


def layout_items():
    pass

def animate_items():
    pass





pgzrun.go()