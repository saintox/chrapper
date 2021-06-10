import configparser
import os
import sys
import time
import datetime
import pytz
import csv


from telethon import TelegramClient, events, sync, types
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telethon.tl.types import InputPeerEmpty
from dateutil import parser

tz = pytz.timezone('Asia/Jakarta')


def clear():
    os.system('clear')


def filter(client, chat):
    start = str(input('Input start date (ex: 2021-6-3) : '))
    end = str(input('Input end date (ex: 2021-6-3) : '))
    try:
        dt_start = datetime.datetime.strptime(
            start, '%Y-%m-%d').replace(tzinfo=tz)
        dt_end = datetime.datetime.strptime(
            end, '%Y-%m-%d').replace(tzinfo=tz)+datetime.timedelta(days=1)

    except ValueError:
        print("Incorrect format")
        clear()
        filter(client, chat)

    clear()

    with open('archive/' + chat.title + '_' + start + '_' + end + '.csv', 'w', encoding='UTF-8') as f:
        writer = csv.writer(f, delimiter=';', lineterminator='\n')
        writer.writerow(['username', 'date', 'text'])
        print('****************')
        print('Processing data!')
        print('****************')

        for message in client.iter_messages(chat, limit=None, offset_date=dt_end):
            if (dt_start > message.date.astimezone(tz)):
                break
            if(message.message):
                writer.writerow(
                    [message.get_sender().username, message.date.astimezone(tz), message.message])

        clear()

    print('**************************************')
    print('Results are written to archive folder!')
    print('**************************************')
    time.sleep(2)
    clear()


def selection(client):
    chats = []
    chats.extend(client.iter_dialogs(limit=10))
    i = 0
    for chat in chats:
        print('['+str(i)+'] ' + chat.title)
        i += 1

    select = input('Select chat: ')
    dialog = chats[int(select)]
    clear()
    filter(client, dialog)
