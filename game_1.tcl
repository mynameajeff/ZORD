#!/usr/bin/env tclsh

# player stats
set player(hp_max) 25
set player(sp_max) 15
set player(xp_max) 25

set player(hp) [randint 5 25]

set player(sp) [randint 5 15]

set player(xp) 0

set player(level) 0

set player(sta) 10

set player_inv [list Basic\ short-sword Bread]

set player(inv_count) [string length player_inv]
#~~~~~~~~~~~~~

set name_given 0

while {!$name_given} {

    puts -nonewline "\nWhat's your name? (MAX 20 CHARACTERS)\n> "

    gets stdin player(name)

    if {[string length $player(name)] > 20} {
        puts "invalid name."
    
    } else {
        set name_given 1
    }

}

set class_chosen 0

while {!$class_chosen} {

    puts -nonewline "\nDo you wish to be a [color 5 MAGE], or a [color 9 WARRIOR]?\n> "

    gets stdin player(class)

    set player(class) [string toupper $player(class)]

    switch $player(class) {

        MAGE {
            set player(class) [color 5 $player(class)]
            set class_chosen 1
        }

        WARRIOR {
            set player(class) [color 9 $player(class)]
            set class_chosen 1
        }

        default {
            puts "invalid."
        }
    }

    puts "You're a $player(class) now!"
}


set main_loop_broken 0

while {!$main_loop_broken} {

    level_up?

    show_stats

    puts -nonewline "\nDo you want to [color 2 SCAVENGE] for supplies, [color 1 HUNT] monsters, "
    puts -nonewline "[color 3 LOOK] around you, or [color 4 CHECK] your inventory?\n> "
    gets stdin player(choice1)

    set player(choice1) [string toupper $player(choice1)]

    switch $player(choice1) {

        SCAVENGE {

        }

        HUNT {

        }

        LOOK {

        }

        CHECK {
            puts [get_inventory]
        }
    }

    if {$player(hp) == 0} {
        # set main_loop_broken 1 ;# in other words, game over!
        exit
    }
}
