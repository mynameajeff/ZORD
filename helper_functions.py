
import os

if os.name == "posix":

    from curses import tparm, tigetstr
    import curses

    try:
        curses.setupterm()
    except curses.error:
        print("ERROR: CURSES FAILED, must be run in a valid terminal.")

    def color(foreground, text):
        return tparm(tigetstr('setaf'), foreground).decode("utf-8") + \
                text + tigetstr("sgr0").decode("utf-8")

else:

    def color(foreground, text):
        return text

