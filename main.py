from  pyb import Timer, Pin
import time

class Note():
    def __init__(self):
        self.hauteur=int()
        self.longueur=float()
        
        
    def play(self):
        self.timer = Timer(5, freq=self.hauteur)
        self.channel = self.timer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=50)
        start=time.ticks_ms()
        while True:
            duree=time.ticks_diff(time.ticks_ms(),start)
            if duree>self.longueur:
                break
            pyb.delay(5)
            
do=Note()
do.hauteur=130
do.longueur=1000

re=Note()
re.hauteur=147
re.longueur=1000

mi=Note()
mi.hauteur=165
mi.longueur=1000

partition=[do,re,mi]

for Note in partition:
    Note.play()

timer.freq(440)