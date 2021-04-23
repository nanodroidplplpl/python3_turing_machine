import os

import externals
import matrix

import PySimpleGUI as sg

def create_algorithm():
    os.system('clear')
    print('-> Podaj ilosc stanow: ')
    num = input()
    tab = []
    for i in range(int(num)):
        os.system('clear')
        print('Zasada wczytywania stanow: ','\n')
        print('nr stanu: automatycznie', '\n',
        'skok jesli 1: gdzie ma sie przesunac matryca 0-zostac 1-lewo 2-prawo',
        '\n', 'marker jesli 1: co zapisac', '\n',
        'goToStan jesli 1: do jakiego stanu skoczyc','\n',
        'skok jesli 0: gdzie ma sie przesunac matryca 0-zostac 1-lewo 2-prawo',
        '\n', 'marker jesli 0: co zapisac', '\n',
        'goToStan jesli 0: do jakiego stanu skoczyc','\n',
        )
        print('------------------','\n')
        print('Nr', i, '\n')
        print('Skok jesli 1: ')
        jump = int(input())
        print('\nMarker jesli 1: ')
        marker = int(input())
        print('\nPrzejdz do jesli 1: ')
        goToStan = int(input())
        print('Skok jesli 0: ')
        jump0 = int(input())
        print('\nMarker jesli 0: ')
        marker0 = int(input())
        print('\nPrzejdz do jesli 0: ')
        goToStan0 = int(input())
        print('Skok jesli end: ')
        jumpend = int(input())
        print('\nMarker jesli end: ')
        markerend = int(input())
        print('\nPrzejdz do jesli end: ')
        goToStanend = int(input())
        print('[*] Zapisuje')
        stan = matrix.State(i, jump, marker, goToStan, jump0, marker0, goToStan0, jumpend, markerend, goToStanend)
        tab.append(stan)
    return tab

def getAllDataFromFile():
    print('[*] Pobieranie danych...')
    file = open('states.txt', 'r')
    n = 0
    for line in file:
        n+=1
    tab = []
    for i in range(n):
        state = matrix.State(0,0,0,0,0,0,0)
        state.getDataFromFile(i)
        tab.append(state)
    file.close()
    print('[*] Pobieranie zakonczone')
    return tab

def wyswietlStany(tab):
    print(int(len(tab)/7))
    for i in range(int(len(tab)/7)):
        print('-----------------------')
        print('Stan: ', tab[i].getData())
        print('Skok 1: ', tab[i].getMove())
        print('Marker 1: ', tab[i].getMarker())
        print('goToStan 1: ', tab[i].getGoToStan())
        print('Skok 0: ', tab[i].getoMove())
        print('Marker 0: ', tab[i].getoMarker())
        print('goToStan 0: ', tab[i].getoGoToStan())
        print('Skok end: ', tab[i].getendMove())
        print('Marker end: ', tab[i].getendMarker())
        print('goToStan end: ', tab[i].getendGoToStan())

def goToStan(nr_stanu, tab):
    for i in range(int(len(tab)/7)):
        if (nr_stanu == tab[i].getNr()):
            return int(i)


#data to wejsc a tab to stany
def start_file(data, tab):
    print('w funkcji')

    go = True
    i = 0
    stan = tab[0]
    pice = int(data.go_to('stop'))
    nono = None
    while(go):
        print(stan.getData())
        print(data.tab)
        print(pice)
        if (pice == 1):
            #pice = stan.getMarker()
            x, y = data.give_actual()
            data.tab[x][y] = stan.getMarker()
            if (stan.getMove() == 1):
                pice = data.go_to('next')
                #print(data.go_to('stop'))
            elif (stan.getMove() == 2):
                pice = data.go_to('left')
                #print(data.go_to('stop'))
            #else:
            #     data.go_to('stop')
            stan = tab[goToStan(stan.getGoToStan(), tab)]
        elif (pice == 0):
            #pice = stan.getoMarker()
            x, y = data.give_actual()
            data.tab[x][y] = stan.getoMarker()
            if (stan.getoMove() == 1):
                pice = data.go_to('next')
            elif (stan.getoMove() == 2):
                pice = data.go_to('left')
            #else:
            #    data.go_to('stop')
            stan = tab[int(goToStan(stan.getoGoToStan(), tab))]
        elif (pice == 404):
            go = False
        elif (pice == 777):
            pice = data.go_to('next')

def head():
    data = externals.Dane(0,0)
    print('-> Czy chcesz wczytac dane z poprzedniej sesji czy dodac nowe')
    print('\n')
    print('Yes/No')
    switch = input()
    if switch == 'No':
        data.add_data()
    else:
        data.read_data()
        print('[*] Dane zostaly wczytane automatycznie')
    print('-> Czy wczytac stany matrycy z poprzedniej sesji?')
    print('\n')
    print('Yes/No')
    switch = input()
    if switch == 'No':
        tab = []
        tab = create_algorithm()
        print('[*] Zapisywanie stanow...')
        for i in range(len(tab)):
            tab[i].uploadToTxt()
        print('[*] Zapisano')
    else:
        tab = getAllDataFromFile()
    print('Twoje stany to: \n')
    wyswietlStany(tab)
    print('w funkcji')
    print('[*] Czy chcesz uruchomic? Jak tak napisz fire')
    ok = input()
    if ok == 'fire':
        start_file(data, tab)

def start_file_for_gui(data, tab):
    print('w funkcji')

    go = True
    i = 0
    stan = tab[0]
    pice = int(data.go_to('stop'))
    nono = None
    while(go):
        print(stan.getData())
        print(data.tab)
        print(pice)
        if (pice == 1):
            #pice = stan.getMarker()
            x, y = data.give_actual()
            data.tab[x][y] = stan.getMarker()
            if (stan.getMove() == 1):
                pice = data.go_to('next')
                #print(data.go_to('stop'))
            elif (stan.getMove() == 2):
                pice = data.go_to('left')
                #print(data.go_to('stop'))
            #else:
            #     data.go_to('stop')
            stan = tab[goToStan(stan.getGoToStan(), tab)]
        elif (pice == 0):
            #pice = stan.getoMarker()
            x, y = data.give_actual()
            data.tab[x][y] = stan.getoMarker()
            if (stan.getoMove() == 1):
                pice = data.go_to('next')
            elif (stan.getoMove() == 2):
                pice = data.go_to('left')
            #else:
            #    data.go_to('stop')
            stan = tab[int(goToStan(stan.getoGoToStan(), tab))]
        elif (pice == 404):
            go = False
        elif (pice == 777):
            pice = data.go_to('next')

    return stan.getNr()

# It is demo so you can use data from last sesion
def head_demo_gui():
    data = externals.Dane(0,0)

    #config layout
    layout = [ [sg.Text('Turing machine, make congfig data and algorithm and lets start')],
            [sg.Text('Czy chcesz wczytac algorytm z poprzedniej sesji?')],
            [sg.Button('Tak'), sg.Button('Nie')],
            [sg.Text('Podaj dane oddzielone spacjami np.: 0 0 1 0 1 1 ...')],
            [sg.Input(key='-input_data-')],
            [sg.Button('Fire')],
            [sg.Text('Stan: ', key=('-output_stan-')), sg.Text('Dane: ', key=('-output_data-'))],
    ]
    # Create the window
    window = sg.Window('Turing machine', layout)
    # Event loop to proces the window
    while True:
        event, values = window.read()
        if event == None:
            break
        if event == 'Tak':
            tab = getAllDataFromFile()
        #if event == 'Nie':
            #tutaj dopisze ten popup na ten algorytm
        if event == 'Fire':
            data.add_data_by_one_data_just_demo(values['-input_data-'])
            stan_back = start_file_for_gui(data, tab)
            window['-output_stan-'].update(stan_back)
            window['-output_data-'].update(data.tab)

    window.close()


def main():
    print('[*] Rozpoczynam konfiguracje')
    head()
    #head_demo_gui()

if __name__ == '__main__':
    main()
