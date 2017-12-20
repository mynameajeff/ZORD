
from helper_functions import *
import player, item

def get_character():

    getting_name = True

    while getting_name:

        name = input("\nWhat's your name? (MAX 20 CHARACTERS)\n> ")

        if 20 < len(name) or len(name) == 0:
            print("Invalid name.")

        else:
            getting_name = False

    getting_class = True

    while getting_class:

        pclass = input("\nDo you wish to be a {}, or a {}?\n> "
            .format(color(5, "MAGE"), color(9, "WARRIOR"))).upper()

        if pclass in ("MAGE", "WARRIOR"):

            if pclass == "MAGE":
                color_num = 5
                default_weapon = "BASIC Weak-Wand"

            elif pclass == "WARRIOR":
                color_num = 9
                default_weapon = "BASIC Short-Sword"

            playerc_retval = player.Player(name, color(color_num, pclass))

            playerc_retval.inventory.insert(0, item.Item(default_weapon))
            playerc_retval.inventory.insert(1, item.Item("BASIC Short-Sword")) #just for testing purposes.

            playerc_retval.equipped = (0, playerc_retval.inventory[0]) #(index, item)

            getting_class = False

        else:
            print("Invalid class name.")

    return playerc_retval
