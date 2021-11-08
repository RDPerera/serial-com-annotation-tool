import time
import random
from playsound import playsound

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print("Playing "+timer, end="\r")
        time.sleep(1)
        t -= 1
    print('Ended...')

musicList=["HAHV1"]
log = open("log.txt", "a")
randomIdx=random.randint(0, len(musicList)-1)
music = musicList[randomIdx]
musicList.remove(music)
start = time.time()
print('Selected Music Track : '+music)
playsound('Music/'+music+'.wav',False)
countdown(30)
end = time.time()
print("")
print("Seleted Music Track : "+music+" Start Time : "+str(start)+" End Time : "+str(end) +" Duration : "+str(end-start),file=log)

