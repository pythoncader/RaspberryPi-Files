from time import sleep
import sys
# Import the PCA9685 module.
import Adafruit_PCA9685

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(busnum=3)

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 120
servo_max = 668
servofrequency = 60
# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(servofrequency)

class ServoGroup:
    #frequency is the number of pulses per second
    #each pulse has 4096 clock sections
    #on: The tick (between 0 and 4095) when the signal should transition from low to high
    #off:the tick (between 0 and 4095) when the signal should transition from high to low

    def __init__(self, num_of_servos, *channels, currentAngle="unknown", infoPrint=True):
        self.currentAngle = currentAngle
        self.infoPrint = infoPrint
        self.num_of_servos = num_of_servos
        self.channels = channels #tuple of channels
        if len(self.channels) != num_of_servos:
            sys.exit("\n\nDid not give enough channels for servos!\n")

    def __str__(self):
        return f"{self.num_of_servos} servos on channels {self.channels} at {self.currentAngle} degrees"

    def set_infoPrint(self, infoPrint):
        self.infoPrint = infoPrint

    def set_angle(self, angle=90, time=1, clockStart=0):
        self.currentAngle = angle
        dutycycle = angle/180
        pulse_width = 548 * dutycycle + 120
        pulse_width = int(pulse_width)

        if clockStart >= 0 and clockStart <= 4095:
            for channel in self.channels:
                pwm.set_pwm(channel, clockStart, pulse_width + clockStart)
                #pwm.set_pwm(channel, on , off) #on and off are 12-bit values so they are in between 0 and 4095
                #pwm.set_pwm_freq(freq) in hz
        else:
            for channel in self.channels:
                print("Invalid clock start time, resetting to zero...")
                pwm.set_pwm(channel, 0, pulse_width)

        if self.infoPrint == True:
            print(f"Setting servos on channels {self.channels} to {self.currentAngle} on clock starting time {clockStart}")
        sleep(time)


class Servo:
    #frequency is the number of pulses per second
    #each pulse has 4096 clock sections
    #on: The tick (between 0 and 4095) when the signal should transition from low to high
    #off:the tick (between 0 and 4095) when the signal should transition from high to low

    def __init__(self, channel, currentAngle="unknown", infoPrint=True):
        self.channel = channel
        self.currentAngle = currentAngle
        self.infoPrint = infoPrint

    def __str__(self):
        return f"Servo on channel {self.channel} at {self.currentAngle} degrees"

    def set_infoPrint(self, infoPrint):
        self.infoPrint = infoPrint

    def set_angle(self, angle=90, time=1, clockStart=0):
        self.currentAngle = angle
        dutycycle = angle/180
        pulse_width = 548 * dutycycle + 120
        pulse_width = int(pulse_width)

        if clockStart >= 0 and clockStart <= 4095:
            pwm.set_pwm(self.channel, clockStart, pulse_width + clockStart)
            #pwm.set_pwm(channel, on , off) #on and off are 12-bit values so they are in between 0 and 4095
            #pwm.set_pwm_freq(freq) in hz
        else:
            print("Invalid clock start time, resetting to zero...")
            pwm.set_pwm(self.channel, 0, pulse_width)

        if self.infoPrint == True:
            print(f"Setting Servo on channel {self.channel} to {self.currentAngle} on clock starting time {clockStart}")
        sleep(time)
    
    def glide_angle(self, startingAngle, endingAngle, timeToTake):
        if self.infoPrint == True:
            print(f"Gliding from angle {startingAngle} to {endingAngle} in {timeToTake} seconds")
            self.infoPrint = False
            glidingInfoPrint = True
        else:
            glidingInfoPrint = False

        time_interval = timeToTake/abs((startingAngle - endingAngle))
        self.set_angle(startingAngle, 0.5)
        if startingAngle < endingAngle:
            for i in range(startingAngle+1, endingAngle+1):
                self.set_angle(i, time_interval)
        else:
            neg_angle = startingAngle - 1
            while neg_angle != endingAngle:
                neg_angle -= 1
                self.set_angle(neg_angle, time_interval)
        if glidingInfoPrint == True:
            self.infoPrint = True
                
        
if __name__ == "__main__":
    knee_1 = Servo(0)
    
    for i in range(0, 181):
        knee_1.set_angle(i, time=0)
