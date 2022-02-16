import PySimpleGUI as sg
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="nettbutikk_db")
mycursor = mydb.cursor(buffered=True)

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
        [sg.Text('lagret', text_color='red', size=(15, 1))],
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
        [sg.Text('Bruker ID', size=(15, 1)), sg.InputText(key='bid_finn')],
        [sg.Text('Varenummer', size=(15, 1)), sg.InputText(key='vn_finn')],
        [sg.Button('Finn', key='finn')],
    ]
    return layout


def win5_layout():
    layout = [
        [sg.Text('bruker navn', size=(15, 1)), sg.InputText(key='ny_bn')],
        [sg.Text('passord', size=(15, 1)), sg.InputText(key='ny_po')],
        [sg.Text('mobil nummer', size=(15, 1)), sg.InputText(key='ny_mn')],
        [sg.Text('Bruker ID', size=(15, 1)), sg.InputText(key='ny_bid')],
        [sg.Button('Lagre', key='lagre_ny_bn')],
    ]
    return layout

def win6_layout():
    layout = [
        [sg.Text('lagret', text_color='red', size=(15, 1))],
        [sg.Text('ny bruker', size=(15, 1)), sg.Text('', size=(15, 1), key='ny_b_win6')],
        [sg.Button('Tilbake', key='bak_win6')],
    ]
    return layout

def win7_layout():
    layout = [
        [sg.Text('Bruker', size=(15, 1)), sg.Text('', size=(15, 1), key='bn_win7')],
        [sg.Text('Passord', size=(15, 1)), sg.Text('', size=(15, 1), key='bn_win7_1')],
        [sg.Text('Mobil nr', size=(15, 1)), sg.Text('', size=(15, 1), key='bn_win7_2')],
        [sg.Text('Bruker ID', size=(15, 1)), sg.Text('', size=(15, 1), key='bn_win7_3')],
        [sg.Button('Slett bruker', key='sb_win7'), sg.Button('Tilbake', key='bak_win7')],
    ]
    return layout

def win8_layout():
    layout = [
        [sg.Text('Varenummer', size=(15, 1)), sg.Text('', size=(15, 1), key='vn_win8')],
        [sg.Text('produktnavn', size=(15, 1)), sg.Text('', size=(15, 1), key='pn_win8')],
        [sg.Text('beskrivelse', size=(15, 1)), sg.Text('', size=(15, 1), key='bs_win8')],
        [sg.Text('pris', size=(15, 1)), sg.Text('', size=(15, 1), key='p_win8')],
        [sg.Text('kategori', size=(15, 1)), sg.Text('', size=(15, 1), key='ka_win8')],
        [sg.Text('bilde', size=(15, 1)), sg.Text('', size=(15, 1), key='bl_win8')],
        [sg.Text('lagernummer', size=(15, 1)), sg.Text('', size=(15, 1), key='ln_win8')],
        [sg.Button('Slett vare', key='sv_win8'), sg.Button('Tilbake', key='bak_win8')],

    ]
    return layout


def login_function():
    global tab_while, tab_win
    global vals1
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
                #print(myresult)
                '''row_count = mycursor.rowcount
                if row_count == 1:
                    sql = "SELECT brukernavn FROM brukere WHERE brukernavn =%s AND passord = %s"
                    mycursor.execute(sql, (bn, po))
                    myresult = mycursor.fetchone()
                    myid = myresult[0]'''

                tab_win['welcome'].update(vals1['brukernavn'])
                tab_win['welcome2'].update(vals1['brukernavn'])
                win1.Close()
                logginn_while = False
                tab_while = True
                if tab_while == True:
                    tab_function()
def tab_function():
    global tab_while
    global vals2
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
                brukerid = vals2['ny_bid']
                sql = "INSERT INTO brukere(brukernavn, passord, mobil_nr, brukerid) VALUES (%s, %s, %s, %s)"
                val = (brukernavn, passord, mobil_nr, brukerid)
                mycursor.execute(sql, val)
                mydb.commit()
                win6 = sg.Window('Registrer ny bruker', win6_layout(), return_keyboard_events=True, finalize=True)
                win6.bind("<Return>", "_Enter")
                win6.read(timeout=100)
                win6['ny_b_win6'].update(vals2['ny_bn'])
                ev4, vals4 = win6()
                if ev4 == '_Enter' or ev4 == 'bak_win6':
                    win6.Close()
                    tab_win.UnHide()
                    tab_win['ny_bn'].update('')
                    tab_win['ny_po'].update('')
                    tab_win['ny_mn'].update('')
                    tab_win['ny_bid'].update('')
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
                    win2.Close()
                    tab_win.UnHide()
        if not vals2['bid_finn'] == '':
            bi_input = vals2['bid_finn']
            if ev2 == 'finn' or ev2 == '_Enter':
                se_bn = ("SELECT brukernavn FROM brukere Where brukerid =%s;" % bi_input)
                mycursor.execute(se_bn)
                myresult_fra_brukere = mycursor.fetchall()


                se_po = ("SELECT passord FROM brukere Where brukerid =%s;" % bi_input)
                mycursor.execute(se_po)
                myresult_fra_brukere1 = mycursor.fetchall()



                se_mn = ("SELECT mobil_nr FROM brukere Where brukerid =%s;" % bi_input)
                mycursor.execute(se_mn)
                myresult_fra_brukere2 = mycursor.fetchall()


                se_bid = ("SELECT brukerid FROM brukere Where brukerid =%s;" % bi_input)
                mycursor.execute(se_bid)
                myresult_fra_brukere3 = mycursor.fetchall()

                win7 = sg.Window('Brukere', win7_layout(), return_keyboard_events=True, finalize=True)
                win7.bind("<Return>", "_Enter")
                win7.read(timeout=100)
                tab_win.Hide()
                win7['bn_win7'].update(myresult_fra_brukere)
                win7['bn_win7_1'].update(myresult_fra_brukere1)
                win7['bn_win7_2'].update(myresult_fra_brukere2)
                win7['bn_win7_3'].update(myresult_fra_brukere3)
                ev5, vals5 = win7()
                if ev5 == 'sb_win7' or ev5 == '_Enter':
                    de_b = ("DELETE FROM brukere Where brukerid =%s;" % bi_input)
                    mycursor.execute(de_b)
                    mydb.commit()
                    tab_win.UnHide()
                    win7.Close()
                    tab_win['bid_finn'].update('')
                if ev5 == 'bak_win7' or ev5 == '_Enter':
                    tab_win['bid_finn'].update('')
                    win7.Close()
                    tab_win.UnHide()
        if not vals2['vn_finn'] == '':
            vn_input = vals2['vn_finn']
            if ev2 == 'finn' or ev2 == '_Enter':
                se_vn = ("SELECT vare_nr FROM varer Where vare_nr =%s;" % vn_input)
                mycursor.execute(se_vn)
                myresult_fra_varer = mycursor.fetchall()
                se_pn = ("SELECT produktnavn FROM varer Where vare_nr =%s;" % vn_input)
                mycursor.execute(se_pn)
                myresult_fra_varer1 = mycursor.fetchall()
                se_bs = ("SELECT beskrivelse FROM varer Where vare_nr =%s;" % vn_input)
                mycursor.execute(se_bs)
                myresult_fra_varer2 = mycursor.fetchall()
                se_p = ("SELECT pris FROM varer Where vare_nr =%s;" % vn_input)
                mycursor.execute(se_p)
                myresult_fra_varer3 = mycursor.fetchall()
                se_ka = ("SELECT kategori FROM varer Where vare_nr =%s;" % vn_input)
                mycursor.execute(se_ka)
                myresult_fra_varer4 = mycursor.fetchall()
                se_bl = ("SELECT bilde FROM varer Where vare_nr =%s;" % vn_input)
                mycursor.execute(se_bl)
                myresult_fra_varer5 = mycursor.fetchall()
                se_ln = ("SELECT lager_nr FROM varer Where vare_nr =%s;" % vn_input)
                mycursor.execute(se_ln)
                myresult_fra_varer6 = mycursor.fetchall()

                win8 = sg.Window('varer', win8_layout(), return_keyboard_events=True, finalize=True)
                win8.bind("<Return>", "_Enter")
                win8.read(timeout=100)
                tab_win.Hide()
                win8['vn_win8'].update(myresult_fra_varer)
                win8['pn_win8'].update(myresult_fra_varer1)
                win8['bs_win8'].update(myresult_fra_varer2)
                win8['p_win8'].update(myresult_fra_varer3)
                win8['ka_win8'].update(myresult_fra_varer4)
                win8['bl_win8'].update(myresult_fra_varer5)
                win8['ln_win8'].update(myresult_fra_varer6)
                ev6, vals6 = win8()
                if ev6 == 'sv_win8' or ev6 == '_Enter':
                    de_v = ("DELETE FROM varer Where vare_nr =%s;" % vn_input)
                    mycursor.execute(de_v)
                    mydb.commit()
                    tab_win.UnHide()
                    win8.Close()
                    tab_win['vn_finn'].update('')
                if ev6 == 'bak_win8' or ev6 == '_Enter':
                    tab_win['vn_finn'].update('')
                    win8.Close()
                    tab_win.UnHide()

tabgrp = [[sg.TabGroup([[sg.Tab('Finn', win4_layout()),
                         sg.Tab('Registrer ny vare', win3_layout()),
                         sg.Tab('Registrer ny bruker', win5_layout())
                         ]])]]
win3 = sg.Window('Registrering', win3_layout())
win4 = sg.Window('Finn', win4_layout())
win5 = sg.Window('ny bruker', win5_layout())


login_function()

