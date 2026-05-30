import nxt.locator 
from nxt.motor import Motor,Port
import time
import keyboard
angular=0
L=0.12
def velocity_convertion(angular:float , linear:float ):
    v_right=(linear+((L/2)*angular))*100
    v_left=(linear-((L/2)*angular))*100
    return v_right,v_left
brick=nxt.locator.find()
print("Connected to : ",brick.get_device_info())
motor_right=Motor(brick,Port.A)
motor_left=Motor(brick,Port.B)
print('Motor starting \n')
while True :
    if keyboard.is_pressed('w'):
        linear=1.0
        angular=0.0
        right,left=velocity_convertion(angular,linear)
        motor_left.run(power=int(right))
        motor_right.run(power=int(left))
    if keyboard.is_pressed('s'):
        linear=-1.0
        angular=0.0
        right,left=velocity_convertion(angular,linear)
        motor_right.run(power=int(right*400))
        motor_left.run(power=int(left*400))
    if keyboard.is_pressed('a'):
        angular+=1.0 
        linear=0.0
        angular_final=max(angular,60)
        right,left=velocity_convertion(angular_final,linear)
        motor_left.run(power=int(left*400))
        motor_right.run(power=int(right*400))
    if keyboard.is_pressed('d'):
        angular-=1.0 
        linear=0.0
        angular_final=max(angular,60)
        right,left=velocity_convertion(angular_final,linear)
        motor_right.run(power=int(right))
        motor_left.run(power=int(left))
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
