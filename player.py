
from helper_functions import *
import item

import random

class Player:

    def __init__(self, name, player_class):

        self.name = name
        self.player_class = player_class

        HP_MAX = 25
        SP_MAX = 15

        STAMINA = 10

        if player_class == color(5, "MAGE"):
            SP_MAX += 5

        elif player_class == color(9, "WARRIOR"):
            STAMINA += 5

        self.hp = [random.randint(5, HP_MAX), HP_MAX]
        self.sp = [random.randint(5, SP_MAX), SP_MAX]
        
        self.xp = (0, 25)
        self.level = 0

        self.st = (STAMINA, STAMINA)

        self.equipped = None

        self.inventory = [item.Item("Bread")]

    def set_eq_weapon(self, new_item_tuple):
        self.equipped = new_item_tuple

        print("You equip the {}.".format(self.equipped[1].name))

    def get_stats(self):

        print(CLEAR_SCR)

        print(" NAME: \"%s the %s\", LVL: %d" %
            (self.name, self.player_class, self.level))

        print(" HP:   %.2d/%d, XP: %d/%d" %
            (self.hp[0], self.hp[1], self.xp[0], self.xp[1]))

        print(" SP:   %.2d/%d, ST: %d/%d" %
            (self.sp[0], self.sp[1], self.st[0], self.st[1]))

    def get_inventory(self):

        inv = color(4, "INVENTORY")
        inv_len = len(self.inventory)

        if inv_len >= 1:

            return_value = CLEAR_SCR + "\n%s:\n" % inv

            i = 0

            while i < inv_len:

                return_value += ("· [{}] {}\n".format(
                    color(3, str(i)), 
                    self.inventory[i].name
                    )
                )

                i += 1

            return return_value.rstrip("\n")

        else:

            return "\nThere are no items in your %s." % inv
