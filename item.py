
from helper_functions import *
import json

with open("MINVENTORY.json") as file:

    MASTER_INVENTORY = json.load(file)

    w0 = MASTER_INVENTORY["BASIC Weak-Wand"]
    w1 = MASTER_INVENTORY["BASIC Short-Sword"]

    w0["desc"] = w0["desc"] % color(5, "MAGE")
    w1["desc"] = w1["desc"] % color(9, "WARRIOR")

class Item:

    classno = 0

    def __init__(self, name):

        Item.classno += 1

        try:
            self.type = MASTER_INVENTORY[name]["type"]
        except KeyError:
            raise SyntaxError("Invalid name of Item '%s' given to Item #%d" % (name, Item.classno))

        self.name = name
        self.description = MASTER_INVENTORY[name]["desc"]

        if self.type == "FOOD":

            # this is the amount of health gained from EATing it.
            self.hp_gain = MASTER_INVENTORY[name]["rehp"]


def food_item_handle(item_obj, player_inst):
    #deal with food items

    local_hp_gain = item_obj.hp_gain

    food_choice = input("Do you want to %s this, or %s?\n-> " %
        (color(2, "EAT"), color(1, "EXIT"))).upper()

    if food_choice == "EAT":

        if (player_inst.hp[0] + local_hp_gain) > player_inst.hp[1]:
            player_inst.hp[0] = player_inst.hp[1]

        else:
            player_inst.hp[0] += local_hp_gain

        return 0

    elif food_choice == "EXIT":
        return -1

def weapon_item_handle(item_index, player_inst):

    weapon_equipped = (player_inst.equipped[0], player_inst.equipped[1].name)

    weapon_in_inv = player_inst.inventory[weapon_equipped[0]].name

    if weapon_equipped[0] == item_index and weapon_equipped[1] == weapon_in_inv:
        print("This WEAPON is equipped.")

    else:
        print("This WEAPON is not equipped.")

def do_something_with_item(item_index, player_inst):

    item_obj = player_inst.inventory[item_index]

    if item_obj.type == "FOOD": #deal with food items being used
        ret_val = food_item_handle(item_obj, player_inst)

        if ret_val == 0:
            del player_inst.inventory[item_index]
            print("You consume the item.")

    elif item_obj.type == "WEAPON": #deal with weapon items being used
        weapon_item_handle(item_index, player_inst)

    else:
        print("Invalid type for item given.\n<do_something_with_item>")
        return 0
