#!/usr/bin/env python

# sudo aptitude install xvkbd


import time
import shlex
import subprocess


command = shlex.split('xvkbd -text "\[F1]\r\[Return]"')
start = time.time()
process = subprocess.Popen(command, stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE, stdin=subprocess.PIPE)
process.wait()
end = time.time()
print end - start
