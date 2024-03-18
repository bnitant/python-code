#Only for pc users
import datetime
from pygame import mixer
import time

t_date=datetime.datetime.now().strftime('%H:%M:%S')
#os.system('cls')
print(t_date)

def play_song(time):
    try:
        
        while True:
            t_date=datetime.datetime.now().strftime('%H:%M:%S')
            if t_date==time:
                
                a='empathy.mp3'
                mixer.init()
                mixer.music.load(a)
                mixer.music.set_volume(0.05)
                mixer.music.play()
                stop=input('if you want to stop the alarm enter s : ')
                if stop=='s':
                    mixer.music.stop()
                    break  
    except Exception as e:
        print('Please try again by entering the time again or check the alarm tune name and path: ',e)
    
time=input('Enter the alarm time in (H:M:S) format : ')
play_song(time)
