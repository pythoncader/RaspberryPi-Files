import RPi.GPIO as GPIO
import datetime
from time import sleep
 
def shutdown(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\nshutdown button pressed at ' + str(datetime.datetime.now()))
        sleep(0.5)
    else:
        print('\nshutdown button released at ' + str(datetime.datetime.now()))
        print("shutting down")
        sleep(0.5)
        #os.system("sudo shutdown now -h")
def restart(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('\nrestart button pressed at ' + str(datetime.datetime.now()))
        sleep(0.5)
    else:
        print('\nrestart button released at ' + str(datetime.datetime.now()))
        print("restarting...")
        sleep(0.5)
        #os.system("sudo reboot")
 
try:
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(26, GPIO.IN)
    GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(26, GPIO.BOTH, callback=shutdown)
    GPIO.add_event_detect(21, GPIO.BOTH, callback=restart)
 
    message = input('\nPress Enter to exit.\n')
 
finally:
    GPIO.cleanup()
 
print("Goodbye!")