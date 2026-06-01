import nxt.locator
from nxt.motor import Motor, Port
import time 

brick=nxt.locator.find()
motor=Motor(brick,Port.A)
motor.reset_position(True)
motor.run(power=80)
for _ in range(20):
    print(motor.get_tacho())
    time.sleep(0.1)
motor.brake()
