import datetime
import pyglet
from time import sleep


time_now = datetime.datetime.now()
print("Current Time:", time_now)


music = pyglet.media.load('demoslayer.mp3')  

print("Enter Day:")
day = int(input())  
print("Enter Hour:")
hour = int(input())  
print("Enter Minutes:")
minutes = int(input())  


while True:
    time_now = datetime.datetime.now()
    if time_now.day == day and time_now.hour == hour and time_now.minute == minutes:
        print("Playing music!")
        music.play()
        pyglet.app.run()  
        break 
    sleep(1)
