
import os, sys

if os.name == "posix":

    from curses import tparm, tigetstr
    import curses

    try:
        curses.setupterm()
    except curses.error:
        print("ERROR: CURSES FAILED, must be run in a valid terminal.")
        sys.exit()

    # this clears the terminal, however it's only been tested to work on linux.
    CLEAR_SCR = "\033c"

    def color(foreground, text):
        return tparm(tigetstr('setaf'), foreground).decode("utf-8") + \
                text + tigetstr("sgr0").decode("utf-8")

else:

    CLEAR_SCR = ""

    color = lambda _, text: text
