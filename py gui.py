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


def win5_layout():
    layout = [
        [sg.Text('bruker navn', size=(15, 1)), sg.InputText(key='ny_bn')],
        [sg.Text('passord', size=(15, 1)), sg.InputText(key='ny_po')],
        [sg.Text('mobil nummer', size=(15, 1)), sg.InputText(key='ny_mn')],
        [sg.Button('Lagre', key='lagre_ny_bn')],
    ]
    return layout

def win6_layout():
    layout = [
        [sg.Text('ny bruker', size=(15, 1)), sg.Text('', size=(15, 1), key='ny_b_win6')],
        [sg.Button('Tilbake', key='bak_win6')],
    ]
    return layout



def login_function():
    global tab_while, tab_win
    win1 = sg.Window('logg inn', win1_layout(), return_keyboard_events=True, finalize=True)
    win1['passord'].bind("<Return>", "_Enter")
    logginn_while = True
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
                if tab_while == True:
                    tab_function()

def tab_function():
    global tab_while
    while tab_while:
        ev2, vals2 = tab_win.read(timeout=100)
        if ev2 == sg.WIN_CLOSED or ev2 == 'Escape:27':
            tab_while = False
        if not vals2['ny_bn'] == '':
            if ev2 == 'lagre_ny_bn' or ev2 == '_Enter':
                tab_win.Hide()
                brukernavn = vals2['ny_bn']
                passord = vals2['ny_po']
                mobil_nr = vals2['ny_mn']
                sql = "INSERT INTO brukere(brukernavn, passord, mobil_nr) VALUES (%s, %s, %s)"
                val = (brukernavn, passord, mobil_nr)
                mycursor.execute(sql, val)
                mydb.commit()
                win6 = sg.Window('Registrer ny bruker', win6_layout(), return_keyboard_events=True, finalize=True)
                win6.bind("<Return>", "_Enter")
                win6.read(timeout=100)
                win6['ny_b_win6'].update(vals2['ny_bn'])
                ev4, vals4 = win6()
                if ev4 or ev4 == '_Enter'== 'bak_win6':
                    win6.Close()
                    tab_win.UnHide()
                    tab_win['ny_bn'].update('')
                    tab_win['ny_po'].update('')
                    tab_win['ny_mn'].update('')
        if not vals2['Varenummer'] == '':
            if ev2 == 'lagre' or ev2 == '_Enter':
                vare_nr = vals2['Varenummer']
                produktnavn = vals2['Produktnavn']
                beskrivelse = vals2['Beskrivelse']
                pris = vals2['Pris']
                kategori = vals2['Kategori']
                bilde = vals2['Bilde src']
                lager_nr = vals2['Lager']
                sql = "INSERT INTO varer(vare_nr, produktnavn, beskrivelse, pris, kategori, bilde, lager_nr) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                val = (vare_nr, produktnavn, beskrivelse, pris, kategori, bilde, lager_nr)
                mycursor.execute(sql, val)
                mydb.commit()
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
                    win2.Close()
                    tab_win.UnHide()
                    tab_win['Varenummer'].update('')
                    tab_win['Produktnavn'].update('')
                    tab_win['Beskrivelse'].update('')
                    tab_win['Pris'].update('')
                    tab_win['Kategori'].update('')
                    tab_win['Lager'].update('')
                    tab_win['Bilde src'].update('')
                if ev3 == 'bak':
                    tab_win.UnHide()



tabgrp = [[sg.TabGroup([[sg.Tab('Finn vare', win4_layout()),
                         sg.Tab('Registrer ny vare', win3_layout()),
                         sg.Tab('Registrer ny bruker', win5_layout())
                         ]])]]
win3 = sg.Window('Registrering', win3_layout())
win4 = sg.Window('Finn', win4_layout())
win5 = sg.Window('ny bruker', win5_layout())


login_function()

