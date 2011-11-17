#!/usr/bin/env python

# GNOME/AT-SPI needed
# AT-SPI = Assistive Technology Service Provider Interface


import time
import pyatspi


start = time.time()
pyatspi.Registry.generateKeyboardEvent(67, None, pyatspi.KEY_PRESS)
pyatspi.Registry.generateKeyboardEvent(36, None, pyatspi.KEY_PRESSRELEASE)
pyatspi.Registry.generateKeyboardEvent(67, None, pyatspi.KEY_RELEASE)
end = time.time()
print end - start
