import pygame

# C
COLOR_L_BLUE = (102, 130, 219)
COLOR_WHITE = (255, 255, 255)
COLOR_YELLOW = (255, 234, 77)

# E

EVENT_ENEMY = pygame.USEREVENT + 1

ENTITY_SPEED = {
    'lvl1-0': 0,
    'lvl1-1': 1,
    'lvl1-2': 2,
    'lvl1-3': 3,
    'player': 3,
    'enemy': 3
}

# M
MENU_OPTION = ('START',
               'SCORE',
               'EXIT')

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# s

SPAWN_TIME = {'enemy': 2000,
}