import winsound
import time

# set parameters for beep sound
Freq = 2500 # set frequency to 2500 Hertz
di = 200 # set duration for "di's" to 200 ms
dah = 600 # set duration for "dah's" to 200 ms
dit = 200 # set duration for "dit's" to 200 ms


# morse alphabet
morse = {"A" : (di, dah),
         "B" : (dah, di, di, dit),
         "C" : (dah, di, dah, dit),
         "D" : (dah, di, dit),
         "E" : (dit,),
         "F" : (di, di, dah, dit),
         "G" : (dah, dah, dit),
         "H" : (di, di, di, dit)}

message = "ABC"

for letter in message:
    for tone in morse[letter]:
        winsound.Beep(Freq, tone)
        time.sleep(0.2)
