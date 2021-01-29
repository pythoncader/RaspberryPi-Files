import random
import PCAde9685
from time import sleep

myrandom = 0
mypass = 0
top3 = 0
top1 = 1
bottom3 = 2
top4 = 3
bottom4 = 4
bottom2 = 5
bottom1 = 6
top2 = 7

min0 = 25
max0 = 80

min1 = 32
max1 = 78

min2 = 72
max2 = 110

min3 = 95
max3 = 170

min4 = 32
max4 = 82

min5 = 85
max5 = 132

min6 = 75
max6 = 85

min7 = 30
max7 = 60

def pickrandom(channel):
    if channel == 0:
        myrandom = random.randrange(min0, max0)
        return myrandom
    if channel == 1:
        myrandom = random.randrange(min1, max1)
        return myrandom
    if channel == 2:
        myrandom = random.randrange(min2, max2)
        return myrandom
    if channel == 3:
        myrandom = random.randrange(min3, max3)
        return myrandom
    if channel == 4:
        myrandom = random.randrange(min4, max4)
        return myrandom
    if channel == 5:
        myrandom = random.randrange(min5, max5)
        return myrandom
    if channel == 6:
        myrandom = random.randrange(min6, max6)
        return myrandom
    if channel == 7:
        myrandom = random.randrange(min7, max7)
        return myrandom
    if channel == 8:
        myrandom = random.randrange(min8, max8)
        return myrandom
    
def pumpkin_random():
    top_1.set_angle(pickrandom(top1), 0)
    top_2.set_angle(pickrandom(top2), 0)
    top_3.set_angle(pickrandom(top3), 0)
    top_4.set_angle(pickrandom(top4), 0)
    bottom_1.set_angle(pickrandom(bottom1), 0)
    bottom_2.set_angle(pickrandom(bottom2), 0)
    bottom_3.set_angle(pickrandom(bottom3), 0)
    bottom_4.set_angle(pickrandom(bottom4), 0)
    
    sleep(random.randrange(0, 500)/1000)
    
top_1 = PCAde9685.Servo(top1)
top_2 = PCAde9685.Servo(top2)
top_3 = PCAde9685.Servo(top3)
top_4 = PCAde9685.Servo(top4)
bottom_1 = PCAde9685.Servo(bottom1)
bottom_2 = PCAde9685.Servo(bottom2)
bottom_3 = PCAde9685.Servo(bottom3)
bottom_4 = PCAde9685.Servo(bottom4)

    
while True:
    top_2.set_angle(min7)
    top_2.set_angle(max7)
