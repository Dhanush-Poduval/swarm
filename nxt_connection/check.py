import nxt.locator 
from nxt.motor import Motor,Port
import time
import keyboard
brick=nxt.locator.find()
print("Connected to : ",brick.get_device_info())
motor_right=Motor(brick,Port.A)
motor_left=Motor(brick,Port.B)
print('Motor starting \n')
while True :
    if keyboard.is_pressed('w'):
        motor_left.run(power=80)
        motor_right.run(power=80)
    if keyboard.is_pressed('s'):
        motor_right.run(power=-80)
        motor_left.run(power=-80)
    if keyboard.is_pressed('a'):
        motor_left.brake()
        motor_right.run(power=80)
    if keyboard.is_pressed('d'):
        motor_right.brake()
        motor_left.run(power=80)
    if keyboard.is_pressed('q'):
        motor_right.brake()
        motor_left.brake()
        break
#motor_right.run(power=0)
#motor_left.run(power=-80)
#time.sleep(10)
#motor_right.brake()
#motor_left.brake()
print("Motor stopped \n")
