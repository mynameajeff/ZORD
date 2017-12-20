
from helper_functions import *
from item_handlers import *
import json

with open("MINVENTORY.json") as file:

    MASTER_INVENTORY = json.load(file)

    w0 = MASTER_INVENTORY["BASIC Weak-Wand"]
    w1 = MASTER_INVENTORY["BASIC Short-Sword"]

    w0["desc"] = w0["desc"].format(color(5, "MAGE"))
    w1["desc"] = w1["desc"].format(color(9, "WARRIOR"))

class Item:

    classno = 0

    def __init__(self, name):

        Item.classno += 1

        try:
            self.type = MASTER_INVENTORY[name]["type"].upper()
        except KeyError:
            raise SyntaxError("Invalid name of Item '%s' given to Item #%d" % (name, Item.classno))

        self.name = name
        self.description = MASTER_INVENTORY[name]["desc"]

        if self.type == "FOOD":

            # this is the amount of health gained from EATing it.
            self.hp_gain = MASTER_INVENTORY[name]["hp-gained"]

            self.item_stats = "\n\t+{} HP.".format(MASTER_INVENTORY[name]["hp-gained"])

        elif self.type == "WEAPON":

            stats = MASTER_INVENTORY[name]["stats"]

            self.item_stats = "\n\tNORMAL DMG: {},   CRIT DMG: {} \
                    \n\tHIT CHANCE: {}%, CRIT CHANCE: {}% \
                    \n\tRANGE: {}".format(

                stats["damage-normal"],
                stats["damage-crit"],
                stats["hit-chance"],
                stats["crit-chance"],
                stats["attack-range"],
            )
