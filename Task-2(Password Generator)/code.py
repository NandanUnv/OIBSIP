
'''
     Task-2 of Oasis InfoByte:
                "Random Password Generator USING PyQt GUI"
                                                            '''
import pyperclip

import PySimpleGUIQt as sg

import random as ra

sg.theme('DarkBrown3')

l_c = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
       'r', 's', 't', 'u', 'v','w', 'x', 'y', 'z']
uc = []
dt = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sp = ['!', '@', '#', '$', '%', '^', '&', '*', '-', '_', '+', '?']

for i in l_c:
    d = i.upper()
    uc.append(d)

form = sg.FlexForm("Password Generator", size=(450, 150))

layout = [[sg.Text("Hi, I am Password Generator!")],
          [sg.Text("")],
          [sg.Text("Do you want to me to create password?")],
          [sg.Text("")],
          [sg.Yes(), sg.No()]
          ]
button, val = form.Layout(layout).Read()

if button == 'No':

    sg.popup_timed(f'Ok,\nThank You!')  # The popup will be closed automatically
    form.close()

elif button == 'Yes':

    form.close()
    pas = ''
    p = []

    form = sg.FlexForm("Password Generator")

    layout = [[sg.Text("Fill the below details:")],
              [sg.Text("no.of lower cases in your password:", size=(35, 1.4)), sg.InputText()],
              [sg.Text("no.of upper cases in your password:", size=(35, 1.4)), sg.InputText()],
              [sg.Text("no.of digits in your password:", size=(35, 1.4)), sg.InputText()],
              [sg.Text("no.of spl_characters in your password:", size=(35, 1.4)), sg.InputText()],
              [sg.Button('Continue')]
              ]

    button, val = form.Layout(layout).Read()

    if button == 'Continue':
        for i in range(int(val[0])):
            a = ra.choice(l_c)
            p.append(a)
        for i in range(int(val[1])):
            a = ra.choice(uc)
            p.append(a)
        for i in range(int(val[2])):
            a = ra.choice(dt)
            p.append(a)
        for i in range(int(val[3])):
            a = ra.choice(sp)
            p.append(a)

    form.close()

    ra.shuffle(p)

    for i in p:
        pas = pas + i

    pyperclip.copy(pas)  # The password is copied to clipboard

    sg.popup(f'Your Password: {str(pas)} \nLength of your password:{len(pas)} \nThe password is copied to clipboard',
             title='Password')

else:
    form.close()

'''
    code by: U.Nandan Varma
                            '''
