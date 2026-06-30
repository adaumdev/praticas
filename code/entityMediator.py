from code.entity import Entity
from code.enemy import Enemy
from code.player import Player
from code.item import Item

class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Enemy):
            if ent.rect.right < 0:
                ent.health = 0
        pass


    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i+1, len(entity_list)):
                entity2 = entity_list[j]
                EntityMediator.__verify_collision_entity(entity1, entity2)

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                    if isinstance(ent, Item):
                        EntityMediator.__give_score(ent, entity_list)
                    entity_list.remove(ent)

    @staticmethod
    def __verify_collision_entity(ent1, ent2):
        valid_interaction = False
        if isinstance(ent1, Enemy) and isinstance(ent2, Player):
            valid_interaction = True
        if isinstance(ent1, Player) and isinstance(ent2, Enemy):
            valid_interaction = True
        if isinstance(ent1, Item) and isinstance(ent2, Player):
            valid_interaction = True
        if isinstance(ent1, Player) and isinstance(ent2, Item):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                ent1.health -= ent2.damage
                ent2.health -= ent1.damage
                ent1.last_dmg = ent2.name
                ent2.last_dmg = ent1.name

    @staticmethod
    def __give_score(item: Item, entity_list: list[Entity]):
        if item.last_dmg == 'player':
            for ent in entity_list:
                if ent.name == 'player':
                    ent.score += item.score