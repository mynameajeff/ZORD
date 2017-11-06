#!/usr/bin/env tclsh

set NEEDED "procs.tcl"
set NEXT_PART "game_1.tcl"

source $NEEDED

puts "\nWelcome to the [color 5 Z][color 135 0][color 141 R][color 147 D] RPG!\n"

puts "\[[color 3 1]\] play the game"
puts "\[[color 3 2]\] information about the game"
puts "\[[color 3 3]\] exit the game"

set s_choice_0 0 ;# to begin the loop

while {$s_choice_0 != 1} {

    puts -nonewline "\n> "

    gets stdin g_choice_0

    switch $g_choice_0 {

        1 {
            set s_choice_0 1
        }

        2 {
            puts "This game was designed by [color 3 mynameajeff] in a few days to test Tcl w/ Python."
            puts "It contains examples of various features of the language being used."

            puts -nonewline "\n[color 2 HP] is [color 2 H]ealth [color 2 P]oints."
            puts " When these reach Zero, you lose the game."

            puts -nonewline "[color 1 XP] is e[color 1 X]perience [color 1 P]oints."
            puts " These allow you to level up and become stronger."

            puts -nonewline "[color 4 SP] is [color 4 S]pecial [color 4 P]oints."
            puts " These are used to perform magick."

            puts -nonewline "[color 6 ST] is [color 6 ST]amina."
            puts " These are used to run away from enemies, and attack harder."

        }

        3 {
            puts "leaving...\n"
            exit ;# this doesn't work with Tkinter, hence the try-except gaurd.
            # it effectively allows me to bootleg-exit
        }

        default {
            puts "incorrect choice."
        }
    }

}

source $NEXT_PART
