import PySimpleGUI as sg
 
# Design pattern 2 - First window remains active


def win1_layout():
    layout = [
        [sg.Text('Brukernavn', size=(15, 1)), sg.InputText(key='brukernavn', size=(30, 10))],
        [sg.Text('Passord', size=(15, 1)), sg.InputText(key='passord', size=(30, 10))],
        [sg.Button('Logg inn', key='logginn')],
    ]

    return layout



def win2_layout():
    layout = [
        [sg.Text('Registrering av varer', text_color='black')],
        [sg.Text('Varenummer', size =(15, 1)), sg.Text('', size=(15, 1), key='Varenummer2')],
        [sg.Text('Produktnavn', size =(15, 1)), sg.Text('', size=(15, 1), key='Produktnavn2')],
        [sg.Text('Beskrivelse', size =(15, 1)), sg.Text('', size=(15, 1), key='Beskrivelse2')],
        [sg.Text('Pris', size =(15, 1)), sg.Text('', size=(15, 1), key='Pris2')],
        [sg.Text('Kategori', size =(15, 1)), sg.Text('', size=(15, 1), key='Kategori2')],
        [sg.Text('Lager', size =(15, 1)), sg.Text('', size=(15, 1), key='Lager2')],
        [sg.Text('Bilde src', size =(15, 1)), sg.Text('', size=(15, 1), key='Bilde src2')],
        
    ]
    return layout


def win3_layout():
    layout = [
        [sg.Text('Registrering av varer', text_color='black')],
        [sg.Text('Varenummer', size=(15, 1)), sg.InputText(key='Varenummer')],
        [sg.Text('Produktnavn', size=(15, 1)), sg.InputText(key='Produktnavn')],
        [sg.Text('Beskrivelse', size=(15, 1)), sg.InputText(key='Beskrivelse')],
        [sg.Text('Pris', size=(15, 1)), sg.InputText(key='Pris')],
        [sg.Text('Kategori', size=(15, 1)), sg.InputText(key='Kategori')],
        [sg.Text('Lager', size=(15, 1)), sg.InputText(key='Lager')],
        [sg.Text('Bilde src', size=(15, 1)), sg.InputText(key='Bilde src')],
        [sg.Button('Lagre', key='lagre')],
    ]

    return layout



def win4_layout():
    layout = [
        [sg.Text('Finn vare', text_color='black')],
        [sg.Text('Varenummer', size =(15, 1)), sg.InputText(key='Varenummer_finn')],
        [sg.Button('Finn', key='finn')],
    ]
    return layout

tabgrp = [[sg.TabGroup([[sg.Tab('Finn vare', win4_layout()),
                         sg.Tab('Registrering av vare', win3_layout())]])]]

win1 = sg.Window('logg inn', win1_layout(), return_keyboard_events= True, finalize= True)
win2 = sg.Window('Registrering', win2_layout())
win3 = sg.Window('Registrering', win3_layout())
win1['passord'].bind("<Return>", "_Enter")
win4 = sg.Window('Finn', win4_layout())
tab_win = sg.Window("tabs", tabgrp)


while True:
    ev1, vals1 = win3.read(timeout=100)
    ev2, vals2 = win1.read(timeout=100)
    if ev2 == sg.WIN_CLOSED or ev2 == 'Escape:27':
        break
    if not vals2['brukernavn'] == '' and not vals2['passord'] == '':
        if ev2 == 'passord' + '_Enter' or ev2 == 'logginn':
            win1.Hide()
            tab_win.read()

    if ev1 == 'lagre':
        win2.read(timeout=100)
        win2['Varenummer2'].update(vals1['Varenummer'])
        win2['Produktnavn2'].update(vals1['Produktnavn'])
        win2['Beskrivelse2'].update(vals1['Beskrivelse'])
        win2['Pris2'].update(vals1['Pris'])
        win2['Kategori2'].update(vals1['Kategori'])
        win2['Lager2'].update(vals1['Lager'])
        win2['Bilde src2'].update(vals1['Bilde src'])






