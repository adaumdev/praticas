#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu, MENU_OPTION
from code.level import Level

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size = (WIN_WIDTH, WIN_HEIGHT))


    def run(self):

        while True:

            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0]]:
               level = Level(self.window, 'Level1', menu_return)
               level_return = level.run()
            
            elif menu_return == MENU_OPTION[2]:
                pygame.quit() #Close window
                quit() #end Python
            else: 
                pygame.quit()
                sys.exit()

