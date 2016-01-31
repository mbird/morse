## program outline
## ask user for message to convert into morse code
## check message for unknown characters
## if unknown characters found, show unknown characters and ask for correction


import winsound
import time

# set parameters for beep sound
freq = 1300 # set frequency of the tone used for morse code
di = 150 # set duration for "di's" to 200 ms
dah = 3 * di # set duration for "dah's" to 3 times di
dit = di # set duration for "dit's" to di
char = float(3 * di / 1000) # set duration between characters to 3 times di
space = float(7 * di / 1000) # set duration between words to 7 times di


# morse alphabet
morse = {"A" : (di, dah),
         "B" : (dah, di, di, dit),
         "C" : (dah, di, dah, dit),
         "D" : (dah, di, dit),
         "E" : (dit,),
         "F" : (di, di, dah, dit),
         "G" : (dah, dah, dit),
         "H" : (di, di, di, dit),
         "I" : (di, dit),
         "J" : (di, dah, dah, dah),
         "K" : (dah, di, dah),
         "L" : (di, dah, di, dit),
         "M" : (dah, dah),
         "N" : (dah, dit),
         "O" : (dah, dah, dah),
         "P" : (di, dah, dah, dit),
         "Q" : (dah, dah, di, dah),
         "R" : (di, dah, dit),
         "S" : (di, di, dit),
         "T" : (dah,),
         "U" : (di, di, dah),
         "V" : (di, di, di, dah),
         "W" : (di, dah, dah),
         "X" : (dah, di, di, dah),
         "Y" : (dah, di, dah, dah),
         "Z" : (dah, dah, di, dit),
         "0" : (dah, dah, dah, dah, dah),
         "1" : (di, dah, dah, dah, dah),
         "2" : (di, di, dah, dah, dah),
         "3" : (di, di, di, dah, dah),
         "4" : (di, di, di, di, dah),
         "5" : (di, di, di, di, dit),
         "6" : (dah, di, di, di, dit),
         "7" : (dah, dah, di, di, dit),
         "8" : (dah, dah, dah, di, dit),
         "9" : (dah, dah, dah, dah, dit),
         "." : (di, dah, di, dah, di, dah),
         "," : (dah, dah, di, di, dah, dah),
         ":" : (dah, dah, dah, di, di, dit),
         "?" : (di, di, dah, dah, di, dit),
         "´" : (di, dah, dah, dah, dah, dit),
         "-" : (dah, di, di, di, di, dah),
         "/" : (dah, di, di, dah, dit),
         "(" : (dah, di, dah, dah, di, dah),
         ")" : (dah, di, dah, dah, di, dah),
         '"' : (di, dah, di, di, dah, dit),
         "'" : (di, dah, di, di, dah, dit),
         "@" : (di, dah, dah, di, dah, dit),
         "=" : (dah, di, di, di, dah),
         " " : ()}

message = input("Please enter your message: ").upper()

for letter in message:
    if letter not in morse:
        print ("'" + letter + "'" + " is no valid character. Please rephrase your message.")
        break
        if letter == " ":
            time.sleep(space)
        else:
            for tone in morse[letter]:
                winsound.Beep(freq, tone)
            time.sleep(char)
