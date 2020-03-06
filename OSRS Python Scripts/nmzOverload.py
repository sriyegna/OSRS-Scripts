import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode
import random

##Have runelite XP tab open to offset the inventory left

button = Button.left
mouse = Controller()

# Coordinates of the items
coords = [[[1448, 936], [1464, 956]], [[1489, 936], [1506, 956]], [[1531, 936], [1550, 956]], [[1571, 936], [1590, 956]],
          [[1448, 971], [1464, 993]], [[1489, 971], [1506, 993]], [[1531, 971], [1550, 993]], [[1571, 971], [1590, 993]]]

##Randomize the interval for mouse movements, then increment ycoord by old-new/interval
#time.sleep(200)

#loop through up to 16 items (*15*) and drink each potion 4 times
for i in range(0, 7):
    print("Overload: " + str(i+1))
    for j in range(0, 4):
        xcoord = random.randint(coords[i][0][0], coords[i][1][0])
        ycoord = random.randint(coords[i][0][1], coords[i][1][1])
        
        mouse.position = (xcoord, ycoord)
        mouse.click(button)
        print(j+1)
        
        sleeptime = random.randint(311, 410) #after 5 mins
        #sleeptime = 70 + random.randint(1, 5) - random.randint(1, 10) #for prayer
        7
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

