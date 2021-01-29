import PCAde9685
ankle_1, knee_1, hip_1 = PCAde9685.Servo(0), PCAde9685.Servo(1), PCAde9685.Servo(2) 
wait_time = 1


while True:
    knee_1.set_angle(0,0)



