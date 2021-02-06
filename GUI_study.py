# EasyGui-Studies


import easygui, random
#easygui.msgbox("Hello there!")

#user_response = easygui.msgbox("Hello there!")
#print(user_response)

# flavor = easygui.buttonbox("What is your favourite ice cream flavour?", choices = ['Vanilla', 'Chocolate', 'Strawberry'])
# easygui.msgbox("You picked " +flavor)

# flavor = easygui.choicebox("What is your favourite ice cream flavour?", choices = ['Vanilla', 'Chocolate', 'Strawberry'])
# easygui.msgbox("You picked " +flavor)


# flavor = easygui.enterbox("What is your favourite ice cream flavor?")
# easygui.msgbox("You entered " + flavor)


def number_guessing():
    secret = random.randint(1,100)
    guess = 0
    tries = 0
    easygui.msgbox("""AHOY! I'm the Dread Prate Roberts, and I have a secret! It's a number from 1 to 100. I'll give you 6 tries.""")
    while guess != secret and tries < 6:
        guess = easygui.integerbox("what's yer guess, matey?", upperbound = 100)
        if not guess: break
        if guess < secret:
            easygui.msgbox(str(guess) + " is too low, ye scurvy dog!")
        elif guess > secret:
            easygui.msgbox(str(guess) + " is too high, landlubber!")
        tries += 1
    if guess == secret:
        easygui.msgbox("Avast! Ye got it! Found my secret, ye did!")
    else:
        easygui.msgbox("No more guesses! The number was " + str(secret))

# number_guessing()

# test_change = "This is a test change to check if I can push onto the repo"

# ___________________________________________________________________________________________________________________________________________
# -------------------------------------------------------------------------------------------------------------------------------------------

import tkinter as tk

HEIGHT = 400
WIDTH = 700
TIMER = "Here will be the timer"

# root = tk.Tk()

# canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
# canvas.pack()

# frame = tk.Frame(root, bg = '#80c1ff') #I can do hex-colors!
# frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8) #expand and fill will fill out the frame

# button = tk.Button(frame, text = "Test  button", bg= "gray")
# button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)


# label = tk.Label(frame, text= "This is a label", bg= "yellow")
# label.place(relx=0.3,rely=0,relwidth=0.45, relheight=0.25)

# entry = tk.Entry(frame, bg='green')
# entry.place(relx=0.8, rely=0, relwidth= 0.2, relheight = 0.25)


# root.mainloop()


root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80f3cc', bd = 5)
frame.place(relx=0., rely=0, relwidth=1, relheight=1)

timer_frame = tk.Frame(root, bg='green', bd=5)
timer_frame.place(relx= 0.5, rely=0.1, relwidth= 0.5, relheight= 0.4, anchor='n')

Timer_label = tk.Label(timer_frame, text=TIMER)
Timer_label.place(relwidth=1,relheight=1)

Settings_button = tk.Button(frame, text='Settings', bg='gray')
Settings_button.place(relx=0.25, rely=0.7, relwidth=0.2, relheight= 0.2, anchor='n')

Start_button = tk.Button(frame, text='Start', bg='gray')
Start_button.place(relx=0.5, rely=0.7, relwidth=0.2, relheight=0.2, anchor='n')

Preset_button = tk.Button(frame, text='Timer-Presets', bg='gray')
Preset_button.place(relx=0.75, rely=0.7, relwidth=0.2, relheight=0.2, anchor='n')




root.mainloop()