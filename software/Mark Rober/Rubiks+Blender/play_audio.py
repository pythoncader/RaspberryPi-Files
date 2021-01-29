#Help from https://learn.adafruit.com/adafruit-crickit-hat-for-raspberry-pi-linux-computers/raspberry-pi-test
#           https://stackoverflow.com/questions/89228/how-to-call-an-external-command
# plays an mp3 file with command "sudo python3 <mp3location.mp3>"

import subprocess
import os
import sys

#mp3file = sys.argv[1]
#os.system ("mpg123 zelda.mp3")
subprocess.Popen(["mpg123", "Late_Night_Drive.mp3"])

