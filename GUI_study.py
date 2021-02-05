import easygui
#easygui.msgbox("Hello there!")

#user_response = easygui.msgbox("Hello there!")
#print(user_response)

flavor = easygui.buttonbox("What is your favourite ice cream flavour?", choices = ['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " +flavor)

flavor = easygui.choicebox("What is your favourite ice cream flavour?", choices = ['Vanilla', 'Chocolate', 'Strawberry'])
easygui.msgbox("You picked " +flavor)


# flavor = easygui.enterbox("What is your favourite ice cream flavor?")
# easygui.msgbox("You entered " + flavor)

import random, easygui

def number_guessing():
    secret = random.randint(1,100)
    guess = 0
    tries = 0
    easygui.msgbox("""AHOY! I'm the Dread Prate Roberts, and I have a secret! It's a number from 1 to 100. I'll give you 6 tries.""")
    while guess != secret and tries < 6:
        guess = easygui.integerbox("what's yer guess, matex?", upperbound = 100)
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


