#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

from pygame import Surface, Rect
from pygame.font import Font
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.Const import COLOR_PURPLE, COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, EVENT_ITEM, SPAWN_TIME, EVENT_TIMEOUT, TIMEOUT_STEP, TIMEOUT_LEVEL
from code.entityMediator import EntityMediator
from code.player import Player

class Level:
    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name))
        player = EntityFactory.get_entity('player')
        player.score = player_score[0]
        self.entity_list.append(player)
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME['enemy'])
        pygame.time.set_timer(EVENT_ITEM, SPAWN_TIME['item'])
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                
                if ent.name == 'player':
                    self.level_text(14, f'Player - Health: {ent.health} | Score: {ent.score}' , COLOR_PURPLE, (10, 25))


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    self.entity_list.append(EntityFactory.get_entity('enemy'))
                if event.type == EVENT_ITEM:
                    self.entity_list.append(EntityFactory.get_entity('item'))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'player':
                                player_score[0] = ent.score
                        return True
                    
                found_player = False 
                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False
                
            # printed text
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', COLOR_WHITE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)


    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)