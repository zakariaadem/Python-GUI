from typing import Sized
import PySimpleGUI as sg
 
sg.theme('Reddit')
 
layout = [
    [sg.Text('My one-shot window.')],
    [sg.InputText(key='-IN-')],
    [sg.Submit(), sg.Cancel()]
]
 
window = sg.Window('Dette er tittelen til vinduet',layout, size=(1000, 500))
 
event, values = window.read()
 
window.close()
text_input = values['-IN-']
 
sg.popup('You entered', text_input)