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
motor_right.reset_position(True)
motor_left.reset_position(True)
print(dir(motor_left))
print(dir(motor_right))
print('Motor starting \n')
while True :
    if keyboard.is_pressed('w'):
        linear=-1.0
        angular=0.0
        right,left=velocity_convertion(angular,linear)
        motor_left.run(power=int(right))
        motor_right.run(power=int(left))
        print("Right weel tacho counter : ",motor_right.get_tacho())
        print("Left wheel tacho counter : ",motor_left.get_tacho())
        time.sleep(0.1)
    if keyboard.is_pressed('s'):
        linear=+1.0
        angular=0.0
        right,left=velocity_convertion(angular,linear)
        motor_right.run(power=int(right))
        motor_left.run(power=int(left))
        print("Right wheel tacho counter : " ,motor_right.get_tacho())
        print("Left wheel tacho counter : " ,motor_left.get_tacho())
        time.sleep(0.1)
    if keyboard.is_pressed('a'):
        motor_right.run(power=80)
        motor_left.brake()
        print("Right wheel tacho counter : " ,motor_right.get_tacho())
        print("Left wheel tacho counter : ",motor_left.get_tacho())
        time.sleep(0.1)
    #     angular+=1.0 
    #     linear=0.0
    #     angular_final=max(angular,60)
    #     right,left=velocity_convertion(angular_final,linear)
    #     motor_left.run(power=int(left*400))
    #     motor_right.run(power=int(right*400))
    if keyboard.is_pressed('d'):
        motor_left.run(power=int(80))
        motor_right.brake()
        print("Right wheel tacho counter : ",motor_right.get_tacho())
        print("Left wheel tacho counter : ",motor_left.get_tacho())
        time.sleep(0.1)
        # angular-=1.0 
        # linear=0.0
        # angular_final=max(angular,60)
        # right,left=velocity_convertion(angular_final,linear)
        # motor_right.run(power=int(right))
        # motor_left.run(power=int(left))
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
