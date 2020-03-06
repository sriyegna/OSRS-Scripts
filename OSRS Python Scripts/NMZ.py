import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random

##Have runelite XP tab open to offset the inventory left

button = Button.left
mouse = Controller()

# Coordinates of the items
coords = [[[1448, 795], [1464, 816]], [[1489, 795], [1506, 816]], [[1531, 795], [1550, 816]], [[1571, 816], [1590, 816]],
          [[1448, 824], [1464, 853]], [[1489, 824], [1506, 853]], [[1531, 824], [1550, 853]], [[1571, 824], [1590, 853]],
          [[1448, 864], [1464, 885]], [[1489, 864], [1506, 885]], [[1531, 864], [1550, 885]], [[1571, 864], [1590, 885]],
          [[1448, 899], [1464, 919]], [[1489, 899], [1506, 919]], [[1531, 899], [1550, 919]], [[1571, 899], [1590, 919]]]

##Randomize the interval for mouse movements, then increment ycoord by old-new/interval
#time.sleep(200)

#loop through up to 16 items (*15*) and drink each potion 4 times
for i in range(0, 11):
    print("Pot: " + str(i+1))
    for j in range(0, 4):
        xcoord = random.randint(coords[i][0][0], coords[i][1][0])
        ycoord = random.randint(coords[i][0][1], coords[i][1][1])
        
        mouse.position = (xcoord, ycoord)
        mouse.click(button)
        print(j+1)
        
        sleeptime = random.randint(250, 330) #110 - 250
        #sleeptime = 70 + random.randint(1, 5) - random.randint(1, 10) #for prayer
        
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

