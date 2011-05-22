#!/usr/bin/env python
# -*- coding:utf-8 -*-

#
# Author: Italo Maia
# Website: http://www.italomaia.com/
#

# -- raw shellscript --
# xinput list | grep -i touchpad
# xinput set-prop 15 "Device Enabled" 0

import re, shlex
from subprocess import call, Popen, PIPE

def get_touchpad_device():
    cmd = 'xinput list'
    p = Popen(shlex.split(cmd), stdout=PIPE)
    p.wait()

    cmd = 'grep -i touchpad'
    p = Popen(shlex.split(cmd), stdin=p.stdout, stdout=PIPE)
    p.wait()

    m = re.search(r'id=(\d+)', p.stdout.read())
    if m is not None:
        return m.group(1)
    else:
        return None

def get_param(args):
    if len(args) != 1:
        return None

    param = args[0].lower()
    if param == "on":
        return 1
    return 0

def print_report(param):
    if param:
        print "Touchpad device enabled."
    else:
        print "Touchpad device disabled."

def main(args):
    param = get_param(args)
    if param is None:
        print "ON or OFF?"
        exit(0)

    touchpad_device = get_touchpad_device()
    if touchpad_device is None:
        print "Touchpad device could not be found."
        exit(1)

    cmd = 'xinput set-prop %s "Device Enabled" %d' % (touchpad_device, param)
    retcode = call(shlex.split(cmd))
    print_report(param)

if __name__=="__main__":
    import sys
    main(sys.argv[1:])
