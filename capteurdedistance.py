from time import sleep
from ultrasonic import Ultrasonic
import tm1637

display = tm1637.TM1637(clk=pyb.Pin('X3'), dio=pyb.Pin('X4'))
sr04 = Ultrasonic( pyb.Pin('X1'), pyb.Pin('X2') )

while True:
    try:
        distance=sr04.distance_in_cm()
    except:
        distance=None
    print(distance)
    
    if distance!=None:
        display.number(int(distance))
    sleep(0.5)




