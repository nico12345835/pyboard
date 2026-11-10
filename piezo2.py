from  pyb import Timer, Pin
import time
import tm1637

class Note():
    def __init__(self,hauteur=float(),longueur=int(),nom=str()):
        self.hauteur=hauteur
        self.longueur=longueur
        self.nom=nom
        
        
    def play(self):
        self.timer = Timer(5, freq=self.hauteur)
        self.channel = self.timer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=50)
        start=time.ticks_ms()
        while True:
            duree=time.ticks_diff(time.ticks_ms(),start)
            if duree>self.longueur:
                break
            pyb.delay(5)
display = tm1637.TM1637(clk=pyb.Pin('X7'), dio=pyb.Pin('X6'))

dict_note={"do":Note(130,1000,"do"),"re":Note(147,1000,"re"),"mi":Note(165,1000,"mi")}

do=dict_note["do"]
re=dict_note["re"]
mi=dict_note["mi"]


partition=[do,re,mi]

for note in partition:
    note.play()
    display.show(note.nom)

timer.freq(440)
