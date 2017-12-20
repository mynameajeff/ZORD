
from helper_functions import *

def food_item_handle(item_obj, player_inst):

    print(item_obj.item_stats)

    local_hp_gain = item_obj.hp_gain

    food_choice = input("Do you want to {} this, or {}?\n-> "
        .format(color(2, "EAT"), color(1, "EXIT"))).upper()

    if food_choice == "EAT":

        if (player_inst.hp[0] + local_hp_gain) > player_inst.hp[1]:

            player_inst.hp[0] = player_inst.hp[1]

        else:
            player_inst.hp[0] += local_hp_gain

        return 0

    elif food_choice == "EXIT":
        return -1

def weapon_item_handle(item_index, item_obj, player_inst):

    print(item_obj.item_stats)

    weapon_in_inv = player_inst.inventory[player_inst.equipped[0]].name

    tstr = "\nThis WEAPON is"

    al = [
        (player_inst.equipped[0]      != item_index), 
        (player_inst.equipped[1].name != weapon_in_inv)
    ]

    if al[0] or al[1]:
        tstr += " not"
        not_equipped = True
    else:
        not_equipped = False

    print(tstr, "equipped.")

    if not_equipped:

        weapon_choice = input("Do you want to {} this, {} it, or {}?\n-> "
            .format(color(3, "EQUIP"), color(2, "DROP"), color(1, "EXIT"))).upper()

        if weapon_choice == "EQUIP":
            player_inst.set_eq_weapon((item_index, item_obj))

        elif weapon_choice == "DROP":
            return 0

        elif weapon_choice == "EXIT":
            return -1

def do_something_with_item(item_index, player_inst):

    item_obj = player_inst.inventory[item_index]

    if item_obj.type == "FOOD": #deal with food items being used
        ret_val = food_item_handle(item_obj, player_inst)

        if ret_val == 0:
            print("You consume the {}.".format(
                player_inst.inventory[item_index].name))

            del player_inst.inventory[item_index]

    elif item_obj.type == "WEAPON": #deal with weapon items being used
        ret_val = weapon_item_handle(item_index, item_obj, player_inst)

        if ret_val == 0:
            print("You drop the {}.".format(
                player_inst.inventory[item_index].name))

            del player_inst.inventory[item_index]

    else:
        print("Invalid type for item given.\n<do_something_with_item>")
        return 0

