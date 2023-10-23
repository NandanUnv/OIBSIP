'''
     Task-1 of Oasis InfoByte:
                "BMI CALCULATOR USING PyQt GUI"
                                                   '''

import PySimpleGUIQt as sg

db = {}
count = 1

sg.theme('BlueMono')

condition = True

# Function for finding of BMI Stage

def st_BMI(BMI):

    if BMI < 18.5:
        sg.popup("BMI is:", BMI, "\nYou are Underweight")

    elif BMI >= 18.5 and BMI <= 22.9:
        sg.popup("BMI is:", BMI, "\nYou are Normal")

    elif BMI >= 23 and BMI <= 24.9:
        sg.popup("BMI is:", BMI, "\nYou are Overweight")

    elif BMI >= 25 and BMI <= 29.9:
        sg.popup("BMI is:", BMI, "\nYou are Pre-Obese")

    else:
        sg.popup("BMI is:", BMI, "\nYou are Obese")


while condition:

    # Creation of GUI with title, size and info and user inputs
    form = sg.FlexForm("BMI Calculator", size=(400, 160))

    myl = [[sg.Text("                 ! Find your BMI !            ")],
           [sg.Text("height in meters:", size=(20, 1)), sg.InputText()],
           [sg.Text("weight in kgs:", size=(20, 1)), sg.InputText()],
           [sg.OK(), sg.Button('Next'),sg.Button('History')]
           ]

    button, values = form.Layout(myl).Read()

    # If 'OK' button is chosen then you can't enter other person's data
    if button == 'OK':
        res = float(values[1]) / (float(values[0])) ** 2
        BMI = round(res, 1)
        db[count]=BMI
        count+=1
        st_BMI(BMI)
        sg.popup("BMi's of your people are:", db)
        break

    # If 'Next' is chosen the popup gives you BMI value and allow to enter other person's data
    elif button=='Next':
        res = float(values[1]) / (float(values[0])) ** 2
        BMI = round(res, 1)
        db[count]=BMI
        count+=1
        st_BMI(BMI)

    # if 'History' is chosen the GUI will provide BMI of every person you entered in dictionary format
    # where key refers to person no./id and values refers to BMI of them respectively
    elif button == 'History':
        sg.popup("BMi's of your people are:", db)

    # if ' is chosen the GUI will be closed and code will terminated
    else:
        condition = False

form.close()

''' 
    Code by: U.Nandan Varma
                                '''
