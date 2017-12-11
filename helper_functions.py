
from curses import tparm, tigetstr
import curses

curses.setupterm()

def color(foreground, text):

    return tparm(tigetstr('setaf'), foreground).decode("utf-8") + \
            text + tigetstr("sgr0").decode("utf-8")
