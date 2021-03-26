# MIT License
#
# Copyright (c) 2020-2021 Ferhat Geçdoğan All Rights Reserved.
# Distributed under the terms of the MIT License.
#
#

# PyCLIWidget (library)
#
# Directly port of CLIWidget library
#
# github.com/ferhatgec/cliwidget

# TODO:
# Mercurial & Git branch widget.
# Uptime widget.
# Internet connection widget.

from time import localtime, strftime

def convert(minute: int, time: int) -> bool:
    if minute == time or minute + 12 == time:
        return True

    return False

def time_widget_main(i_time: int, minute: int, half: bool):
    if   convert(1, i_time):
        (lambda: print('🕐'), lambda: print('🕜'))[half]()
    elif convert(2, i_time):
        (lambda: print('🕑'), lambda: print('🕝'))[half]()
    elif convert(3, i_time):
        (lambda: print('🕒'), lambda: print('🕞'))[half]()
    elif convert(4, i_time):
        (lambda: print('🕓'), lambda: print('🕟'))[half]()
    elif convert(5, i_time):
        (lambda: print('🕔'), lambda: print('🕠'))[half]()
    elif convert(6, i_time):
        (lambda: print('🕕'), lambda: print('🕡'))[half]()
    elif convert(7, i_time):
        (lambda: print('🕖'), lambda: print('🕢'))[half]()
    elif convert(8, i_time):
        (lambda: print('🕗'), lambda: print('🕣'))[half]()
    elif convert(9, i_time):
        (lambda: print('🕘'), lambda: print('🕤'))[half]()
    elif convert(10, i_time):
        (lambda: print('🕙'), lambda: print('🕥'))[half]()
    elif convert(11, i_time):
        (lambda: print('🕚'), lambda: print('🕦'))[half]()
    elif convert(12, i_time):
        (lambda: print('🕛'), lambda: print('🕧'))[half]()


def time_widget():
    hour   = int(strftime('%H', localtime()))
    minute = int(strftime('%M', localtime()))

    if minute >= 30:
        time_widget_main(hour, minute, True)
    else:
        time_widget_main(hour, minute, False)