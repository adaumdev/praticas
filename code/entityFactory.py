#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.player import Player
from code.enemy import Enemy
from code.item import Item


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0,0)):
        match entity_name:
            case 'lvl1-':
                list_bg = []
                for i in range(4):
                    list_bg.append(Background(f'lvl1-{i}', (0,0)))
                    list_bg.append(Background(f'lvl1-{i}', (WIN_WIDTH, 0)))
                return list_bg
            case 'player':
                return Player('player', (10, WIN_HEIGHT / 2))
            case 'enemy':
                return Enemy('enemy', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))
            case 'item':
                return Item('item', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40)))