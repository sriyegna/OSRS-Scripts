import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random

##Have runelite XP tab open to offset the inventory left

button = Button.left
mouse = Controller()


##Randomize the interval for mouse movements, then increment ycoord by old-new/interval
#time.sleep(200)

#loop through up to 16 items (*15*) and drink each potion 4 times
for i in range(0, 2000):
    print("Pray Flick: " + str(i+1))
    xcoord = random.randint(1459,1480)
    ycoord = random.randint(111, 127)
        
    mouse.position = (xcoord, ycoord)
    mouse.click(button)
    time.sleep(0.4)
    mouse.click(button)
    
    sleeptime = random.randint(31, 54) #110 - 250
        
        #Alert for upcoming click
    print("Going to sleep for: " + str(sleeptime) + " seconds.")
    for k in range(sleeptime, 0, -1):
        if (k == 30):
            print("30s left.")
        elif (k == 20):
            print("20s left.")                
        elif (k == 10):
            print("10s left.")                                
        time.sleep(1)
    
    #Random wait that isnt a whole integer
    time.sleep(random.random())        

