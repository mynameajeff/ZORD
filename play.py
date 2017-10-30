#!/usr/bin/env python3

import tkinter
import sys

r = tkinter.Tcl()

try:

    r.eval('source intro.tcl')

except tkinter._tkinter.TclError:

    sys.exit()
