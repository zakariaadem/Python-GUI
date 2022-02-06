import PySimpleGUI as sg
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="nettbutikk_DB"
)
mycursor = mydb.cursor()
sql = "SELECT passord, brukernavn, mobil_nr"
mycursor.execute(sql)
myresult = mycursor.fetchall()

print(myresult)
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
        [sg.Text('Varenummer', size=(15, 1)), sg.Text('', size=(15, 1), key='Varenummer2')],
        [sg.Text('Produktnavn', size=(15, 1)), sg.Text('', size=(15, 1), key='Produktnavn2')],
        [sg.Text('Beskrivelse', size=(15, 1)), sg.Text('', size=(15, 1), key='Beskrivelse2')],
        [sg.Text('Pris', size=(15, 1)), sg.Text('', size=(15, 1), key='Pris2')],
        [sg.Text('Kategori', size=(15, 1)), sg.Text('', size=(15, 1), key='Kategori2')],
        [sg.Text('Lager', size=(15, 1)), sg.Text('', size=(15, 1), key='Lager2')],
        [sg.Text('Bilde src', size=(15, 1)), sg.Text('', size=(15, 1), key='Bilde src2')],

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
        [sg.Text('Varenummer', size=(15, 1)), sg.InputText(key='Varenummer_finn')],
        [sg.Button('Finn', key='finn')],
    ]
    return layout


tabgrp = [[sg.TabGroup([[sg.Tab('Finn vare', win4_layout()),
                         sg.Tab('Registrering av vare', win3_layout())]])]]

win1 = sg.Window('logg inn', win1_layout(), return_keyboard_events=True, finalize=True)
win2 = sg.Window('Registrering', win2_layout())
win3 = sg.Window('Registrering', win3_layout())
win1['passord'].bind("<Return>", "_Enter")
win4 = sg.Window('Finn', win4_layout())
tab_win = sg.Window("tabs", tabgrp)


logginn_while = True
tab_while = False
while logginn_while:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED or ev1 == 'Escape:27':
        logginn_while = False
    if not vals1['brukernavn'] == '' and not vals1['passord'] == '':
        if ev1 == 'passord' + '_Enter' or ev1 == 'logginn':
            win1.Close()
            logginn_while = False
            tab_while = True

while tab_while:
    ev2, vals2 = tab_win.read(timeout=100)
    if ev2 == sg.WIN_CLOSED or ev2 == 'Escape:27':
        tab_while = False
    if ev2 == 'lagre':
        win2.read(timeout=100)
        win2['Varenummer2'].update(vals2['Varenummer'])
        win2['Produktnavn2'].update(vals2['Produktnavn'])
        win2['Beskrivelse2'].update(vals2['Beskrivelse'])
        win2['Pris2'].update(vals2['Pris'])
        win2['Kategori2'].update(vals2['Kategori'])
        win2['Lager2'].update(vals2['Lager'])
        win2['Bilde src2'].update(vals2['Bilde src'])






