import configparser
import os
import time
import grabber as g


from telethon import TelegramClient, events, sync, types
from telethon.tl.functions.messages import GetDialogsRequest, GetHistoryRequest
from telethon.tl.types import InputPeerEmpty
from dateutil import parser


def config_setup():
    os.system('clear')
    client = check_config()


def check_config():
    print('===================')
    print('Reading Credentials')
    print('===================')
    credential = configparser.RawConfigParser()
    credential.read('creds')
    try:
        api_id = credential['API']['id']
        api_hash = credential['API']['hash']
        client = TelegramClient(
            ('session_' + api_id), api_id, api_hash)
        os.system('clear')
        client = login(client)
        return client
    except KeyError:
        print('=============================================')
        print('Credentials not Found! Configuring a new one!')
        print('=============================================')
        os.system('clear')
        config_setup()


def login(client):
    print('=================')
    print('Logging In to API')
    print('=================')
    client.start()
    os.system('clear')
    print('=============')
    print('Login Success')
    print('=============')
    time.sleep(2)
    os.system('clear')
    return client
