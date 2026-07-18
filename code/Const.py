import pygame

# C
COLOR_L_BLUE = (102, 130, 219)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 234, 77)
COLOR_PURPLE = (110, 3, 199)

# E

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_ITEM = pygame.USEREVENT
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'lvl1-0': 0,
    'lvl1-1': 1,
    'lvl1-2': 2,
    'lvl1-3': 3,
    'lvl2-0': 0,
    'lvl2-1': 1,
    'lvl2-2': 2,
    'lvl2-3': 3,
    'player': 3,
    'enemy': 3,
    'item': 1
}

ENTITY_HEALTH = {
    'lvl1-0': 999,
    'lvl1-1': 999,
    'lvl1-2': 999,
    'lvl1-3': 999,
    'lvl2-0': 999,
    'lvl2-1': 999,
    'lvl2-2': 999,
    'lvl2-3': 999,
    'player': 200,
    'enemy': 100,
    'item': 1
}

ENTITY_DAMAGE = {
    'lvl1-0': 0,
    'lvl1-1': 0,
    'lvl1-2': 0,
    'lvl1-3': 0,
    'lvl2-0': 0,
    'lvl2-1': 0,
    'lvl2-2': 0,
    'lvl2-3': 0,
    'player': 1,
    'enemy': 20,
    'item': 0
}

ENTITY_SCORE = {
    'lvl1-0': 0,
    'lvl1-1': 0,
    'lvl1-2': 0,
    'lvl1-3': 0,
    'lvl2-0': 0,
    'lvl2-1': 0,
    'lvl2-2': 0,
    'lvl2-3': 0,
    'player': 0,
    'enemy': 0,
    'item': 1
}


# M
MENU_OPTION = ('START',
               'SCORE',
               'EXIT')


# s

SPAWN_TIME = {'enemy': 1000,
              'item': 3000
}

# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 20000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324