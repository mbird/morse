import winsound
import time

# Create beep sound
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second
##winsound.Beep(Freq,Dur)
##time.sleep(0.1) # wait for 0.1 seconds


# create di
Freq = 2500 # Set Frequency To 2500 Hertz
di = 200 # Set Duration To 200 ms
##winsound.Beep(Freq,di)
##time.sleep(0.2) # wait for 0.2 seconds

# create dah
Freq = 2500 # Set Frequency To 2500 Hertz
dah = 600 # Set Duration To 600 ms
##winsound.Beep(Freq,dah)
##time.sleep(0.2) # wait for 0.2 seconds

# morse alphabet
morse = {"A" : (di, dah),
         "B" : (dah, di, di, di),
         "C" : (dah, di, dah, di),
         "D" : (dah, di, di),
         "E" : (di,),
         "F" : (di, di, dah, di),
         "G" : (dah, dah, di),
         "H" : (di, di, di, di)}

message = "ABC"

for letter in message:
    for tone in morse[letter]:
        winsound.Beep(Freq, tone)
        time.sleep(0.2)
