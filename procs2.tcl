
#this procedure allows you to interact with the food item selected.
proc type_is_food? {} {

    global player

    puts -nonewline "Do you want to [color 2 EAT] this, or [color 1 EXIT]?\n> "
    gets stdin player(choice3)

    set player(choice3) [string toupper $player(choice3)]

    if {[string compare $player(choice3) EAT] == 0} {
        
        if {[expr $player(hp) + 10] > $player(hp_max)} {
        
            set player(hp) $player(hp_max)
        
        } else {
        
            set player(hp) [expr $player(hp) + 10]
        
        }
        
        return 0

    } elseif {[string compare $player(choice3) EXIT] == 0} {
        return -1
    }

}

proc type_is_weapon? {index} {

    global player

    # this contains the index of the item "equipped"
    set item_index_eq [lindex $player(equipped?) 0]

    # this contains the name of the item "equipped"
    set item_name_eq  [lindex $player(equipped?) 1]

    # this contains the name of the item in the inventory
    set weapon_name [lindex $player(inv) $index]
    
    # this tests to see if the equipped item matches up with the selected item.
    if {$item_index_eq == $index && $item_name_eq == $weapon_name} {

        puts "This WEAPON is equipped." ;# {they match up.}

    } else {

        puts "This WEAPON is not equipped.";# {they do not match up.}
    }


    return -1
}

# this procedure is the bridge between the functionality of the items and the player.
proc do_something_with_item? {item} {

    global player
    global master_inv_type

    set item_name [lindex $player(inv) $item] ;# item is the index of the item selected.

    set item_loop_broken 0

    if {[dict exists $master_inv_type $item_name]} {

        set TYPE [dict get $master_inv_type $item_name]

        while {!$item_loop_broken} {

            # TYPE is the type of the item selected.
            switch $TYPE {

                FOOD {

                    set ret_val [type_is_food?]

                    if {$ret_val == 0} {
                        set player(inv) [lreplace $player(inv) $item $item]
                    }

                    puts "You consume the $item_name."

                    return ret_val

                }

                WEAPON {

                    set ret_val [type_is_weapon? $item]

                    if {$ret_val == 0} {
                        set player(inv) [lreplace $player(inv) $item $item]
                    }

                    return ret_val

                }

                default {

                    puts "invalid type for item given.\n<do_something_with_item?>"

                }


            }

        }


    }
}

# allows player to select an item.
proc check_choice {} {

    global player
    global master_inv

    puts [get_inventory]

    puts -nonewline "\nEnter the number of the item you with to interact with,\n"
    puts -nonewline "Or you could type [color 1 EXIT] to exit the [color 4 INVENTORY]."

    set check_loop_broken 0

    while {!$check_loop_broken} {

        puts -nonewline "\n> "

        gets stdin player(choice2)

        set player(choice2) [string toupper $player(choice2)]


        if {[string compare $player(choice2) "EXIT"] == 0} {

            set check_loop_broken 1
        
        } elseif {[string is entier $player(choice2)] == 1} {


            if {$player(choice2) < [llength $player(inv)] && $player(choice2) > -1} {

                if {[dict exists $master_inv [lindex $player(inv) $player(choice2)]]} {

                    puts [format "\n%s" \
                            [dict get $master_inv [lindex $player(inv) $player(choice2)] \
                        ]
                    ]

                    set continue [do_something_with_item? $player(choice2)]

                    if {$continue == -1} {
                        set check_loop_broken 1
                    
                    } else {
                    
                        puts -nonewline "\nEnter the number of the item you with to interact with,\n"
                        puts -nonewline "Or you could type [color 1 EXIT] to exit the [color 4 INVENTORY]."

                    }

                } else {

                    puts "Typo Error/Player's Item not found in the master list."

                }

            } else {

                puts "invalid!"
            }


        } else {

            puts "invalid!"
        }


    }


}
