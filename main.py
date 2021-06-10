import os
import sys
import time
import setup as s
import grabber as g
import parser as p

client = None


def clear():
    os.system('clear')


def scrap_chat():
    print('Feature not ready')
    clear()


def mainmenu():
    global client
    clear()
    menu_select = 0

    print('====================')
    print('WELCOME TO CHRAPPER')
    print('====================')
    print()
    print()
    print('[1] Setup session')
    print('[2] Grab chat')
    print('[3] Scrap chat')
    print('[4] Exit')
    print()

    menu_select = input('Select feature : ')

    if (menu_select == '1'):
        clear()
        client = s.check_config()
    elif (menu_select == '2'):
        clear()
        if (client == None):
            print('Please setup the session first!')
            time.sleep(2)
            mainmenu()
        else:
            g.selection(client)
    elif (menu_select == '3'):
        clear()
        p.parser_menu()
    elif (menu_select == '4'):
        clear()
        goodbye()

    while menu_select != 3:
        mainmenu()


def goodbye():
    print('============================')
    print('THANK YOU FOR USING CHRAPPER')
    print('============================')
    time.sleep(1)
    clear()
    exit()


try:
    clear()
    mainmenu()

except IndexError:
    print('Error')
