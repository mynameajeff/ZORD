
from helper_functions import *
import char_creation, item

import sys

def check_choice_wl(player_inst):

    print(player_inst.get_inventory())

    text = "\nEnter the number of the item you wish to interact with, \
            \nOr you could type %s to exit the inventory." % color(1, "EXIT")

    print(text, end = "")

    interacting_w_inventory = True

    while interacting_w_inventory:

        check_choice = input("\n> ").upper()

        if check_choice == "EXIT":

            interacting_w_inventory = False

        elif check_choice.isdigit():

            cc_num = int(check_choice)
            
            if -1 < cc_num < len(player_inst.inventory):

                print("\n%s" % player_inst.inventory[cc_num].description, end = "")
                cont = item.do_something_with_item(cc_num, player_inst)

                if cont == -1:
                    interacting_w_inventory = False

                else:
                    print(text, end = "")

            else:
                print("Invalid.")

        else:
            print("Invalid.")


def wloop_1():

    player_instance = char_creation.get_character()

    while True:

        player_instance.get_stats()

        print("\nDo you want to %s for supplies, %s monsters, %s around you, or %s your inventory?" %
            (color(2, "SCAVENGE"), color(1, "HUNT"), color(3, "LOOK"), color(4, "CHECK")), end = "")

        choice_1 = input("\n> ").upper()

        if choice_1 == "SCAVENGE":
            pass

        elif choice_1 == "HUNT":
            pass

        elif choice_1 == "LOOK":
            pass

        elif choice_1 == "CHECK":
            
            check_choice_wl(player_instance)

        elif choice_1 == "EXIT":
            break


def wloop_0():

    while True:

        choice_0 = input("\n> ")

        if choice_0 == '1':
            break

        elif choice_0 == '2':
            print("This game was designed by %s.\n" % color(3, "mynameajeff"))

            print("%s is %sealth %soints. When these reach Zero, you lose the game." % 
                (color(2, "HP"), color(2, "H"), color(2, "P")))

            print("%s is e%sperience %soints. These allow you to level up and become stronger." % 
                (color(1, "XP"), color(1, "X"), color(1, "P")))

            print("%s is %special %soints. These are used to perform magick." %
                (color(4, "SP"), color(4, "S"), color(4, "P")))

            print("%s is %samina %soints. These are used to run away from enemies, and attack harder." %
                (color(6, "ST"), color(6, "ST"), color(6, "P")))

        elif choice_0 == '3':
            print("leaving...\n")
            sys.exit()

        else:
            print("incorrect choice.")


def create_screen():
    print("\nWelcome to the %s RPG!\n" % 
        (color(5, "Z") + color(135, "0") + color(141, "R") + color(147, "D")))

    i = 0

    for item in ["play", "information about", "exit"]:

        print("[%s] %s the game" % (color(3, str(i + 1)), item))

        i += 1
