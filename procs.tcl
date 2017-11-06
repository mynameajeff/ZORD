
source "procs2.tcl"

# color procedure courtesy of Donal Fellows
#stackoverflow.com/questions/25519393/how-to-change-color-text-using-puts-in-tcl
proc color {foreground text} {
    # tput is a little Unix utility that lets you use the termcap database
    # *much* more easily...
    return [exec tput setaf $foreground]$text[exec tput sgr0]
}

# the base is the number lowest, where the heighest number is hinum.
# this procedure returns a number between base to hinum.
proc randint {base hinum} {
    return [expr {
            int($base + rand() * ($hinum - $base))
        }
    ]
}

# this procedure checks to see if XP is equal to XP_MAX,
# then if it is it increases the level of the player.
proc level_up? {} {

    global player

    if {$player(xp) == $player(xp_max)} {

        set player(xp) 0
        set player(xp_max) [expr {int($player(xp_max) * 1.75)}]

        set player(hp) [expr {int($player(hp) * 1.5)}]
        set player(hp_max) [expr {int($player(hp_max) * 1.5)}]

        set player(level) [expr $player(level) + 1]

        puts "Level Up! You're now level $player(level)."
    }
}

# this procedure PUTS(prints) to stdout the STATISTICS of the player.
proc show_stats {} {

    global player

    puts "\nNAME: \"$player(name) the $player(class)\", LVL: $player(level)"

    puts "HP:   [format %.2d $player(hp)]/$player(hp_max), XP: $player(xp)"

    puts "SP:   [format %.2d $player(sp)]/$player(sp_max), ST: $player(sta)"

}

# this procedure returns a string detailling the contents of the players inventory.
proc get_inventory {} {

    global player

    set inv [color 4 INVENTORY]

    if {[llength $player(inv)] < 1} {
    
        return "\nThere are no items in your $inv."
    
    } else {

        set return_val "\n$inv:\n"

        for {set index 0} {$index < [llength $player(inv)]} {incr index} {

            append return_val [format "· \[%s\] %s\n" \
                [color 3 $index] \
                [lindex $player(inv) $index] \
            ]
        } 

        return [string trimright $return_val "\n"]

    }

}
