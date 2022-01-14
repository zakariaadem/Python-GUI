from turtle import color
import PySimpleGUI as sg
 
# Design pattern 2 - First window remains active
 
def win1_layout():
    layout = [
        [sg.Text('Registrering av varer', text_color='black'),],
        [sg.Text('Varenummer', size =(15, 1)), sg.InputText()],
        [sg.Text('Produktnavn', size =(15, 1)), sg.InputText()],
        [sg.Text('Beskrivelse', size =(15, 1)), sg.InputText()],
        [sg.Text('Pris', size =(15, 1)), sg.InputText()],
        [sg.Text('Kategori', size =(15, 1)), sg.InputText()],
        [sg.Text('Lager', size =(15, 1)), sg.InputText()],
        [sg.Text('Bilde src', size =(15, 1)), sg.InputText()],
        [sg.Button('Lagre')]
        ]
 
    return layout
 

 
win1 = sg.Window('Window 1', win1_layout())
 
win2_active = False
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
        break
 
