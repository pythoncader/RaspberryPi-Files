import os
#sudo apt-get install espeak
import sys
from time import sleep
sleep(5)
os.system("espeak 'Hello World' 2>/dev/null")

myarguments = sys.argv
mytext = ""
for i in range(1, len(myarguments)):
	mytext = f"{mytext} {myarguments[i]}"
#mytext = str(input("What do you want to say?\n"))

#add some quotes to the text so that the espeak command gets the text as a string and not a list of strings
mytext = "\""+mytext+"\""
print(mytext)
#wait for the user to be ready to hear the text
commandbeginning = "espeak"
voiceoption = "-v"
american = "en-us"
french = "fr"
spanish = "es"
african = "af"
malevoices = ["+m1", "+m2", "+m3", "+m4", "+m5", "+m6", "+m7"]
femalevoices = ["+f1", "+f2", "+f3", "+f4"]
croak = "+croak"
whisper = "+whisper"
speed = "-s" #speed of speech in words per minute (-s{integer speed})
pause = "-g" #pause between words in milliseconds (-g{integer pause})
speaktextfile = "-f" #-f {textfile} to read the contents
pitch = "-p" #set the integer value of the pitch (0-99) default 50
volume = "-a" #set the integer volume (0-200) default 100
outputtowav = "-w" #Don't speak the text, just write it to a .wav file

commandend = ' 2>/dev/null' # To dump the std errors to /dev/null
os.system(f"{commandbeginning} {voiceoption}{american}{femalevoices[2]} {mytext} {commandend}")
