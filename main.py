# -*- coding = utf-8 -*-
# @Author : BA7JJQ - Donald

import wiringpi
morsedict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
             'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
             'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
             'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
             'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
             'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
             '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
             '9': '----.', ' ': ' ', '/': '-..-.', '?': '..--..', '.': '.-.-.-', '-': '-....-',
             # '=' means 'CQ CQ CQ DE BA7JJQ BA7JJQ BA7JJQ PSE K'. Change to your own callsign here.
             '=': '-.-. --.- -.-. --.- -.-. --.- -.. . -... .- --... .--- .--- --.- -... .- --... .--- .--- --.- -... .- --... .--- .--- --.- .--. ... . -.-'}


wiringpi.wiringPiSetup()
pin = 6                             # Set GPIO here!
output = 1
high = 1
low = 0
t = 70                              # CW speed setting. How long does 'Dit' takes.
wiringpi.pinMode(pin, output)       # Set pin 6 as output
wiringpi.digitalWrite(pin, high)    # Set the default value of pin 6. You may need to change this if your radio need a 'HIGH' to transmit.


def dit():
    wiringpi.digitalWrite(pin, low)
    wiringpi.delay(t)
    wiringpi.digitalWrite(pin, high)
    wiringpi.delay(t)


def dah():
    wiringpi.digitalWrite(pin, low)
    wiringpi.delay(t*3)
    wiringpi.digitalWrite(pin, high)
    wiringpi.delay(t)


while 1 < 2:
    msg = input('message:')
    msg = msg.lower()

    for m in msg:
        code = morsedict[m]

        if code is None:
            print('character not available')
        elif code is '=':
            print('cq cq cq de ba7jjq ba7jjq ba7jjq pse k')
        else:
            print(m)

        for c in code:
            if c == '.':
                dit()
            elif c == '-':
                dah()
            elif c == ' ':
                wiringpi.delay(t*3)
            else:
                print('code is not available')
        wiringpi.delay(t*3)
