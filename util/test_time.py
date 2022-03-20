from time import localtime
from pygame import mixer
import time

#H = input(" Coloque a hora   ")

M = input(" Coloque o minuto   ")

x = time.localtime()
tempo = x[4]
afterTime = tempo + int(M)


while 1:
    print(afterTime)
    print(localtime().tm_min)
    if localtime().tm_min == int(afterTime):
        print("ACORDE")
        mixer.init()
        mixer.music.load("musica.mp3")
        mixer.music.play()
        break
#localtime().tm_hour == int(H) and