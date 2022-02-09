import PySimpleGUI as sg
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="nettbutikk_db")
mycursor = mydb.cursor()
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
        [sg.Text('Varenummer', size=(15, 1)), sg.Text('', size=(15, 1), key='Varenummer2')],
        [sg.Text('Produktnavn', size=(15, 1)), sg.Text('', size=(15, 1), key='Produktnavn2')],
        [sg.Text('Beskrivelse', size=(15, 1)), sg.Text('', size=(15, 1), key='Beskrivelse2')],
        [sg.Text('Pris', size=(15, 1)), sg.Text('', size=(15, 1), key='Pris2')],
        [sg.Text('Kategori', size=(15, 1)), sg.Text('', size=(15, 1), key='Kategori2')],
        [sg.Text('Lager', size=(15, 1)), sg.Text('', size=(15, 1), key='Lager2')],
        [sg.Text('Bilde src', size=(15, 1)), sg.Text('', size=(15, 1), key='Bilde src2')],
        [sg.Button('Lagre', key='lagre_win2'), sg.Button('Tilbake', key='bak')],

    ]
    return layout


def win3_layout():
    layout = [
        [sg.Text('Welcome', text_color='black', key='welcome2')],
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
        [sg.Text('Welcome', text_color='black', key='welcome')],
        [sg.Text('Varenummer', size=(15, 1)), sg.InputText(key='Varenummer_finn')],
        [sg.Button('Finn', key='finn')],
    ]
    return layout


tabgrp = [[sg.TabGroup([[sg.Tab('Finn vare', win4_layout()),
                         sg.Tab('Registrering av vare', win3_layout())]])]]

win1 = sg.Window('logg inn', win1_layout(), return_keyboard_events=True, finalize=True)
win1['passord'].bind("<Return>", "_Enter")
win3 = sg.Window('Registrering', win3_layout())
win4 = sg.Window('Finn', win4_layout())


logginn_while = True
tab_while = False
while logginn_while:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED or ev1 == 'Escape:27':
        logginn_while = False
    if not vals1['brukernavn'] == '' and not vals1['passord'] == '':
        if ev1 == 'passord' + '_Enter' or ev1 == 'logginn':
            tab_win = sg.Window("Nettbutikk", tabgrp, finalize=True)
            tab_win.bind("<Return>", "_Enter")

            bn = vals1['brukernavn']
            po = vals1['passord']
            sql = "SELECT brukernavn, passord FROM brukere WHERE brukernavn =%s AND passord = %s"
            mycursor.execute(sql, (bn, po))
            myresult = mycursor.fetchall()
            row_count = mycursor.rowcount
            if row_count == 1:
                sql = "SELECT brukernavn FROM brukere WHERE brukernavn =%s AND passord = %s"
                mycursor.execute(sql, (bn, po))
                myresult = mycursor.fetchone()
            myid = myresult[0]

            tab_win['welcome'].update(vals1['brukernavn'])
            tab_win['welcome2'].update(vals1['brukernavn'])

            win1.Close()
            logginn_while = False
            tab_while = True

while tab_while:

    ev2, vals2 = tab_win.read(timeout=100)
    if ev2 == sg.WIN_CLOSED or ev2 == 'Escape:27':
        tab_while = False
    if ev2 == 'lagre' or ev2 == '_Enter':
        win2 = sg.Window('Registrering', win2_layout(), return_keyboard_events=True, finalize=True)
        win2.bind("<Return>", "_Enter")
        tab_win.Hide()
        win2.read(timeout=100)
        win2['Varenummer2'].update(vals2['Varenummer'])
        win2['Produktnavn2'].update(vals2['Produktnavn'])
        win2['Beskrivelse2'].update(vals2['Beskrivelse'])
        win2['Pris2'].update(vals2['Pris'])
        win2['Kategori2'].update(vals2['Kategori'])
        win2['Lager2'].update(vals2['Lager'])
        win2['Bilde src2'].update(vals2['Bilde src'])
        ev3, vals3 = win2()

        if ev3 == 'lagre_win2' or ev3 == '_Enter':
            break
        if ev3 == 'bak':
            tab_win.UnHide()




