#!/usr/bin/env python
# sudo aptitude install python-bluetooth
# Developed by Tatiana Al-Chueyr and Álvaro Justen
# License: GPLv2 http://www.gnu.org/licenses/gpl-2.0.html

import bluetooth
import pyatspi


arduino_BT_MAC = '00:3C:B8:B1:12:F0'
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

sock.connect((arduino_BT_MAC, 1))
print 'Connected. Receiving...'

status_old = [pyatspi.KEY_RELEASE for x in range(6)]
status = [0 for x in range(6)]
keycodes = (36, 67, 68, 69, 70, 71)

while True:
    try:
        receive_buffer = sock.recv(1)
        buttons_values = ord(receive_buffer[0])
        for i in range(6):
            status[i] = (buttons_values >> i) & 1 and pyatspi.KEY_RELEASE or pyatspi.KEY_PRESS
        
        for i in range(6):
            if status[i] != status_old[i]:
                #pyatspi.Registry.generateKeyboardEvent(keycodes[i], None, status[i])
                status_old[i] = status[i]
                print 'Key %d changed!' % i


    except KeyboardInterrupt:
        sock.disconnect()
        break