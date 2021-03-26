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

from os import path, system

branch_sign   = '⎇'
internet_sign = '🌐'

mercurial   = branch_sign
git         = branch_sign

get_git_branch       = "git branch | grep '^*' | sed 's/* //'"
get_mercurial_branch = "hg branch"

bin = "/bin/{}"

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
    from time import localtime, strftime

    hour   = int(strftime('%H', localtime()))
    minute = int(strftime('%M', localtime()))

    if minute >= 30:
        time_widget_main(hour, minute, True)
    else:
        time_widget_main(hour, minute, False)


def time_widget_init() -> tuple:
    with open('/proc/uptime', 'r') as line:
        seconds = float(line.readline().split()[0])

    days    = seconds / 60 / 60 / 24
    hours   = seconds / 60 / 60 % 24
    minutes = seconds / 60 % 60

    return (days, hours, minutes)


def branch_widget():
    if  path.exists(".hg") and path.isfile(bin.format("hg")):
        system(get_mercurial_branch)
    elif path.exists(".git") and path.isfile(bin.format("git")):
        system(get_git_branch)

# It has not any checker for executables of VCSs.
def branch_widget_fast():
    if  path.exists(".hg"):
        system(get_mercurial_branch)
    elif path.exists(".git"):
        system(get_git_branch)

def uptime_widget(to_int: bool):
    time = time_widget_init()

    if to_int:
        print(int(time[1]), 'h ', int(time[2]), 'm', sep='')
    else:
        print(time[1], 'h ', time[2], 'm')

def check_internet_connection() -> bool:
    try:
        import httplib
    except:
        import http.client as httplib

    connection = httplib.HTTPConnection("www.google.com", timeout=1)

    try:
        connection.request("HEAD", "/")
        connection.close()

        return True
    except:
        connection.close()

        return False


def internet_connection_widget():
    if check_internet_connection():
        print(internet_sign)