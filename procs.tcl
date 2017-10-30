
# this procedure allows me to color the text.
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

proc get_inventory {} {

    global player
    global player_inv

    if {$player(inv_count) < 1} {
    
        return "There are no items in your inventory."
    
    } else {

        set return_val "\nINVENTORY:\n"

        for {set index 0} {$index < [llength $player_inv]} {incr index} {

            append return_val [format "· %s\n" [lindex $player_inv $index]]
        } 

        return [string trimright $return_val "\n"]

    }

}
