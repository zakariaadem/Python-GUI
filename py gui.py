from ast import Break
from tkinter import Text
from turtle import color
import PySimpleGUI as sg
 
# Design pattern 2 - First window remains active
 
def win1_layout():
    layout = [
        [sg.Text('Registrering av varer', text_color='black')],
        [sg.Text('Varenummer', size =(15, 1)), sg.InputText(key='Varenummer')],
        [sg.Text('Produktnavn', size =(15, 1)), sg.InputText(key='Produktnavn')],
        [sg.Text('Beskrivelse', size =(15, 1)), sg.InputText(key='Beskrivelse')],
        [sg.Text('Pris', size =(15, 1)), sg.InputText(key='Pris')],
        [sg.Text('Kategori', size =(15, 1)), sg.InputText(key='Kategori')],
        [sg.Text('Lager', size =(15, 1)), sg.InputText(key='Lager')],
        [sg.Text('Bilde src', size =(15, 1)), sg.InputText(key='Bilde src')],
        [sg.Button('Lagre')],
    ]
 
    return layout

def win2_layout():
    layout = [
        [sg.Text('Registrering av varer', text_color='black')],
        [sg.Text('Varenummer', size =(15, 1)), sg.Text('test', size=(15, 1), key='Varenummer2')],
        [sg.Text('Produktnavn', size =(15, 1))],
        [sg.Text('Beskrivelse', size =(15, 1))],
        [sg.Text('Pris', size =(15, 1))],
        [sg.Text('Kategori', size =(15, 1))],
        [sg.Text('Lager', size =(15, 1))],
        [sg.Text('Bilde src', size =(15, 1))],
        
    ]
    return layout

win1 = sg.Window('Registrering', win1_layout())
win2 = sg.Window('Registrering', win2_layout())

 
while True:
    ev1, vals1 = win1.read(timeout=100)
    if ev1 == sg.WIN_CLOSED:
        break

    if ev1 == 'Lagre':
        win1.Hide()
        win2.read(timeout=100)
        win2['Varenummer2'].update(vals1['Varenummer'])
        
 
