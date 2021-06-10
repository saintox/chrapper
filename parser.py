import os
import glob
import re
import pandas as p
import time


def clear():
    os.system('clear')


def parser_menu():
    print('=======================')
    print('Select file for parsing')
    print('=======================')
    csv_list = [f for f in glob.glob('archive/*.csv')]
    i = 0
    for filename in csv_list:
        print('['+str(i)+'] ' + filename.replace('archive/', ''))
        i += 1

    select = input('Select file: ')
    selected = csv_list[int(select)]
    clear()
    parser_method(selected)


def parser_method(filename):
    print('=====================')
    print('Select parsing method')
    print('=====================')
    print()
    print('[1] Regex')
    print('[2] String')
    selected = input('Select method: ')
    clear()
    parser_core(filename, selected)


def parser_core(filename, method):
    clear()
    reg = input('Input regex : ')
    clear()
    print('****************')
    print('Processing data!')
    print('****************')
    rd = p.read_csv(filename,
                    error_bad_lines=False,
                    delimiter=';',
                    lineterminator='\n')
    pattern = re.compile(reg, flags=re.I + re.X)

    with open('result/' + filename.replace('archive/', '').replace('.csv', '') + '.txt', 'w', encoding='UTF-8') as res:
        for idx, data in rd.iterrows():
            match = re.findall(pattern, data['text'])
            if (len(match)):
                res.write('From : ' + data['username'] + '\n')
                res.write('Date : ' + data['date'] + '\n')

                for pkg in match:
                    res.write('Package : ' + pkg[0] + '\n')
                    res.write('Value : ' + pkg[1] + '\n')
                res.write('\n')
    clear()
    print('******************************')
    print('Results are written to folder!')
    print('******************************')
    time.sleep(2)
    clear()
