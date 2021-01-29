#startup sequence

import PCAde9685
servo= PCAde9685.Servo(0)
servo.set_angle(125)
servo.set_angle(90)
servo.set_angle(65)

servo.glide_angle(65, 125, 5)
servo.glide_angle(125, 65, 2)